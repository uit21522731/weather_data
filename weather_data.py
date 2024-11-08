from flask import Flask, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# Helper function to generate a random cardinal wind direction
def random_wind_direction():
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    return random.choice(directions)

# Function to generate detailed weather data for a region
def generate_weather_data(region_name):
    # Set regional temperature ranges
    temperature_range = {
        "North": (15, 30),
        "Central": (18, 35),
        "South": (20, 40)
    }
    temp_min, temp_max = temperature_range.get(region_name, (20, 35))

    # Generate random values for weather attributes
    return {
        "region": region_name,
        "temperature": round(random.uniform(temp_min, temp_max), 1),
        "humidity": random.randint(50, 90),
        "wind_speed": round(random.uniform(5, 30), 1),
        "wind_direction": random_wind_direction(),
        "precipitation": round(random.uniform(0, 50), 1),
        "air_pressure": round(random.uniform(1000, 1025), 1),
        "visibility": round(random.uniform(5, 20), 1),  # in kilometers
        "cloud_cover": random.randint(0, 100),
        "uv_index": random.randint(0, 10),
        "status": random.choice(["sunny", "cloudy", "overcast", "rainy", "stormy"]),
        "timestamp": datetime.now().isoformat()  # ISO formatted timestamp
    }

# Route to get detailed weather data for all regions
@app.route('/api/weather', methods=['GET'])
def get_weather():
    # Generate weather data for each region
    regions = ["North", "Central", "South"]
    weather_data = [generate_weather_data(region) for region in regions]
    
    # Return JSON response
    return jsonify({"weather_data": weather_data})

if __name__ == '__main__':
    app.run(debug=True)