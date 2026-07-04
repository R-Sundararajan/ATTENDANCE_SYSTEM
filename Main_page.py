import streamlit as st
import base64
st.set_page_config(page_title="Face recognition attendance system", page_icon="🔒")

# Render the image and heading using flexbox (aligned to the left, moved up)
st.markdown(
    f"""
    <div style="display: flex; align-items: center; margin-left: -120px; margin-top: -60px;"> <!-- Move content up -->
        <h1 style="margin: 0; padding-left: 10px; white-space: nowrap;">FACE RECOGNITION BASED ATTENDANCE SYSTEM</h1>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("""
## 📌 Features

""")

st.markdown(
    f"""
    <div style="display: flex; align-items: center;font-size:20px; margin-left: 110px; margin-top: 20px;">

- 📸 Real-time webcam-based **Multi-Face Recognition**  
- 🧍 New user **Face Registration**  
- 🧠 128-D **Facial feature extraction** stored in CSV  
- ✅ Automated **Attendance System**  
- 📊 Attendance Logs are Stored in **SQLite database**  
- 🌐 Web interface built using **Streamlit**  
- ⚙️ Uses **dlib Wheel** Built for Python 3.11
    </div>
    """,
    unsafe_allow_html=True
)

# Hide the Deploy button, header, and footer using CSS
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}  /* Hide the menu */
        footer {visibility: hidden;}      /* Hide the footer */
        header {visibility: hidden;}      /* Hide the header */
    </style>
    """,
    unsafe_allow_html=True
)
