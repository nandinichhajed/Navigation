from sqlite3 import Time
from django.db import models

# Create your models here.

class Mytable(models.Model):
    ID = models.IntegerField(db_column="ID") #name of column of existing db
    Course_Over_Ground = models.CharField(db_column="Course_Over_Ground")
    Latitude = models.CharField(db_column="Latitude")
    Longitude = models.CharField(db_column="Longitude")
    Ship_ID = models.IntegerField(db_column="Ship_ID")
    Speed = models.IntegerField(db_column="Speed")
    Time = models.TimeField(db_column="Time")
    
    class Meta:
        db_table = "mytable"
    
    
    def __str__(self):
        return self.ID