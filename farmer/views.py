from django.shortcuts import render
from .models import FarmerData
from django.contrib.auth.decorators import login_required


crop_data = {
"Rice":{
"temp_min":20,
"temp_max":35,
"rain_min":200,
"rain_max":400,
"soil":["Clay","Loamy"],
"season":"Kharif"
},

"Wheat":{
"temp_min":10,
"temp_max":25,
"rain_min":50,
"rain_max":100,
"soil":["Loamy","Black"],
"season":"Rabi"
},

"Cotton":{
"temp_min":25,
"temp_max":35,
"rain_min":100,
"rain_max":200,
"soil":["Black"],
"season":"Kharif"
}
}

@login_required
def dashboard(request):
    return render(request,"dashboard.html")


def recommend_crop(temp, rain, soil, season):

    best_crop = None
    best_score = 0

    for crop, data in crop_data.items():

        score = 0

        if data["temp_min"] <= temp <= data["temp_max"]:
            score += 30

        if data["rain_min"] <= rain <= data["rain_max"]:
            score += 30

        if soil in data["soil"]:
            score += 20

        if season == data["season"]:
            score += 20

        if score > best_score:
            best_score = score
            best_crop = crop

    return best_crop


def home(request):

    if request.method == "POST":

        soil = request.POST["soil"]
        temp = float(request.POST["temperature"])
        rain = float(request.POST["rainfall"])
        season = request.POST["season"]

        crop = recommend_crop(temp, rain, soil, season)

        FarmerData.objects.create(
            soil=soil,
            temperature=temp,
            rainfall=rain,
            season=season,
            recommended_crop=crop
        )

        return render(request,"recommendation_result.html",{
    "crop":crop,
    "soil":soil,
    "season":season,
    "rain":rain,
    "temp":temp
})

    return render(request,"crop_form.html")