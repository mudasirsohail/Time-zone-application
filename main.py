# Here we imported the required libraries
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of available time zones
TIME_ZONES = [
        "UTC",
    "Asia/Karachi",  
    "Australia/Sydney",  
    "America/New_York",  
    "Europe/London",  
    "Asia/Tokyo",  
    "Asia/Dubai",  
    "Europe/Paris",  
    "America/Los_Angeles",  
    "Asia/Shanghai",  
    "Europe/Berlin",  
    "Africa/Cairo",  
    "America/Chicago",  
    "Asia/Kolkata",  
    "Pacific/Auckland",  
    "Europe/Moscow",  
    "America/Toronto",  
    "Asia/Singapore",  
    "America/Mexico_City",  
    "Africa/Johannesburg",  
    "America/São_Paulo",  
    "Asia/Seoul",  
    "Europe/Madrid",  
    "Asia/Jakarta",  
    "Europe/Rome",  
    "America/Denver",  
    "Asia/Bangkok",  
    "America/Vancouver",  
    "Asia/Hong_Kong",  
    "Europe/Amsterdam",  
    "Australia/Melbourne"  
]

# app title
st.title("Time Zone App")

#Here We Create a multi-select dropdown for choosing differnt time zones
selected_timezone = st.multiselect(
    "Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

# Display current time for selected time zones
st.subheader("Selected Timezones")
for tz in selected_timezone:
    # Get and format current time for each selected timezone with AM/PM
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    # Display timezone and its current time
    st.write(f"**{tz}**: {current_time}")

# Create section for time conversion
st.subheader("Convert Time Between Timezones")
# Create time input field with current time as default
current_time = st.time_input("Current Time", value=datetime.now().time())
# Dropdown to select source timezone
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
# Dropdown to select target timezone
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# Create convert button and handle conversion
if st.button("Convert Time"):
    # Combine today's date with input time and source timezone
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    # Convert time to target timezone and format it with AM/PM
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    # Display the converted time with success message
    st.success(f"Converted Time in {to_tz}: {converted_time}")

st.write("--------------------------")
st.write("Made with ❤️ by [Mudasir Sohail](https://github.com/mudasirsohail) ")