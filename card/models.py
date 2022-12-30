from django.db import models
from django.contrib.auth.models import AbstractUser


SEX_CHOICES = [
    ('M', 'M'),
    ('F', 'F')
]


class Profile(AbstractUser):
    sex = models.CharField(max_length=4, default=SEX_CHOICES[1], choices=SEX_CHOICES, db_index=True, verbose_name='Пол')

    class Meta(AbstractUser.Meta):
        pass


class Card(models.Model):
    status_choices = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Prosrochena', 'Prosrochena')
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='cards')
    series = models.PositiveSmallIntegerField(verbose_name='серия')
    number = models.BigIntegerField(verbose_name='номер')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создана')
    ended_at = models.DateTimeField(verbose_name='срок истекает')
    status = models.CharField(max_length=20, default=status_choices[0], choices=status_choices, verbose_name='статус')

    class Meta:
        ordering = ('profile',)
        verbose_name = 'karta'
        verbose_name_plural = 'karti'

    def __str__(self):
        return f'{self.series} {self.number}'


