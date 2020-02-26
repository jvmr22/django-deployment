from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    #copy all the generic columns of User (admin) model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    '''
    Again it is necessary to set "on_delete" parameter. Always that I have
    a constraint, this is necessary

    '''
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
