import imp
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.


@admin.register(models.User)  # admin에 ueser을 등록하기 위해서 추가함
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (  
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "grade",
                    "gender",
                    "bio",
                    "birthdate",
                    "influencer",
                    "email_verified",
                    "email_secret",
                )
            },
        ),
    )

    list_filter = ("influencer",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "grade",
        "gender",
        "birthdate",
        "email_verified",
    )


   

