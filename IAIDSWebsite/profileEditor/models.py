from django.db import models
from IAIDSWebsite import settings
from pathlib import Path
from os import remove
from datetime import datetime

from django.contrib.auth.models import User

# Code by Cameron Showalter
# class userModel is modified by original class Player.

class userModel(models.Model):
    def save_usr_pic(self, filename):
        #if file name already exists, remove it before adding new one
        file_name = 'usr-{0}'.format(self.domain_name)
        middle_dir = "person-"+str(user.email)
        dir_to_file = settings.MEDIA_ROOT + middle_dir

        # creates 'middle_dir' if it doesn't exist:
        Path(dir_to_file).mkdir(exist_ok=True)
        file = Path(dir_to_file+'/'+file_name)
        if file.is_file():
            remove(file)
        return '/'.join([middle_dir, file_name])

    domain_name = models.CharField(max_length=45, unique=True)
    email = models.EmailField(max_length=128, unique=True)
    profile_pic = models.ImageField(upload_to=save_usr_pic)
    administrator = models.BooleanField()
    # had to make player_type cascade to delete corectly when game is deleted
    # will make view so that you can switch players to an existing player_type instead
    # player_type = models.ForeignKey('PlayerType', on_delete=models.CASCADE)
    # game = models.ForeignKey('Game', on_delete=models.CASCADE)
    # current_status = models.CharField(max_length=2, default='HU', 
    # 	choices=(('HU', 'Human'), ('ZO','Zombie'),
    # 			 ('CO', 'Corpse'),('NP', 'Spectating'),))

    class Meta:
        verbose_name = "person"
        verbose_name_plural = "People"
        ordering = ['domain_name']

    def __str__(self):
        return self.domain_name