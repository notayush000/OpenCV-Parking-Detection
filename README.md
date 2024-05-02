
# Car Parking Space Counter using OpenCV in Python

In this project, we have built a parking space counter. We began by selecting the parking spaces. Subsequently, we implemented a system to detect whether a space is occupied or not. This allows us to calculate the number of free spaces available.


## Acknowledgements

In this project, I drew inspiration from the video [Parking Space Counter using OpenCV Python](https://youtu.be/caKnQlCMIYI?si=K2AmxEBPMD_hMQ9G) by [Murtaza's Workshop - Robotics and AI](https://www.youtube.com/@murtazasworkshop) on YouTube.


## Project Highlights

- Identifies parking spaces as empty or occupied in real-time. It updates the counter accordingly.
- Employs basic image processing techniques.


## Installation and Usage

1. Clone this repository
```
https://github.com/notayush000/OpenCV-Parking-Detection.git
```

2. If you want to re-select the parking spaces using different resource then do the following:
    - Get a clear picture of the resource that you have choosen
    - Open `ParkingSpacePicker.py`
    - Put the image name/path here
        ```python
        img = cv2.imread("name/path")
        ```
    - Run `ParkingSpacePicker.py`
        ```python
        python ParkingSpacePicker.py
        ```
    - Now click on the area that you want to select as a parking space
    - If you want to remove an area that you have previously selected then right click on that area

3. Now run `main.py` to check the number of parking space available
```python
python main.py
```

NOTE:

Perform Step 2 only when you change your resource, otherwise it is not required.

