from django.db import models

class Stops(models.Model):
    stop_id = models.IntegerField(primary_key=True)
    stop_code = models.CharField(max_length=10, blank=True, null=True)
    platform_code = models.CharField(max_length=10, blank=True, null=True)
    stop_name = models.CharField(max_length=255, blank=True, null=True)
    stop_desc = models.CharField(max_length=255, blank=True, null=True)
    stop_lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    stop_lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    zone_id = models.IntegerField(blank=True, null=True)
    stop_url = models.CharField(max_length=50, blank=True, null=True)
    location_type = models.SmallIntegerField(blank=True, null=True)
    parent_station = models.IntegerField(blank=True, null=True)
    stop_timezone = models.CharField(max_length=20, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    direction_id = models.IntegerField(blank=True, null=True)
    wheelchair_boarding = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stops'
        verbose_name_plural = "stops"

    def __str__(self):
        if self.stop_id is None or self.stop_name is None:
            return 'Sem ID'
        
        return str(self.stop_id) + ' - ' + self.stop_name