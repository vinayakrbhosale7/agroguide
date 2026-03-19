from django.shortcuts import redirect, render
from .models import FarmerData, FertilizerRecommendation
from django.contrib.auth.decorators import login_required
crop_data = {

"Rice":{
"temp_min":20,"temp_max":35,
"rain_min":200,"rain_max":400,
"soil":["Clay","Loamy","Alluvial"],
"season":"Kharif"
},

"Wheat":{
"temp_min":10,"temp_max":25,
"rain_min":50,"rain_max":100,
"soil":["Loamy","Black","Alluvial"],
"season":"Rabi"
},

"Cotton":{
"temp_min":25,"temp_max":35,
"rain_min":100,"rain_max":200,
"soil":["Black","Alluvial"],
"season":"Kharif"
},

"Sugarcane":{
"temp_min":20,"temp_max":35,
"rain_min":150,"rain_max":300,
"soil":["Loamy","Black","Alluvial"],
"season":"Annual"
},

"Maize":{
"temp_min":18,"temp_max":30,
"rain_min":50,"rain_max":150,
"soil":["Loamy","Alluvial"],
"season":"Kharif"
},

"Bajra":{
"temp_min":25,"temp_max":40,
"rain_min":40,"rain_max":100,
"soil":["Sandy","Loamy"],
"season":"Kharif"
},

"Jowar":{
"temp_min":25,"temp_max":35,
"rain_min":50,"rain_max":100,
"soil":["Black","Loamy"],
"season":"Kharif"
},

"Barley":{
"temp_min":12,"temp_max":25,
"rain_min":40,"rain_max":100,
"soil":["Loamy","Alluvial"],
"season":"Rabi"
},

"Soybean":{
"temp_min":20,"temp_max":30,
"rain_min":60,"rain_max":120,
"soil":["Black","Loamy"],
"season":"Kharif"
},

"Groundnut":{
"temp_min":20,"temp_max":30,
"rain_min":50,"rain_max":100,
"soil":["Sandy","Loamy"],
"season":"Kharif"
},

"Mustard":{
"temp_min":10,"temp_max":25,
"rain_min":25,"rain_max":75,
"soil":["Loamy","Alluvial"],
"season":"Rabi"
},

"Chickpea":{
"temp_min":20,"temp_max":30,
"rain_min":30,"rain_max":60,
"soil":["Sandy","Loamy"],
"season":"Rabi"
},

"Lentil":{
"temp_min":15,"temp_max":25,
"rain_min":30,"rain_max":60,
"soil":["Loamy","Alluvial"],
"season":"Rabi"
},

"Tea":{
"temp_min":18,"temp_max":30,
"rain_min":150,"rain_max":300,
"soil":["Loamy","Acidic"],
"season":"Annual"
},

"Coffee":{
"temp_min":15,"temp_max":28,
"rain_min":150,"rain_max":250,
"soil":["Loamy","Acidic"],
"season":"Annual"
},

"Tomato":{
"temp_min":18,"temp_max":30,
"rain_min":50,"rain_max":100,
"soil":["Loamy","Sandy"],
"season":"Zaid"
},

"Potato":{
"temp_min":15,"temp_max":25,
"rain_min":40,"rain_max":80,
"soil":["Loamy","Sandy"],
"season":"Rabi"
},

"Onion":{
"temp_min":13,"temp_max":30,
"rain_min":30,"rain_max":70,
"soil":["Loamy","Sandy"],
"season":"Rabi"
},

"Watermelon":{
"temp_min":22,"temp_max":35,
"rain_min":40,"rain_max":80,
"soil":["Sandy","Loamy"],
"season":"Zaid"
},

"Cucumber":{
"temp_min":20,"temp_max":30,
"rain_min":40,"rain_max":80,
"soil":["Loamy","Sandy"],
"season":"Zaid"
}

}


def dashboard(request):
    return render(request,"dashboard.html")

@login_required
def before_recommendation(request):
    return render(request,"before_recommendation.html")

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


from .models import FarmerData
from django.contrib.auth.decorators import login_required

@login_required
def history(request):
    crop_data = FarmerData.objects.all().order_by('-created_at')
    fertilizer_data = FertilizerRecommendation.objects.all().order_by('-created_at')

    print("CROP:", crop_data)
    print("FERT:", fertilizer_data)

    return render(request, "history.html", {
        "data": crop_data,
        "fdata": fertilizer_data
    })



def about(request):
    return render(request,"about.html")

def delete_history(request, id):
    if request.method == "POST":
        try:
            record = FarmerData.objects.get(id=id)
            record.delete()
        except FarmerData.DoesNotExist:
            pass
    return redirect("history")

def delete_fhistory(request, id):
    if request.method == "POST":
        try:
            record = FertilizerRecommendation.objects.get(id=id)
            record.delete()
        except FertilizerRecommendation.DoesNotExist:
            pass
    return redirect("history")


# Fertilizer base data
fertilizer_data = {
    "Rice": "Urea + DAP",
    "Wheat": "NPK 12-32-16",
    "Cotton": "NPK 20-20-20",
    "Sugarcane": "Urea + Potash",
    "Maize": "NPK 20-10-10",
    "Bajra": "Urea + SSP",
    "Jowar": "NPK 18-46-0",
    "Barley": "NPK 10-26-26",
    "Soybean": "DAP + Potash",
    "Groundnut": "Gypsum + SSP",
    "Mustard": "NPK 12-32-16",
    "Chickpea": "DAP",
    "Lentil": "NPK 10-20-20",
    "Tea": "Ammonium Sulphate",
    "Coffee": "NPK 17-17-17",
    "Tomato": "NPK 19-19-19",
    "Potato": "NPK 12-32-16",
    "Onion": "NPK 10-26-26",
    "Watermelon": "NPK 20-20-20",
    "Cucumber": "NPK 19-19-19"
}

@login_required
def fertilizer_view(request):

    if request.method == "POST":
        crop = request.POST['crop']
        soil = request.POST['soil']
        n = int(request.POST['nitrogen'])
        p = int(request.POST['phosphorus'])
        k = int(request.POST['potassium'])

        # Base fertilizer
        base = fertilizer_data.get(crop, "General NPK")

        # Logic
        if n < 50:
            result = base + " + Add Urea"
        elif p < 50:
            result = base + " + Add DAP"
        elif k < 50:
            result = base + " + Add MOP"
        else:
            result = base

        # Soil improvement
        if soil == "Sandy":
            result += " + Organic Compost"
        elif soil == "Clay":
            result += " + Gypsum"

        # Save to DB
        FertilizerRecommendation.objects.create(
            crop=crop,
            soil=soil,
            nitrogen=n,
            phosphorus=p,
            potassium=k,
            recommendation=result
        )

        # ✅ 👉 SHOW RESULT PAGE HERE
        return render(request, "fertilizer_result.html", {
            "crop": crop,
            "soil": soil,
            "n": n,
            "p": p,
            "k": k,
            "result": result
        })

    # 👉 First time open
    return render(request, "fertilizer.html")

