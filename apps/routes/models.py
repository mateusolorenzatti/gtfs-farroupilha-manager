from django.db import models

from apps.agency.models import Agency

class Routes(models.Model):
    agency = models.ForeignKey(Agency, models.DO_NOTHING, blank=True, null=True)
    route_id = models.IntegerField(primary_key=True)
    route_short_name = models.CharField(max_length=50, blank=True, null=True)
    route_long_name = models.CharField(max_length=255, blank=True, null=True)
    route_desc = models.CharField(max_length=255, blank=True, null=True)
    route_type = models.SmallIntegerField(blank=True, null=True)
    route_url = models.CharField(max_length=50, blank=True, null=True)
    route_color = models.CharField(max_length=11, blank=True, null=True)
    route_text_color = models.CharField(max_length=11, blank=True, null=True)
    route_sort_order = models.IntegerField(blank=True, null=True)
    min_headway_minutes = models.IntegerField(blank=True, null=True)
    eligibility_restricted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'routes'
        verbose_name_plural = "routes"

    def __str__(self):
        return str(self.route_id) + ' - ' + self.route_long_name