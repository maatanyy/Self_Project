import uuid
import email
import os
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    """Custom User Model"""  

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    GRADE_1 = "1"
    GRADE_2 = "2"
    GRADE_3 = "3"
    GRADE_4 = "4"

    GRADE_CHOICES = ((GRADE_1, "GRADE_1"), (GRADE_2, "GRADE_2"), (GRADE_3, "GRADE_3"), (GRADE_4, "GRADE_4"))

    avatar = models.ImageField(
        upload_to="avatars", blank=True
    )  # null은 database에서 blank는 form에서

    grade = models.CharField(choices=GRADE_CHOICES, max_length=10, blank=True)

    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    
    bio = models.TextField(blank=True)  # default or null
    birthdate = models.DateField(blank=True, null=True)
    influencer = models.BooleanField(default=False)

    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

    def verify_email(self):
        if self.email_verified is False:   
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            ) 
            send_mail(
                ("Verify Airbnb Account"),
                strip_tags(html_message),    
                settings.EMAIL_FROM, 
                [self.email], 
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return

