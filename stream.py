import streamlit as st

# Function to predict weather condition based on inputs
def predict_weather(temp, humidity, wind_speed, pressure):
    if temp > 35 and humidity < 30 and wind_speed < 10:
        return "Hot and Dry"
    elif temp < 20 and humidity > 70 and wind_speed > 15:
        return "Cold and Rainy"
    elif 20 <= temp <= 30 and 40 <= humidity <= 60 and wind_speed < 15:
        return "Pleasant"
    elif wind_speed > 25:
        return "Stormy"
    elif pressure < 1000:
        return "Low Pressure: Possible Rain"
    else:
        return "Uncertain Conditions"

# Streamlit app
st.title("Weather Condition Predictor")

# Input fields for weather parameters
st.header("Enter Weather Parameters")
temp = st.number_input("Temperature (°C)", min_value=-50.0, max_value=60.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=200.0, value=10.0)
pressure = st.number_input("Pressure (hPa)", min_value=800.0, max_value=1200.0, value=1013.0)

# Button to predict weather condition
if st.button("Predict Weather Condition"):
    condition = predict_weather(temp, humidity, wind_speed, pressure)
    st.subheader("Weather Report")
    st.write(f"**Temperature:** {temp}°C")
    st.write(f"**Humidity:** {humidity}%")
    st.write(f"**Wind Speed:** {wind_speed} km/h")
    st.write(f"**Pressure:** {pressure} hPa")
    st.write(f"**Predicted Condition:** {condition}")