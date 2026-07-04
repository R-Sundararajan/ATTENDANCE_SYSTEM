# Face Recognition Based Smart Attendance System

## Overview

This repository contains a local face-recognition attendance system built with Python. It provides a Streamlit-based application flow for registering faces, generating face encodings, taking attendance from a webcam, and viewing attendance data stored in SQLite.

At a high level, users register face images through a camera interface, convert those images into 128-dimensional dlib face descriptors, and then run the attendance taker. During attendance, the webcam feed is checked against the saved descriptors, and recognized names are recorded with the current date and time.

## Features

- Streamlit home page and multipage navigation.
- Webcam-based face registration using OpenCV, dlib, Tkinter, and Pillow.
- Registered face images saved under `data/data_faces_from_camera/`.
- Face descriptor extraction into `data/features_all.csv`.
- Mean 128D face descriptor generation for each registered person.
- Real-time attendance recognition from the default webcam.
- SQLite attendance storage in `attendance.db`.
- Duplicate attendance prevention for the same name on the same date.
- Date-based attendance viewing through a Flask page at `http://127.0.0.1:5000`.

## Technologies Used

### Programming Languages

- Python
- HTML
- CSS

### Computer Vision Libraries

- OpenCV (`opencv-python`)
- Pillow

### Machine Learning / Face Recognition Libraries

- dlib
- face_recognition_resnet_models
- NumPy

### Database Technologies

- SQLite

### Web Frameworks

- Streamlit
- Flask

### Frontend Technologies

- HTML templates
- CSS
- Bootstrap CDN in the Flask attendance template

### Supporting Libraries

- pandas
- csv, datetime, logging, os, shutil, time, tkinter, and sqlite3 from the Python standard library

## Project Structure

```text
Face-Recognition-Based-Smart-Attendance-System/
|-- Main_page.py          # Main Streamlit entry page
|-- app.py                # Flask attendance viewer
|-- pages/                # Streamlit pages for attendance, registration, extraction, and database link
|-- templates/            # Flask HTML template
|-- data/
|   |-- data_dlib/        # dlib face recognition and landmark model files
|   |-- data_faces_from_camera/ # Captured registered face images
|   `-- features_all.csv  # Saved face descriptors
|-- Details/              # Additional repository assets
|-- attendance.db         # SQLite attendance database
|-- requirements.txt      # Python dependencies
`-- dlib-19.24.1-cp311-cp311-win_amd64.whl # Included Windows dlib wheel for Python 3.11
```

## Setup

Use Python 3.11 if you plan to install the included Windows dlib wheel.

```bash
python -m venv venv311
venv311\Scripts\activate
pip install .\dlib-19.24.1-cp311-cp311-win_amd64.whl
pip install -r requirements.txt
```

The application expects the dlib model files to exist in `data/data_dlib/` and uses the default webcam through OpenCV.

## Running the Application

Start the Streamlit application:

```bash
streamlit run Main_page.py
```

For the date-based attendance table, start the Flask app in a separate terminal:

```bash
python app.py
```

Then open `http://127.0.0.1:5000` or use the Streamlit database page link.

## System Workflow

1. Face registration: the registration page opens a Tkinter camera window, accepts a name, creates a folder for that person, and saves cropped face images.
2. Face encoding generation: the extraction page reads saved face images, computes dlib 128D face descriptors, averages each person's descriptors, and writes them to `data/features_all.csv`.
3. Recognition process: the attendance page loads `features_all.csv`, detects faces from the webcam, computes descriptors for detected faces, and compares them with saved descriptors using Euclidean distance.
4. Attendance recording: when a face is recognized, the system inserts the name, current time, and current date into the `attendance` table in SQLite. The code checks existing records to avoid marking the same person more than once per date.

## Repository Insights

- `Main_page.py` defines the Streamlit landing page and lists the main application capabilities.
- `pages/2_New_Register.py` handles webcam registration, folder creation, face image capture, and clearing previously saved face data.
- `pages/3_Extraction.py` converts registered face images into `data/features_all.csv`.
- `pages/1_Attendance_taker.py` loads known descriptors, performs webcam recognition, and records attendance in SQLite.
- `pages/4_Database.py` provides a Streamlit link to the local Flask attendance viewer.
- `app.py` serves a Flask form for selecting a date and reading matching attendance records from `attendance.db`.
- `templates/index.html` renders the date picker and attendance table for the Flask view.

## Screenshots and Images

The repository includes `Details/day 1.png`, which can be placed after the Overview section if it represents the application UI or attendance output. The registered face images under `data/data_faces_from_camera/` should not be used as README screenshots unless the subjects have approved their use.

`Demo/` Contains Useful screenshots of the Streamlit home page, the registration camera window and the Flask attendance table.

