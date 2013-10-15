import  pytz
from django.db import models
from django.contrib.auth.models import User
from timezone_field import TimeZoneField
from django.utils import timezone
import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    time_zone = TimeZoneField()
    wake_up_time = models.TimeField()
    prev_login_time = models.DateTimeField()

    def __unicode__(self):
        return self.user.username

    def get_curr_quote_id(self):
        return 1

class Quote(models.Model):
    quote = models.TextField()
    meta_data = models.TextField(blank=True, null=True) # This field is optional.

    def __unicode__(self):
        return self.quote

class Log(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    quote = models.ForeignKey(Quote)
    wake_up_date = models.DateTimeField()

    def __unicode__(self):
        return self.user_profile.user.first_name + " " + self.wake_up_date.__str__()
