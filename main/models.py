from django.db import models

class Story(models.Model):
    username = models.CharField('Nickname', max_length=25)
    email = models.CharField('Email-address', max_length=50)
    product = models.CharField('Products', max_length=30)
    date = models.DateTimeField('Date')

    def get_absolute_url(self):
        return f'/{self.id}'

    def __str__(self):
        return self.username
class Exists(models.Model):
    name = models.CharField('Product-name', max_length=30)
    price = models.IntegerField('Price')
    company = models.CharField('Company', max_length=30)

    def get_absolute_url(self):
        return f'/exists/{self.id}'

    def __str__(self):
        return self.name
