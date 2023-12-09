import cv2
import numpy as np
from deep_sort import DeepSort
from yolov5 import YoloV5

def main():
  # Initialize the YOLOv5 and Deep SORT models.
  yolov5 = YoloV5()
  deep_sort = DeepSort()

  # Open the video file.
  video_file = "video.mp4"
  cap = cv2.VideoCapture(video_file)

  # Initialize the people counter.
  people_counter = 0

  # Loop over the video frames.
  while cap.isOpened():
    ret, frame = cap.read()

    # Detect people in the frame.
    detections = yolov5.detect(frame)

    # Track the people in the frame.
    track_ids = deep_sort.track(detections)

    # Count the number of people in the frame.
    people_count = len(np.unique(track_ids))

    # Update the people counter.
    people_counter += people_count

    # Display the number of people in the frame.
    cv2.putText(frame, f"People: {people_count}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the bounding boxes around the people.
    for detection in detections:
      bbox = detection["bbox"]
      cv2.rectangle(frame, bbox, (0, 255, 0), 2)

    # Display the video frame.
    cv2.imshow("Frame", frame)

    # Press `q` to quit.
    key = cv2.waitKey(1)
    if key == ord("q"):
      break

  # Close the video file.
  cap.release()

  # Print the final people count.
  print("Total people:", people_counter)

if __name__ == "__main__":
  main()
