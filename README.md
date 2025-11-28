# 🌤️ My Weather App

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A beautiful and user-friendly weather application built with Python and Tkinter. Get real-time weather information and forecasts for any city worldwide!

## 📸 Preview

![Weather App Screenshot](weather_app_demo.png) _(Add your screenshot here)_

## ✨ Features

- **Real-Time Weather**: Current temperature, humidity, pressure, wind speed, and description
- **5-Day Forecast**: Daily weather predictions with icons
- **Timezone & Location**: Accurate time zones and coordinates for any city
- **Intuitive GUI**: Sleek interface with weather-themed icons and colors
- **Global Coverage**: Works for cities worldwide using geocoding

## 🛠 Installation

### Prerequisites

- Python 3.7 or higher
- Internet connection for API calls

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/darshansavani18/my-weather.git
   cd my-weather
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Get your OpenWeatherMap API Key:**
   - Sign up at [OpenWeatherMap](https://openweathermap.org/api)
   - Get your free API key
   - Replace the `api_key` variable in `weather.py` with your key:
     ```python
     api_key = "YOUR_API_KEY_HERE"
     ```

## 🚀 Usage

1. **Run the application:**

   ```bash
   python weather.py
   ```

2. **Enter a city name** in the search bar and click the search button

3. **View weather details:**
   - Current weather data on the left
   - 5-day forecast at the bottom

## 📦 Dependencies

The application uses the following Python libraries:

- `geopy` - For geocoding city names to coordinates
- `requests` - To fetch weather data from OpenWeatherMap API
- `pytz` - For timezone handling
- `timezonefinder` - To determine timezone from coordinates
- `Pillow` (PIL) - For image processing and displaying weather icons
- `tkinter` - Standard GUI library (comes with Python)

Full list in `requirements.txt`.

## 🔧 How It Works

1. **Location Lookup**: Uses Nominatim (via geopy) to find latitude/longitude for the entered city
2. **Timezone Detection**: Determines local timezone using TimezoneFinder
3. **Weather Data**: Fetches weather forecast from OpenWeatherMap API (5-day, 3-hour intervals)
4. **Data Extraction**:
   - Current weather from the first API result
   - 5-day forecast by filtering for 12:00 PM entries
5. **GUI Display**: Updates Tkinter widgets with weather data and icons

## 📁 Project Structure

```
my-weather/
├── weather.py              # Main application script
├── requirements.txt        # Python dependencies
├── icon/                   # Weather condition icons (36 files)
│   ├── 01d.jpeg           # Clear sky day
│   ├── 02n.jpeg           # Few clouds night
│   └── ...                # More weather icons
├── 14.png                 # Search bar image
├── 15.jpeg                # UI box image
├── 16.jpeg                # UI box image
├── 17.jpeg                # Round box image
├── 18.jpg                 # App icon
├── 19.png                 # Weather image
├── 20.png                 # Search button image
└── README.md              # This file
```

## 🐛 Troubleshooting

- **API Key Issues**: Ensure your OpenWeatherMap API key is valid and has weather forecast access
- **Geocoding Errors**: Check internet connection and verify city name spelling
- **Missing Images**: Ensure all image files (14.png, 15.jpeg, etc.) and icon folder are present

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- Icons from OpenWeatherMap's free icon set
- UI inspiration from various desktop weather applications

---

**Made with ❤️ by [Darshan Savani](https://github.com/darshansavani18)**
