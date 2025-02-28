import streamlit as st

# Set page config with minimal settings
st.set_page_config(
    page_title="Retro Chat",
    page_icon="🕹️",
    layout="wide"
)

# Basic inline styling
st.markdown("""
<style>
body {
    background-color: #120458;
    color: #ffffff;
}
h1 {
    color: #ff00c1;
    text-shadow: 0 0 5px #ff00c1;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Simple content
st.title("RETRO CHAT")
st.write("Loading app...")

if st.button("Click to continue"):
    st.success("Button clicked successfully!")
    st.write("If you see this message, your app is working correctly.")
    
    # Once this minimal version works, you can redirect to your full app
    st.info("Now you can replace this file with your full application code.")
