from django.contrib import admin
from keijiban.models import Tweet
# Register your models here.
from keijiban.models import Tweet, ID

admin.site.register(Tweet)
admin.site.register(ID)
