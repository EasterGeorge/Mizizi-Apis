from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(blank=True, max_length=25)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    phoneNumber = models.CharField(blank=True, max_length=25)
    paymentMethod = models.CharField(blank=True, max_length=100)
    

    def __str__(self):
        return self.email

#'name', 'email', 'phoneNumber', 'password','paymentMethod'

class FirstAidProcedure(models.Model):
    title = models.CharField(blank=True, max_length=25)
    category = models.CharField(blank=True, max_length=50)
    text = models.CharField(blank=True, max_length=250)
    image = models.ImageField(upload_to='media/', default='https://homepages.cae.wisc.edu/~ece533/images/airplane.png')

    def __str__(self):
        return self.title

class MiziziUser(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    paymentMethod = models.CharField(max_length=50)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return self.name