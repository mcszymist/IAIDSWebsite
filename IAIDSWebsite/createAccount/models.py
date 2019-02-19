
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.db import models
from IAIDSWebsite import settings
from pathlib import Path
from os import remove
from datetime import datetime

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must provide an email address')
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            date_of_birth = date_of_birth

        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, password, date_of_birth, first_name, last_name):
        user = self.create_user(
            email,
            password=password,
            date_of_birth = date_of_birth,
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

        # creates 'middle_dir' if it doesn't exist:
        Path(dir_to_file).mkdir(exist_ok=True)
        file = Path(dir_to_file+'/'+file_name)
        if file.is_file():
            remove(file)
        return '/'.join(['profileEditor',file_name])

    email = models.EmailField(max_length= 255, unique = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    date_of_birth = models.DateField()
    profile_pic = models.ImageField(upload_to=save_usr_pic, default="thispersondoesnotexist.jpg")
    domain_name = models.CharField(max_length=45, unique=True, default="IAIDS")
 
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'first_name', 'last_name']
    
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
        ordering = ['domain_name']

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
    def __str__(self):
        return self.domain_name




