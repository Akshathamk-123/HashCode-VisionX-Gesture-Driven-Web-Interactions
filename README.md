# Elite_Force_HashCode
This is a Project that was done as a part of a 24-hour-Hackathon called Hashcode.
## Project Name: **VisionX: Gesture-Driven Web Interactions**

VisionX is a cutting-edge web application that integrates various computer vision and gesture recognition features. By leveraging technologies such as OpenCV, MediaPipe, and Flask, VisionX provides a seamless and intuitive user experience for text input, mouse control, and system operations through hand and eye gestures.

## Features

1. **Virtual Keyboard**:
   - Type using hand gestures.
   - Detects hand landmarks to simulate key presses.
   - Supports space and backspace functionalities.

2. **Eye-Controlled Mouse**:
   - Control mouse cursor using eye movements.
   - Click functionality through eye gestures.

3. **Hand Gesture Control**:
   - Navigate and interact with the system using hand gestures.
   - Adjust volume and brightness.
   - Scroll vertically and horizontally.

## Technologies Used

- **Flask**: Web framework for building the application.
- **OpenCV**: Computer vision library for image processing.
- **MediaPipe**: Framework for building multimodal machine learning pipelines.
- **CVZone**: High-level library for computer vision tasks.
- **Pynput**: Library for controlling and monitoring input devices.
- **PyAutoGUI**: Library for programmatically controlling the mouse and keyboard.
- **Screen Brightness Control**: Library for controlling screen brightness.
- **PyCaw**: Library for controlling system audio.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/visionx.git
   cd visionx
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Open a web browser and navigate to:

   ```
   http://127.0.0.1:5000/
   ```

## Usage

### Virtual Keyboard

- Launch the application and navigate to the main page.
- Use hand gestures to type on the virtual keyboard displayed on the screen.

### Eye-Controlled Mouse

- Run `app_mouse.py` to enable eye-controlled mouse functionality.
- Use eye movements to control the mouse cursor and perform clicks.

### Hand Gesture Control

- Run `app_mouse_hand.py` to enable hand gesture control.
- Use predefined hand gestures to perform various system operations such as adjusting volume, brightness, and scrolling.

## File Structure

```plaintext
visionx/
├── app.py                # Main Flask application for virtual keyboard
├── app_mouse.py          # Script for eye-controlled mouse
├── app_mouse_hand.py     # Script for hand gesture control
├── templates/
│   └── index_1.html      # HTML template for the web interface
├── static/
│   └── css/
│       └── styles.css    # CSS styles for the web interface
├── requirements.txt      # List of required Python packages
└── README.md             # ReadMe file for the project
```

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Thanks to the developers of OpenCV, MediaPipe, CVZone, and other libraries for their incredible work.

---

For any issues or feature requests, please open an issue. We appreciate your feedback and contributions!

---

Enjoy using VisionX!

## Certificate of Participation
![image](https://github.com/Akshathamk-123/Elite_Force_HashCode/assets/92522733/25ec49cc-5f7c-43d3-ae75-a6d55dfc5bf5)
