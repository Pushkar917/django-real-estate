import email
from email import message
import imp
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUIDModel
from django.core.validators import RegexValidator


class Enquiry(TimeStampedUUIDModel):
    name = models.CharField(_('Your Name'), max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    email = models.EmailField(_("Email"))
    subject = models.CharField(_('Subject'), max_length=100)
    message = models.TextField(_('Message'))

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Enquiries"