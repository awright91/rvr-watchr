from django.db import models
from rivers.models import River
from django.contrib.auth.models import User


# Create your models here.


class RiverSubscription(models.Model):

    user = models.ForeignKey(User, blank=True)
    river = models.ForeignKey(River)
    trigger_level = models.FloatField()


    def __str__(self):
        return self.user.username

    def RenderTriggerLevel(self):
        if self.river.measurement == 'cfs':
            current_string = str(self.trigger_level)
            new_current_level = current_string[:-2]
            return "{} {}".format(new_current_level, self.river.measurement)
        return "{} {}".format(self.trigger_level, self.river.measurement)
