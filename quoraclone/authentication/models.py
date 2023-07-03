from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models
from cloudinary.models import CloudinaryField

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('username', "Fahad1234")
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('age', 23)

        # Create a regular user using the create_user method
        user = self.create_user(email, password, **extra_fields)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    name = models.CharField(max_length=50 , blank=False )
    email = models.EmailField(max_length=30, unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    profile_picture = CloudinaryField('profile_pictures')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    def clean(self):
        super().clean()

        if self.age > 120:
            raise ValidationError("Age cannot be more than 120.")

        if not self.password:
            raise ValidationError("Password is required.")

        if not self.name.isalpha():
            raise ValidationError("Name should only contain alphabetic characters.")

        if not self.username.isalnum():
            raise ValidationError("Username should only contain alphanumeric characters.")
