from django.db import models

from apps.routes.models import Routes
from apps.shapes.models import Shapes

class Trips(models.Model):
    route = models.ForeignKey(Routes, models.DO_NOTHING, blank=True, null=True)
    service_id = models.CharField(max_length=30, blank=True, null=True)
    trip_id = models.CharField(primary_key=True, max_length=20)
    trip_short_name = models.CharField(max_length=50, blank=True, null=True)
    trip_headsign = models.CharField(max_length=100, blank=True, null=True)
    direction_id = models.SmallIntegerField(blank=True, null=True)
    block_id = models.IntegerField(blank=True, null=True)
    shape_id = models.CharField(max_length=20, blank=True, null=True)
    shape_id_serial = models.ForeignKey(Shapes, models.DO_NOTHING, db_column='shape_id_serial', blank=True, null=True)
    bikes_allowed = models.SmallIntegerField(blank=True, null=True)
    wheelchair_accessible = models.SmallIntegerField(blank=True, null=True)
    trip_type = models.IntegerField(blank=True, null=True)
    drt_max_travel_time = models.IntegerField(blank=True, null=True)
    drt_avg_travel_time = models.IntegerField(blank=True, null=True)
    drt_advance_book_min = models.IntegerField(blank=True, null=True)
    drt_pickup_message = models.IntegerField(blank=True, null=True)
    drt_drop_off_message = models.IntegerField(blank=True, null=True)
    continuous_pickup_message = models.CharField(max_length=50, blank=True, null=True)
    continuous_drop_off_message = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trips'
        verbose_name_plural = "trips"

    def __str__(self):
        from apps.stop_times.models import StopTimes

        stop_times = StopTimes.objects.filter(trip = self.trip_id).order_by('stop_sequence')

        return "{} - T{} ({} - {})".format(self.route.route_long_name, self.trip_id[2:8], stop_times[0].departure_time, stop_times.order_by('-stop_sequence')[0].departure_time)
