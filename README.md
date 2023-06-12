# Raspberry Pi QR Code Detector: Detecting Malicious QR Codes


This code implements a Raspberry Pi-based QR code detector. It captures video using the Pi's camera module and uses OpenCV to detect and decode QR codes in real-time. The decoded data is then checked against the Google Safe Browsing API to determine if it is potentially malicious. Depending on the result, it controls GPIO pins to light up corresponding LEDs (green for safe and red for malicious). The program also displays the video feed with QR code detection overlaid.
