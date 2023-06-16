from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Normalize the email address by lowercasing the domain part of it
        email = self.normalize_email(email)

        # Create a new instance of the CustomUser model
        user = self.model(email=email, **extra_fields)

        # Set the password for the user
        user.set_password(password)

        # Save the user to the database
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        def create_superuser(self, email, password=None, **extra_fields):
            # Set the extra fields for the superuser
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)

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
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.username
