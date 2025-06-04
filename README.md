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
