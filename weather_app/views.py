from django.shortcuts import render
import requests
from datetime import datetime, timedelta

# Map small towns to bigger cities for fallback
TOWN_FALLBACKS = {
    'Gampalagudem': 'Krishna',
    'SmallTownExample': 'NearestCity',
    # Add more mappings as needed
}

def home(request):
    city = request.POST.get('city', '').strip()
    
    if not city:
        city = 'Lubbock'
    else:
        # If city is a known small town, use its fallback city
        city = TOWN_FALLBACKS.get(city, city)
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9772b773cbd4bd019b6c3310e734a5ad'
    PARAMETERS = {'units': 'metric'}

    try:
        data = requests.get(url, params=PARAMETERS).json()

        description = data['weather'][0]['description'].title()
        icon = data['weather'][0]['icon']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        utc_time = datetime.utcfromtimestamp(data['dt'])
        timezone_offset = data['timezone']
        local_time = utc_time + timedelta(seconds=timezone_offset)

        return render(request, 'home.html', {
            'city': city,
            'description': description,
            'icon': icon,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'day': local_time.strftime('%A, %d %B %Y - %I:%M %p'),
        })

    except KeyError:
        return render(request, 'home.html', {
            'error_message': 'City or town not found. Please enter a valid name.'
        })
