import os
import requests
import pytz
from .models import Message, Client, Mail
from main_app.celery import app
from datetime import datetime
from dotenv import load_dotenv
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

load_dotenv()
URL_API = os.getenv('URL_API')
TOKEN_API = os.getenv('TOKEN_API')

@app.task(bind=True, retry_backoff=True, max_retries = 25)
def send_api(self, client_id, mail_id, url=URL_API, token=TOKEN_API):

    mail = Mail.objects.get(pk=mail_id)
    client = Client.objects.get(pk=client_id)
    message = Message.objects.filter(id_mail_id=mail.id,
                                     id_client_id=client.id).get()
    phonenumbers = str(client.phone_number.country_code) + str(
        client.phone_number.national_number)
    dt = datetime.now(pytz.timezone(client.time_zone))
    data = {
        'id': message.id,
        "phone": phonenumbers,
        "text": mail.text
        }
    if mail.date_start <= dt <= mail.date_finish and message.status == 'Ready' \
            or message.status == 'Error':
        header = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'}

        response = requests.post(url=url + str(data['id']), headers=header,
                            json=data)
        if response.status_code == 200:
            print(response.status_code)
            message.status = 'Sent'
            message.save()
            logger.info(
                        f"Object: "
                        f"Message ID - {message.id}, "
                        f"Phone - {phonenumbers},"
                        f"CHANGE status - {message.status}"
            )
        else:
            print(response.status_code)
            message.status = 'Error'
            message.save()
            logger.info(
                f"Object: "
                f"Message ID - {message.id}, "
                f"Phone - {phonenumbers},"
                f"CHANGE status - {message.status}"
            )
            self.retry(countdown=600)


    elif mail.date_finish <= dt and message.status == 'Error':
        print('error: sent date < now date')
        message.status = 'Not sent'
        message.save()
        logger.info(
            f"Object: "
            f"Message ID - {message.id}, "
            f"Phone - {phonenumbers},"
            f"CHANGE status - {message.status}"
        )
    else:
        raise self.retry(countdown=600)
