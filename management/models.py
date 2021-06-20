from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class products(models.Model):
    product_name = models.CharField(max_length=25, verbose_name="Product Name", unique=True)

    def __str__(self):
        return '{}'.format(self.product_name)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class locations(models.Model):
    location_name = models.CharField(max_length=25,verbose_name='Location',unique=True)


    def __str__(self):
        return '{}'.format(self.location_name)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'


class movements(models.Model):
    product = models.ForeignKey(to='products',on_delete=models.CASCADE)
    location_from = models.ForeignKey(to='locations',on_delete=CASCADE,related_name="location_from",blank=True)
    location_to = models.ForeignKey(to='locations',on_delete=CASCADE,related_name="location_to")
    quantity = models.IntegerField()
    time = models.TimeField(auto_now=True)


    def __str__(self):
        return '{}'.format(self.product)

    class Meta:
        verbose_name = 'Movement'
        verbose_name_plural = 'Movements'