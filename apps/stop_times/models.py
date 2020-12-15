from django.db import models

from apps.trips.models import Trips
from apps.stops.models import Stops

class StopTimes(models.Model):
    trip = models.ForeignKey(Trips, models.DO_NOTHING)
    arrival_time = models.CharField(max_length=8, blank=True, null=True)
    departure_time = models.CharField(max_length=8, blank=True, null=True)
    stop = models.ForeignKey(Stops, models.DO_NOTHING)
    stop_sequence = models.IntegerField(primary_key=True)
    stop_headsign = models.CharField(max_length=20, blank=True, null=True)
    pickup_type = models.SmallIntegerField(blank=True, null=True)
    drop_off_type = models.SmallIntegerField(blank=True, null=True)
    shape_dist_traveled = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    timepoint = models.SmallIntegerField(blank=True, null=True)
    start_service_area_id = models.CharField(max_length=11, blank=True, null=True)
    end_service_area_id = models.CharField(max_length=11, blank=True, null=True)
    start_service_area_radius = models.CharField(max_length=11, blank=True, null=True)
    end_service_area_radius = models.CharField(max_length=11, blank=True, null=True)
    continuous_pickup = models.CharField(max_length=11, blank=True, null=True)
    continuous_drop_off = models.CharField(max_length=11, blank=True, null=True)
    pickup_area_id = models.CharField(max_length=11, blank=True, null=True)
    drop_off_area_id = models.CharField(max_length=11, blank=True, null=True)
    pickup_service_area_radius = models.CharField(max_length=11, blank=True, null=True)
    drop_off_service_area_radius = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stop_times'
        verbose_name_plural = "stop_times"
        unique_together = (('trip', 'stop', 'stop_sequence'),)
    
    def __str__(self):
        return 'S'+ str(self.stop) + 'T' + str(self.trip)[2:8] + ' (' + str(self.arrival_time) + ')'