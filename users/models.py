import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    """
    Default custom user model for team_mgm
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    cpf = models.CharField(max_length=100, default="000.000.000-00")
    role = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="000")
    profile_id = models.CharField(max_length=100, default="undefined")
    address = models.CharField(max_length=100, default="")
    expertise = models.CharField(max_length=100, default="", blank=True, null=True)
    experience = models.CharField(max_length=100, default="", blank=True, null=True)