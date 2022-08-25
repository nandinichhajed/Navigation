from django.db import models

# Create your models here.

class Mytable(models.Model):
    id = models.IntegerField(db_column="id", primary_key=True) #name of column of existing db
    Course_Over_Ground = models.CharField(db_column="course_over_ground", max_length=200)
    Latitude = models.CharField(db_column="latitude", max_length=200)
    Longitude = models.CharField(db_column="longitude", max_length=200)
    Ship_ID = models.IntegerField(db_column="ship_id")
    Speed = models.IntegerField(db_column="speed")
    Time = models.TimeField(db_column="time")
    
    class Meta:
        db_table = "mytable"
    
    
    def __str__(self):
        return self.id