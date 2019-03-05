
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.db import models
from IAIDSWebsite import settings
from pathlib import Path
from os import remove
from datetime import datetime
from IAIDSWebsite.validators import validate_file_size

class MyUserManager(BaseUserManager):
    def create_user(self, email,first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must provide an email address')
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name)

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(
            email,
            password=password,
            first_name = first_name,
            last_name = last_name

        )
        user.is_admin = True
        user.set_password(password)
        user.save(using = self._db)
        return user

class MyUser(AbstractBaseUser):
    def save_usr_pic(self, filename):
        #if file name already exists, remove it before adding new one
        file_name = filename
        dir_to_file = settings.MEDIA_ROOT + '/profileEditor'

        Path(dir_to_file).mkdir(exist_ok=True)
        #file = Path(dir_to_file+'/'+file_name)
        file = models.FileField(upload_to=dir_to_file + '/', verbose_name=file_name, validators=[validate_file_size])
        # if file.is_file():
        #     remove(file)
        return '/'.join(['profileEditor',file_name])

    email = models.EmailField(max_length= 255, unique = True)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)

    date_of_birth = models.DateField(null = True)
    profile_pic = models.ImageField(null = True, upload_to=save_usr_pic, default="thispersondoesnotexist.jpg")
    description = models.CharField(null = True, max_length=250, default="Hi, I'm a volunteer.")

 
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self):
        return self.email
   
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    




