import streamlit as st
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        # Extract relevant information
        city_name = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        
        return {
            "city": city_name,
            "temperature": temperature,
            "description": weather_description,
            "humidity": humidity
        }
    else:
        return None

# Streamlit app
st.title("Weather App")
st.write("Get the current weather for Karachi")

# Replace 'YOUR_API_KEY' with your actual API key
api_key = "4281008c6ac34658169dfa78d73218d5"
city = "Karachi"

if st.button("Get Weather"):
    weather_data = get_weather(city, api_key)
    
    if weather_data:
        st.write(f"City: {weather_data['city']}")
        st.write(f"Temperature: {weather_data['temperature']}°C")
        st.write(f"Weather: {weather_data['description']}")
        st.write(f"Humidity: {weather_data['humidity']}%")
    else:
        st.error("Failed to retrieve data from the weather service.")
