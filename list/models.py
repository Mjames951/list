from django.conf import settings
from django.db import models
from django.utils import timezone

class Member(models.Model):
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    email = models.CharField(max_length = 50)
    phone = models.CharField(max_length=20)
    LOW = 'L'
    MID = 'M'
    HIGH = 'H'
    tier_choices = [
        (LOW, 'Low'),
        (MID, 'Mid'),
        (HIGH, 'High'),
    ]
    membership_tier = models.CharField(
        max_length=1,
        choices=tier_choices,
        default=LOW
    )
    home_address = models.CharField(max_length=100)
    EMAIL = 'EM'
    PHONECALL = 'PC'
    TEXT = 'TX'
    LETTER = 'LR'
    contact_choices = [
        (EMAIL, 'Email'),
        (PHONECALL, 'Phone'),
        (TEXT, 'Text'),
        (LETTER, 'Letter'),
    ]
    preferred_mode_of_contact = models.CharField(
        max_length=2,
        choices=contact_choices,
        default=EMAIL
    )

    def __str__(self):
        return self.Lname
    


# Create your models here.
