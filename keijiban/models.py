from django.db import models

# Create your models here.


class Tweet(models.Model):
    twidata = models.TextField('tweet',default='NOTHING')
    twilink = models.CharField('link',max_length=500,default = 'NOTHING')
    twiurl = models.CharField('url',max_length=500,default = 'NOTHING')
    #twiid = models.CharField('yes',max_length=25)
    def __str__(self):
        return self.twidata


class ID(models.Model):
    USERID = models.CharField('id',max_length=500,default = 'NOTHING')
    def __str__(self):
        return self.USERID