from django import forms
from .models import User
from cloudinary.forms import CloudinaryFileField

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    profile_picture = CloudinaryFileField(required=False)

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'age', 'gender', 'password1', 'password2', 'profile_picture']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password1")
        user.set_password(password)
        if commit:
            user.save()
        profile_picture = self.cleaned_data.get("profile_picture")
        if profile_picture:
            user.profile_picture = profile_picture
            user.save() 
        return user    
    
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)    
    