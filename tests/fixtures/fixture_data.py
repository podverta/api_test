import pytest
from datetime import datetime, timedelta



@pytest.fixture
def client_1():
    from api.models import Client
    return Client.objects.create(phone_number='+79998887766',
                                 code_mobile='999',
                                 tags='just',
                                 time_zone='Europe/Amsterdam'
                                 )


@pytest.fixture
def mail_1():
    from api.models import Mail
    return Mail.objects.create(date_start=datetime.now() - timedelta(hours=9),
                               date_finish=datetime.now() + timedelta(hours=9),
                               tags='just',
                               code_mobile='Europe/Amsterdam',
                               text='123',
                               )



@pytest.fixture
def message_1(mail_1, client_1):
    from api.models import Message
    return Message.objects.create(date=datetime.now(),
                                   status='Ready',
                                   id_mail=mail_1.id,
                                   id_client = client_1.id
                                   )
