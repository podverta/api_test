from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q


from .models import Mail, Client, Message
from .tasks import send_api
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@receiver(post_save, sender=Mail)
def create_mail(sender, instance, created, **kwargs):
    if created:
        mailer = Mail.objects.filter(id=instance.id).get()
        clients = Client.objects.filter(Q(code_mobile=mailer.code_mobile) |
                                        Q(tags=mailer.tags)).all()
        for client in clients:
            mail_id = mailer.id
            client_id = client.id
            Message.objects.create(status='Ready',
                                   id_mail_id=mail_id,
                                   id_client_id=client_id)

            logger.info(
                f"Create the object Message for: "
                f"Mail ID - {mail_id},"
                f"Client ID - {client_id},"
                f"with status - 'Ready'"
            )
            send_api.apply_async((client_id, mail_id))
