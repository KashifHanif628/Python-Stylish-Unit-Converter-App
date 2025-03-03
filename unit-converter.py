import streamlit as st
import time

# Custom CSS for Styling & Animations
st.markdown(
    """
    <style>
    /* Light Mode */
    .light-mode {
        background: linear-gradient(to right, #ff9a9e, #fad0c4);
        color: black;
    }
    
    /* Dark Mode */
    .dark-mode {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }

    /* Title Typing Effect */
    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }
    
    .title-container {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #ff9800;
        white-space: nowrap;
        overflow: hidden;
        border-right: 2px solid white;
        width: 0;
        animation: typing 2.5s steps(30, end) forwards;
    }

    /* Subtitle Styling with Always Visible Color */
    .subtitle {
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        color: #00e676; /* Changed to Green for Visibility */
        margin-bottom: 30px;
        transition: all 0.3s ease-in-out;
    }

    .subtitle:hover {
        color: #ffeb3b;
    }

    /* Input & Button Styling */
    .stSelectbox, .stNumberInput {
        padding: 10px;
        margin-top: 20px;
        margin-bottom: 20px;
        font-size: 18px;
    }

    /* Button Hover Effect */
    .stButton button {
        background-color: #ff9800 !important;
        color: white !important;
        font-size: 18px !important;
        border-radius: 10px !important;
        transition: all 0.3s ease-in-out;
    }
    
    .stButton button:hover {
        background-color: #ff5722 !important;
        transform: scale(1.1);
    }

    /* Result Box */
    .result-box {
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        background: white;
        color: black;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 4px 10px rgba(255, 152, 0, 0.5);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Theme Toggle (Dark / Light Mode)
theme = st.toggle("🌗 Toggle Dark/Light Mode")

# Apply Theme Based on Selection
if theme:
    st.markdown('<div class="dark-mode">', unsafe_allow_html=True)
else:
    st.markdown('<div class="light-mode">', unsafe_allow_html=True)

# Animated Title with Typewriter Effect
st.markdown('<div class="title-container">✨ Unit Converter App ✨</div>', unsafe_allow_html=True)

# Subtitle with Hover Effect
st.markdown('<div class="subtitle">🔢 Convert Length, Weight and Time instantly</div>', unsafe_allow_html=True)

# Category Selection
category = st.selectbox("📏⚖️⏳ Select the category", ["📏 Length", "⚖️ Weight", "⏳ Time"])

# Function for Unit Conversion
def convert_units(category, value, unit):
    if category == "📏 Length":
        if unit == "🌍 Kilometers to Miles":
            return value * 0.621371
        elif unit == "🛣️ Miles to Kilometers":
            return value / 0.621371
        
    elif category == "⚖️ Weight":
        if unit == "🏋️ Kilograms to Pounds":
            return value * 2.20462
        elif unit == "⚖️ Pounds to Kilograms":
            return value / 2.20462
        
    elif category == "⏳ Time":
        if unit == "⏱️ Seconds to Minutes":
            return value / 60
        elif unit == "⏱️ Minutes to Seconds":
            return value * 60
        elif unit == "⏳ Minutes to Hours":
            return value / 60
        elif unit == "⏳ Hours to Minutes":
            return value * 60
        elif unit == "🕰️ Hours to Days":
            return value / 24
        elif unit == "🕰️ Days to Hours":
            return value * 24

# Unit Selection Based on Category
if category == "📏 Length":
    unit = st.selectbox("🔄 Select Conversion", ["🌍 Kilometers to Miles", "🛣️ Miles to Kilometers"])
elif category == "⚖️ Weight":
    unit = st.selectbox("🔄 Select Conversion", ["🏋️ Kilograms to Pounds", "⚖️ Pounds to Kilograms"])
elif category == "⏳ Time":
    unit = st.selectbox("🔄 Select Conversion", ["⏱️ Seconds to Minutes", "⏱️ Minutes to Seconds", "⏳ Minutes to Hours", "⏳ Hours to Minutes", "🕰️ Hours to Days", "🕰️ Days to Hours"])

# Value Input Field
value = st.number_input("🔢 Please Enter the value to convert!")

# Convert Button with Loading Animation
if st.button("✅ Convert"):
    with st.spinner('🔄 Converting... Please wait!'):
        time.sleep(1.5)  # Simulating a delay for animation
        result = convert_units(category, value, unit)
        st.markdown(f'<div class="result-box">🎯 The Converted result is: <b>{result:.2f}</b></div>', unsafe_allow_html=True)

# Close Theme Div
st.markdown('</div>', unsafe_allow_html=True)
