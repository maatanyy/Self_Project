from django import forms
from . import models
from django.contrib.auth import password_validation


class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))  

    def clean(self):   
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data  
            else:
                self.add_error("password", forms.ValidationError("Password is wrong")) 
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist")) 


class SignUpForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email",)

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': "Name"}),
            'last_name': forms.TextInput(attrs={'placeholder': "Id"}),   #last_name을 ID처럼 쓸꺼임, abstactuser에 새로운 항을 만들수도있음
            'email': forms.EmailInput(attrs={'placeholder': "Email"}),
        }

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Password"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Confirm Password"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError(
                "That email is already taken", code="existing_user"
            )
        except models.User.DoesNotExist:
            return email
    
    def clean_username(self):
        username = self.cleaned_data.get("last_name")
        try:
            models.User.objects.get(username=username)
            raise forms.ValidationError(
                "That id is already taken", code="existing_user"
            )
        except models.User.DoesNotExist:
            return username
            
    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.first_name = first_name
        user.username = last_name 
        user.email = email
        user.set_password(password)
        user.save()

    def _post_clean(self):
        super()._post_clean()

        password = self.cleaned_data.get("password1")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error("password1", error) 