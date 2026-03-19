from django.db import models

class FarmerData(models.Model):

    soil = models.CharField(max_length=50)
    temperature = models.FloatField()
    rainfall = models.FloatField()
    season = models.CharField(max_length=20)

    recommended_crop = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recommended_crop
    

from django.db import models


class FertilizerRecommendation(models.Model):
    crop = models.CharField(max_length=100)
    soil = models.CharField(max_length=50)

    nitrogen = models.IntegerField()
    phosphorus = models.IntegerField()
    potassium = models.IntegerField()

    recommendation = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.crop}"