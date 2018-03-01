from django.shortcuts import render
import requests


def index(request):

    main = "http://api.openweathermap.org/data/2.5/weather?q="
    key = "&appid=d2e145db4ed70f0140213da3add513bf"

    if request.method == 'POST':
        city = request.POST.get('q')
        country = request.POST.get('country')
        if country == "lazy":
            url = main + city + key
        else:
            url = main + city + "," + country + key
        res = requests.get(url).json()

        if res['cod'] == 200:
            context = {
                'state': 1,
                'city': res['name'],
                'country': res['sys']['country'],
                'weather': res['weather'][0]['main'],
                'icon': res['weather'][0]['icon'],
                'weatherDes': res['weather'][0]['description'],
                'temp': int(res['main']['temp'] - 273),
                'tempMax': int(res['main']['temp_max'] - 273),
                'tempMin': int(res['main']['temp_min'] - 273),
                'windSpeed': res['wind']['speed'],
                'windAngle': res['wind']['deg']
            }
        else:
            context = {
                'state': -1
            }
    else:
        context = {
            'state': 0
        }
    return render(request, 'home/index.html', context)
