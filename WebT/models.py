from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    ip_address = models.GenericIPAddressField()
    port = models.DecimalField(max_digits=6, decimal_places=0)
    place = models.CharField(max_length=250)
    max_temperature = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    min_temperature = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    in_range = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensors')
    amount = models.DecimalField(max_digits=11, decimal_places=4)
    datetime = models.DateTimeField()