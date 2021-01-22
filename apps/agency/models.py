from django.db import models

class Agency(models.Model):
    agency_id = models.IntegerField(primary_key=True)
    agency_url = models.CharField(max_length=255, blank=True, null=True)
    agency_lang = models.CharField(max_length=10, blank=True, null=True)
    agency_name = models.CharField(max_length=255, blank=True, null=True)
    agency_phone = models.CharField(max_length=50, blank=True, null=True)
    agency_timezone = models.CharField(max_length=50, blank=True, null=True)
    agency_fare_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agency'
        verbose_name_plural = "agencies"

    def __str__(self):
        return str(self.agency_id)