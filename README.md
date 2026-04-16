# FreeWeatherAPICompare
Comparison of various free weather APIs

## Overview

**FreeWeatherAPICompare** is a web app for comparing hourly weather forecasts from multiple free weather APIs and models, side-by-side and overlaid on a single chart. It helps you visually analyze differences in temperature and precipitation predictions for any location, with a focus on clarity, speed, and customization.

### Features
- Compare up to 12+ free weather APIs/models (OpenWeatherMap, WeatherAPI.com, Open-Meteo, wttr.in, NOAA/NWS, etc.)
- Unified time axis (from 4 hours ago to 72 hours ahead)
- Combined chart overlays all selected models for direct comparison
- Individual charts for each model
- Precipitation accumulation bars (color-matched to model)
- Smart caching (10-minute TTL, avoids unnecessary API calls)
- 10 color themes (5 dark, 5 light) with instant toggle
- Responsive UI, touch-friendly, pull-to-refresh
- Thin progress bar during API refresh
- Day/night shading and midnight lines
- Version tracking and localStorage persistence

## How to Use

### 1. Prerequisites
- Python 3.x (for the simple local server)
- Node.js is **not required**
- No API keys are required for most models (WeatherAPI.com key is optional for extra data)

### 2. Start the App
1. Open a terminal in the `FreeWeatherAPICompare` folder.
2. Run the server:
   - On Windows: Double-click `start_server.bat` **or**
   - Run: `python server.py`
3. Open your browser and go to: [http://localhost:8009](http://localhost:8009)

### 3. Using the App
- Enter a location (city name or ZIP code) and click **Fetch Forecasts**
- Use the toggle buttons to select which models/APIs to display
- View:
  - **Individual charts**: Each model in its own panel
  - **Combined chart**: All selected models overlaid, with legend and precipitation bars
- Change color theme with the palette button (top right)
- Pull down on mobile/touch to refresh all data
- Progress bar at top shows when APIs are being refreshed
- Version and last update info in the footer

### 4. Notes
- Data is cached for 10 minutes per location to reduce API usage
- OpenWeatherMap is limited to 3 days (72 points)
- WeatherAPI.com may require a free API key (see `config.js`)
- All code is vanilla JS/HTML/CSS, no frameworks

## Screenshots

_Add screenshots here if desired._

## License
MIT
