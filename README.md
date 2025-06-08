# 🌦️ Weather Website

This is a simple weather forecast web application built using **Django** and the **OpenWeatherMap API**. Users can enter a city name to view the current weather, including temperature, weather condition, humidity, wind speed, and a photo representing the location.

## 🌐 Live Features

- Displays current weather based on user input  
- Default city weather shown on load  
- Dynamic city images using Unsplash API (or equivalent)  
- Error handling for unknown city names

---

## 🚀 Demo

> 🖼️ Enter a city name like `London`, `New York`, or `Hyderabad` and get the current weather instantly.

![Weather App Screenshot](screenshot.png)  
<sub>*Include a screenshot of your app here*</sub>

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap  
- **Backend**: Django (Python)  
- **API**: [OpenWeatherMap](https://openweathermap.org/api)  
- **Others**: Requests library, Datetime module

---

## 📦 Installation

### Prerequisites

- Python 3.10 or higher  
- pip (Python package manager)  
- Virtual environment (optional but recommended)

### Steps

```bash
# Clone the repository
git clone https://github.com/Tarunkumarreddyyaramala/Weather-website.git
cd Weather-website

# Create and activate virtual environment (optional)
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the server
python manage.py runserver

```

Then open your browser and go to:
👉 http://127.0.0.1:8000

## 🔑 API Setup

You’ll need an API key from OpenWeatherMap to fetch weather data.

Sign up and get your free API key.

In your Django project settings or views, set the API key as an environment variable or add it in a secure way like using python-decouple.

Example using python-decouple in settings.py:

```bash
# from decouple import config
WEATHER_API_KEY = config('WEATHER_API_KEY')

# Then in your .env file:
WEATHER_API_KEY=your_api_key_here

```

## 📁 Project Structure

```bush 
Weather-website/
│
├── weather/                # Django app
│   ├── templates/
│   │   └── weather.html    # Main frontend page
│   ├── static/             # Static files (CSS, images)
│   └── views.py            # Weather view logic
│
├── WeatherWebsite/         # Project configuration
│   └── settings.py         # Django settings
│
├── manage.py               # Django entry point
├── requirements.txt        # Dependencies
└── README.md               # This file

```
## 🧑‍💻 Author
Tarun Kumar Reddy Yaramala

Check out the [🔗 GitHub](https://github.com/Tarunkumarreddyyaramala/)

## 📄 License
This repository is open source and available under the MIT License.

## Happy Coding!
😄 Thanks! Happy coding to you too! 💻✨

If you need help with anything—code, docs, deployment—I'm here. 🚀

Now go build something awesome! 🛠️💡





