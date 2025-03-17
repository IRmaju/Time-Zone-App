import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of available time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# App Title
st.title("Two Time Zone Converter")

# Select two time zones
st.subheader("Select Two Time Zones")
timezone1 = st.selectbox("Select First Timezone", TIME_ZONES, index=1)
timezone2 = st.selectbox("Select Second Timezone", TIME_ZONES, index=2)

# Display current time in selected time zones
st.subheader("Current Time in Selected Timezones")
current_time1 = datetime.now(ZoneInfo(timezone1)).strftime("%Y-%m-%d %I:%M:%S %p")
current_time2 = datetime.now(ZoneInfo(timezone2)).strftime("%Y-%m-%d %I:%M:%S %p")

st.write(f"**{timezone1}**: {current_time1}")
st.write(f"**{timezone2}**: {current_time2}")

# Time Conversion Section
st.subheader("Convert Time Between Selected Timezones")
input_time = st.time_input("Select Time to Convert", value=datetime.now().time())

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), input_time, tzinfo=ZoneInfo(timezone1))
    converted_time = dt.astimezone(ZoneInfo(timezone2)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"Converted Time in {timezone2}: {converted_time}")
