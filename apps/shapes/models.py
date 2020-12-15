from django.db import models

class Shapes(models.Model):
    shape_id_serial = models.AutoField(primary_key=True)
    shape_id = models.CharField(max_length=50)
    shape_pt_lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    shape_pt_lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    shape_pt_sequence = models.IntegerField(blank=True, null=True)
    shape_dist_traveled = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shapes'
        unique_together = (('shape_id_serial', 'shape_id'),)
        verbose_name_plural = "shapes"

    def __str__(self):
        return str(self.shape_id) + ' - ' + str(self.shape_pt_sequence)
