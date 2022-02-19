from django.db import models
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

    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)

    bio = models.TextField(blank=True)  # default or null
    birthdate = models.DateField(blank=True, null=True)

    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

