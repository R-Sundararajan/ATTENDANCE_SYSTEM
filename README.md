# 🎓 Face Recognition Based Smart Attendance System

A smart attendance tracking solution that uses real-time face recognition to mark and manage attendance data securely. It leverages **dlib** for face recognition, **OpenCV** for video capture, **Streamlit** for the user interface, and **SQLite** for local storage. This is ideal for classrooms, labs, or small organizations looking to digitize attendance workflows.

---

## 📌 Features

- 📸 Real-time webcam-based **face recognition**
- 🧍 New user face registration with intelligent detection
- 🧠 128D **facial feature extraction** stored in CSV
- ✅ Automated **attendance marking**
- 📊 Attendance logs stored in **SQLite database**
- 🌐 Web interface built using **Streamlit**
- ⚙️ Uses **dlib wheel** prebuilt for Python 3.11 (included)
- 🤖 Integrates AI-powered face matching and detection pipeline

---
⚙️ Installation
🐍 Python Version
Ensure you're using Python 3.11 (required for the dlib .whl).

🔧 Step-by-Step Setup

# 1. Create virtual environment
python -m venv venv
venv\Scripts\activate          # Windows

# 2. Install dlib manually (wheel included)
pip install ./dlib_whl/dlib-19.24.2-cp311-cp311-win_amd64.whl

# 3. Install other required packages
pip install -r requirements.txt

🚀 How to Run

# Launch the Streamlit app
streamlit run Main_page.py

Navigate using the Streamlit sidebar:

-🧍 New Registration

-🧠 Feature Extraction

-📸 Take Attendance

-📊 View Attendance Log

📦 Data Files
features_all.csv: Facial features from registered users.

attendance.db: SQLite database with name, date, time.

data_faces_from_camera/: Folder with captured user face images.

📜 License  
This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute it, including for commercial purposes.

👨‍💻 Author
Sundararajan R
Project – Smart Attendance System

## 🗂️ Project Structure

```plaintext
Final_year_proj/
├── data/
│   ├── assets/                        # Placeholder for UI/media files
│   ├── data_dlib/                     # dlib model data
│   ├── data_faces_from_camera/       # Captured face images
│   └── features_all.csv              # CSV storing 128D face embeddings
│
├── Details/                          # Additional logs or metadata
│
├── pages/                            # Multi-page Streamlit modules
│   ├── 1_Attendance_taker.py         # Face recognition & attendance logic
│   ├── 2_New_Register.py             # Register a new user with webcam
│   ├── 3_Extraction.py               # Extract embeddings from saved faces
│   └── 4_Database.py                 # View attendance logs in UI
│
├── templates/
│   └── index.html                    # Optional HTML template (for Flask)
│
├── app.py                            # Streamlit app main entry point
├── Main_page.py                      # Landing or control page
├── attendance.db                     # SQLite DB for attendance records
├── index.html                        # Duplicate HTML page (optional)
├── dlib_whl/                         # Folder containing dlib .whl for Windows
│   └── dlib-19.24.2-cp311-cp311-win_amd64.whl
├── README.md                         # You're reading it!





