import argparse
import numpy as np
import cv2


def main(args):
    network = cv2.dnn.readNetFromCaffe('network/MobileNetSSD_deploy.prototxt.txt', 'network/MobileNetSSD_deploy.caffemodel')

    CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
        "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
        "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
        "sofa", "train", "tvmonitor"]
    COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

    img = cv2.imread(args.image)

    # Preprocessing of the frame
    cv_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    frame = img
    frame_resized = cv2.resize(frame, (300, 300))

    # Get high and width of the real frame
    (h, w) = frame.shape[:2]

    # Get a blob which is our input image after mean substraction, normalizing and channel swapping
    blob = cv2.dnn.blobFromImage(frame_resized,0.007843, (300, 300), 127.5)

    # Pass the blob through the network and obtain the detections and predictions
    network.setInput(blob)
    detections = network.forward()
    
    area_biggest_detection = 0

    # Loop over all the detections in a same frame
    for i in np.arange(0, detections.shape[2]):
        object_type = detections[0,0,i,1]
        confidence = detections[0, 0, i, 2]
        if object_type == 15 and confidence > 0.2: # If has detected a human and it has a confidence > 20% --> HUMAN DETECTED

            person_detected = 1
            # Get the (x, y) coordinates of the bounding box
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # Get bounding box center and area used for commanding the TurtleBot to follow a person
            center_box = int((startX+endX)/2)
            area_box = (endX-startX)*(endY-startY)
            
            # Draw the box and the intruder label in the frame 
            label = "{}: {:.2f}%".format('intruder',confidence * 100)
            cv2.rectangle(frame, (startX, startY), (endX, endY),[0,0,255], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(frame, label, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, [0,0,255], 2)

            # If there are more than 1 human get the position of the closest (biggest area)
            if area_box > area_biggest_detection: 
                area_biggest_detection = area_box
                center_biggest_detection = center_box


    cv2.imshow("Image window", frame)
    cv2.waitKey(0)


if __name__ == '__main__':
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-i", "--image", type=str, default='images/im1.jpg', help="path to Image File ")
    args = arg_parse.parse_args()
    main(args)