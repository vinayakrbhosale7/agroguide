from django.db import models

from django.db import models
from django.contrib.auth.models import User

class FarmerData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   # ✅ ADD THIS

    soil = models.CharField(max_length=50)
    temperature = models.FloatField()
    rainfall = models.FloatField()
    season = models.CharField(max_length=20)

    recommended_crop = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recommended_crop


class FertilizerRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   # ✅ ADD THIS

    crop = models.CharField(max_length=100)
    soil = models.CharField(max_length=50)

    nitrogen = models.IntegerField()
    phosphorus = models.IntegerField()
    potassium = models.IntegerField()

    recommendation = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.crop

from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.rating}⭐"


class CropData(models.Model):
    name = models.CharField(max_length=50)
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    rain_min = models.FloatField()
    rain_max = models.FloatField()
    soil = models.CharField(max_length=100)
    season = models.CharField(max_length=20)

    class Meta:
        db_table = "crop_data"   # 👈 connect to this SQL table

class FertilizerData(models.Model):
    crop = models.CharField(max_length=50)
    base_fertilizer = models.CharField(max_length=100)

    class Meta:
        db_table = "fertilizer_data"   # connect SQL table

    def __str__(self):
        return self.crop