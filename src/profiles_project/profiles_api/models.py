from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """helps django work with custom user model"""

    def create_user(self,email,name,password=None):

        """create a new user profile object"""

        if not email:
            raise ValueError('User must have an Email Address')

        email=self.normalize_email(email)

        #create a new user profile object
        user=self.model(email=email,name=name)
        user.set_password(password)

        user.save(using=self._db)
        return user


    def create_superuser(self,email,name,password):
        """ create and save a superuser with given details"""

        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Represent a UserProfile in our system"""

    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)

    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=["name"]

    def get_full_name(Self):
        return self.name
    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
