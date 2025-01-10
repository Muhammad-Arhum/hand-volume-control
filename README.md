# Hand Gesture Volume Control Using MediaPipe and PyCaw

This project utilizes MediaPipe, OpenCV, and PyCaw to create a hand gesture-based volume control system. The system uses a webcam to capture real-time video feed, processes hand landmarks to detect the distance between the thumb and index finger, and adjusts the system's volume accordingly. Here's a detailed breakdown:
# 1. Hand Landmark Detection:

    MediaPipe is used to detect hand landmarks in real-time.
    The position of key landmarks on the hand (specifically the thumb tip and index finger tip) is tracked.
    The distance between the thumb tip (landmark 4) and index finger tip (landmark 8) is continuously calculated. This distance will serve as the input for controlling the system's volume.

# 2. Volume Control Logic:

    The distance between the thumb and index finger is normalized to a scale between 0 and 100, representing the volume range.
    The maximum and minimum distances are tracked, and the current distance is adjusted based on these extremes to ensure smooth volume control.
    The calculated distance is mapped to a volume level using PyCaw, a Python library that provides access to the audio settings of the system.
    The volume is updated in real-time as the distance between the thumb and index finger changes.

# 3. User Interface:

    Hand landmarks are drawn on the video feed using OpenCV to visually track the position of the thumb and index finger.
    The volume level is displayed on the top-left corner of the window in real-time, allowing the user to see the current volume.

# 4. Key Features:

    Real-time video feed with hand gesture tracking.
    Volume control mapped to the distance between thumb and index finger.
    Live feedback on the current volume level displayed on the window.
    Min-Max normalization ensures that the distance between thumb and index provides a consistent range of volume control, regardless of hand size or distance from the camera.

# 5. Libraries Used:

    OpenCV for capturing and displaying the video feed.
    MediaPipe for detecting and processing hand landmarks.
    PyCaw for controlling the system's audio volume.
    Math library for calculating the Euclidean distance between the thumb and index finger tips.

# How It Works:

    The webcam captures the user's hand movements.
    MediaPipe detects hand landmarks and calculates the distance between the thumb and index fingers.
    The distance is normalized to determine the volume level.
    PyCaw adjusts the system volume based on the calculated distance.
    The updated volume level is displayed on the screen, along with hand landmarks.

# User Interaction:

    Hand gestures: The user controls the volume by changing the distance between their thumb and index finger.
    The system continuously monitors the hand position and adjusts the volume accordingly.
    The user can quit the application by pressing the Escape key.

# Applications:

    Gesture-based control systems for volume adjustment.
    Accessible control for users with mobility challenges.
    Interactive systems for home automation, gaming, or virtual meetings.

This project is a practical demonstration of integrating computer vision and audio control, offering a novel and intuitive method for controlling system settings through hand gestures.