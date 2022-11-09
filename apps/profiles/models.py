from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from apps.common.models import TimeStampedUUIDModel
from django.core.validators import RegexValidator


User = get_user_model()


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _('Other')
    


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    about_me = models.TextField(verbose_name=_("About Me"), default="say something about yourself")
    license = models.CharField(verbose_name=_("Real Estate License"), max_length=20, blank=True, null=True)
    profile_photo = models.ImageField(verbose_name=_("Profile Photo"), default="/profile_default.png")
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, default=Gender.OTHER, max_length=20)
    country = CountryField(verbose_name=_("Country"), default="IN", blank=False, null=False)
    city = models.CharField(verbose_name=_("City"), max_length=180, default="Bangalore", blank=False, null=False)
    is_buyer = models.BooleanField(verbose_name=_("Buyer"), default=False, help_text=_("Are you looking to buy a property?"))
    is_seller = models  .BooleanField(verbose_name=_("Seller"), default=False, help_text=_("Are you looking to sell a property?"))
    is_agent = models.BooleanField(verbose_name=_("Agent"), default=False, help_text=_("Are you an agent?"))
    top_agent = models.BooleanField(verbose_name=_("Top Agent"), default=False)
    ratings= models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(verbose_name=_("Number of reviews"), default=0, null=True, blank=True)


    def __str__(self):
        return f"{self.user.username}'s profile"




# Create your models here.
