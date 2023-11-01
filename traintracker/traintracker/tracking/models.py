from django.db import models

class GPSTracker(models.Model):
    tracker_id = models.CharField(max_length=50, unique=True)
    lat = models.FloatField()
    lng = models.FloatField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.tracker_id
