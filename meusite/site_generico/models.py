from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.core.validators import MaxValueValidator, MinValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=32)
    letter = models.CharField(max_length=1)

    def __str__(self):
        return self.letter + " - " + self.name

class Sex(models.Model):
    name = models.CharField(max_length=32)
    letter = models.CharField(max_length=1)

    def __str__(self):
        return self.letter + " - " + self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    value = models.DecimalField(max_digits=11, decimal_places=2)
    description = models.TextField(null=True)
    sex = models.ForeignKey('Sex', on_delete=models.CASCADE)

    def __str__(self):
        return self.sex.letter + ' - ' + self.name


class ProductTag(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)

    def __str__(self):
        return self.tag.name + " - " + self.product.name

class Stock(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name + " - " +\
               self.color.name + " - " + self.size.name


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='user_data')
    created = models.DateTimeField(editable=False, default=timezone.now)

    # Personal data
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    ddd = models.CharField(max_length=3, null=True, default=None)
    mobile = models.CharField(max_length=18, null=True, default=None)
    birthday = models.DateField(null=True, default=None)

    # Address
    address_city = models.CharField(max_length=50, null=True, default=None)
    address_district = models.CharField(max_length=50, null=True, default=None)
    address_street = models.CharField(max_length=320, null=True, default=None)
    address_state = models.CharField(max_length=10, null=True, default=None)
    address_number = models.CharField(max_length=15, null=True, default=None)
    address_extra = models.CharField(max_length=35, null=True, default=None)
    address_cep = models.CharField(max_length=8, null=True, default=None)

    def __str__(self):
        return self.name

class PaymentStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    payment_day = models.DateTimeField(default=None, blank=True, null=True)
    payment_method = models.ForeignKey('PaymentMethod',
                                       on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=11, decimal_places=2)
    created = models.DateTimeField(editable=False, default=timezone.now)
    status = models.ForeignKey('PaymentStatus',
                               on_delete=models.CASCADE,
                               default=None,
                               blank=True, null=True)

    def __str__(self):
        return self.created.strftime("%d-%m-%Y") + " - " +\
               self.client.user + " - " +\
               self.status.name

class InvoiceProduct(models.Model):
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.invoice.status.name + " - " +\
               self.product.name + " - " + str(quantity)

class Rating(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    value = models.IntegerField(
        default=5,
        validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return self.product.name + " - " + str(self.profile.pk)
