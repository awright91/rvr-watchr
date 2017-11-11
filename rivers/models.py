from django.db import models

# Create your models here.


class River(models.Model):
    name = models.CharField(max_length = 250)
    section = models.CharField(max_length = 250, default=' ')
    description = models.TextField()
    current_level = models.FloatField()
    measurement = models.CharField(max_length=10)
    state = models.ForeignKey('locations.State', null=True, blank=True, related_name="river")
    url = models.CharField(max_length=250, default = ' ')
    image = models.ImageField(upload_to="static/img", default="/img/rapids.jpg")

    def __str__(self):
        return self.name

    def renderLevel(self):
        if self.measurement == 'cfs':
            current_string = str(self.current_level)
            new_current_level = current_string[:-2]
            return "{} {}".format(new_current_level, self.measurement)
        return "{} {}".format(self.current_level, self.measurement)

    def summary(self):
        return self.description[:200] + '...'
