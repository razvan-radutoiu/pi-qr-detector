# Raspberry Pi QR Code Detector: Detecting Malicious QR Codes

## Overview

This repository contains code for a Raspberry Pi-based QR code detector designed to identify potentially malicious QR codes in real-time. The program utilizes the Raspberry Pi's camera module to capture video, OpenCV for QR code detection and decoding, and the Google Safe Browsing API for malicious content verification. The system responds to the analysis results by controlling GPIO pins, illuminating LEDs to indicate the safety status (green for safe, red for malicious). Additionally, the video feed is displayed with QR code detection overlaid.

## Features

- Real-time QR code detection using the Raspberry Pi camera module
- QR code decoding with OpenCV
- Integration with the Google Safe Browsing API for malicious content verification
- GPIO pin control for LED illumination based on the QR code analysis results
- Live video feed display with overlaid QR code detection

## Getting Started

Follow these steps to set up the Raspberry Pi QR Code Detector on your system:

1. **Prerequisites:**
   - Ensure you have a Raspberry Pi with the camera module.
   - Install the required dependencies, including OpenCV.

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/razvan-radutoiu/qr-code-detector.git
   ```

3. **Configuration:**
   - Configure the Google Safe Browsing API key in the QR.py file.

4. **Run the Program:**
   ```bash
   cd qr-code-detector
   python qr_code_detector.py
   ```

5. **Interpret LED Status:**
   - Green LED: Indicates a safe QR code.
   - Red LED: Indicates a potentially malicious QR code.

## Dependencies

- OpenCV
- Google Safe Browsing API

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Follow the [Contribution Guidelines](CONTRIBUTING.md) for more information.

## Acknowledgments

- The project relies on the excellent [OpenCV library](https://opencv.org/).
- Google Safe Browsing API for malicious content detection.


---
