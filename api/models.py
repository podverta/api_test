from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

import pytz

User = get_user_model()

class Tag(models.Model):
    word = models.CharField(max_length=35)

    def __str__(self):
        return self.word

class Mail(models.Model):

    date_start = models.DateTimeField("дата и время запуска рассылки")
    date_finish = models.DateTimeField("дата и время окончания рассылки")
    text = models.TextField("Текст сообщения", max_length=1000)


class Client(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    phone_number = PhoneNumberField(region='RU')
    code_mobile = models.CharField(max_length=3, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
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
    ]

    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=status_choices, max_length=13)
    id_mail = models.ForeignKey(Mail, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)

class Group(models.Model):
    title = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.title

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    group = models.ForeignKey(Group, on_delete=models.PROTECT,
                              blank=True, null=True, related_name='group_posts')
    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created = models.DateTimeField("Дата добавления", auto_now_add=True, db_index=True)

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='user')
    following = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='following',)

