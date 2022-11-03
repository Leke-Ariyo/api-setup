from django.db import models
from django.conf import settings

#for userprofile
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

#for custom userprofile manage
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""
    
    def create_user(self, id, name, password=None):
        """create a new user profile"""
        user = self.model(id=id, name=name)
        user.set_password(password)

        #best practice to use (using=self.db)
        user.save(using=self._db)

        return user


    def create_superuser(self, name, password):
        """create a new superuser with given details"""
        user = self.create_user(name, password)

        #automatically created by PermissionsMixin
        user.is_superuser = True

        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    name = models.CharField(max_length=255,unique=True)
    id = models.IntegerField(unique=True, primary_key=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    #overwrite default username to use email, so that Admin portal will display email and password
    #instad of username and password
    #also mark email as required or mandatory field
    USERNAME_FIELD = 'name'

    #explicitly declare fields which are required
    REQUIRED_FIELDS =['id']

    def get_full_name(self):
        """retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """retrieve short name of user"""
        return self.name

    def __str__(self):
        """return string representation of user"""
        return self.name


