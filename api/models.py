from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

import pytz


class Mail(models.Model):

    date_start = models.DateTimeField("дата и время запуска рассылки")
    date_finish = models.DateTimeField('дата и время окончания рассылки')
    tags = models.CharField(max_length=35, blank=True,)
    code_mobile = models.CharField('код оператора',
                                     max_length=3,
                                     blank=True)
    text = models.TextField("Текст сообщения", max_length=1000)

    def save(self, *args, **kwargs):
        if self.tags == "":
            self.tags = "empty"
        return super(Mail, self).save(*args, **kwargs)

class Client(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    phone_number = PhoneNumberField(region='RU')
    code_mobile = models.CharField('код оператора', max_length=3, blank=True)
    tags = models.CharField(max_length=35, blank=True)
    time_zone = models.CharField(max_length=32, choices=TIMEZONES,
                                 default='UTC')

    def save(self, *args, **kwargs):
        self.code_mobile = str(self.phone_number)[2:5]
        return super(Client, self).save(*args, **kwargs)

class Message(models.Model):
    status_choices = [
        ('Sent', 'Sent'),
        ('Error', 'Error'),
        ('Ready', 'Ready'),
        ('Not sent', 'Not sent'),
    ]

    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=status_choices, max_length=13)
    id_mail = models.ForeignKey(Mail, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)


