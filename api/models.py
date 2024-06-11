from django.db import models


class Rate(models.Model):
    Curr_ID = models.IntegerField()
    Date = models.DateTimeField()
    Cur_Abbreviation = models.CharField(max_length=3)
    Cur_Scale = models.SmallIntegerField()
    Cur_name = models.CharField(max_length=50)
    Cur_OfficialRate = models.FloatField()

    class Meta:
        db_table = 'rate'
        verbose_name = 'rate'
        verbose_name_plural = 'rates'
