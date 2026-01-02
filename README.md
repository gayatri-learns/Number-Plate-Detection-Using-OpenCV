# Number-Plate-Detection-Using-OpenCV
This project detects a vehicle’s number plate from an image using OpenCV and applies a background blur effect while keeping the number plate region clear. It demonstrates practical computer vision techniques such as edge detection, contour analysis, ROI extraction, and image masking.

🎯 What This Project Does
Reads a car image
Detects edges using Canny Edge Detection
Finds contours and approximates rectangular shapes
Identifies the number plate region (ROI)
Blurs the background while keeping the number plate visible
Displays both detected number plate and final processed image

❓ Why This Project Exists
Automatic Number Plate Detection is widely used in:
Traffic monitoring systems
Smart parking solutions
Toll booths
Surveillance and security applications
This project was built to understand classical computer vision techniques before moving to deep learning–based approaches.

🧠 What Problems It Solves
Locates number plates without deep learning
Demonstrates how to isolate and process specific regions in an image
Shows how masking and image blending work in real-world scenarios
Provides a lightweight solution without heavy models

🛠️ Technologies Used
Python
OpenCV
NumPy

🖼️ Output
Detected number plate displayed separately
Final image with blurred background and clear number plate

⚠️ Known Limitations
Works best on clear images with visible rectangular number plates
Struggles with:
Low-light images
Extreme angles
Multiple vehicles in one frame
Does not perform OCR (text recognition)
Image-based only (no video support)
These limitations are intentional to focus on classical OpenCV techniques.
