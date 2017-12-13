import matplotlib.image as mpimg
import visualizer
from classifier import Classifier
import os
import cv2
from skvideo.io import VideoWriter
import imageio
import numpy as np
import speed_detection
import heatmap
from tracking import Tracking
from debugger import Debugger
from bounding_box import BoundingBox

image_size = (1280,720)
num_examples = 8500
hm_threshold = 0

# Train classifier
# svm = Classifier(num_examples)
# svm.train()

# See test images
# for image_name in os.listdir('test_images/'):
#     if image_name[0] == '.':
#         continue
#     image = cv2.imread('test_images/'+image_name)
#     image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#
#     classified_image, bounding_boxes = svm.classify(image)
#     visualizer.draw_image(classified_image)

    # classified_image2 = svm.find_cars(image)
    # visualizer.draw_image(classified_image2)


    # cluster_img = heatmap.cluster_bounding_boxes(image,bounding_boxes,0)
    # visualizer.draw_image(cluster_img)
    #
    # visualizer.draw_image(classified_image)



    # speed_image = svm.find_cars(image)
    #
    # visualizer.draw_image(speed_image)
# See video

#
# writer1 = VideoWriter('tracking_full.mp4',frameSize=image_size,fps=4)
# writer1.open()
# writer2 = VideoWriter('output_video_fast.mp4',frameSize=image_size,fps=20)
# writer2.open()

debug = Debugger()
detected_boxes = []
time_range = range(0,1250)
# for i in time_range:
#     if i%100 ==0:
#         print(i)
#     # tracker.prediction()
#     image = vid.get_data(i)
#     prediction = visualizer.draw_tracking(image,tracker)
#     # visualizer.draw_image(prediction)
#     # print(np.max(image))
#     result1,bboxes = svm.classify(image)
#     # visualizer.draw_image(result1)
#     bboxes = heatmap.cluster_bounding_boxes(image,bboxes,hm_threshold)
#
#     draw_img = visualizer.draw_labeled_bboxes(image, bboxes)
#     # visualizer.draw_image(draw_img)
#     # visualizer.save_image(detection_img,i)
#     # writer1.write(detection_img)
#     # result2 = svm.find_cars(image)
#     # writer2.write(result2)
#     # tracker.update(cluster_bboxes)
#     # track_result = visualizer.draw_tracking(image,tracker)
#     # visualizer.draw_image(track_result)
#     # writer1.write(track_result)
#     debug.store_detected_bounding_boxes(bboxes,i)
#
# debug.write_detection()


filename = 'project_video.mp4'

vid = imageio.get_reader(filename,  'ffmpeg')

detections = debug.read_detected_bounding_boxes()
tracker = Tracking()

writer1 = VideoWriter('tracking_2.mp4',frameSize=image_size,fps=24)
writer1.open()

# writer2 = VideoWriter('detection.mp4',frameSize=image_size,fps=2)
# writer2.open()

for i in range(len(detections)):
    frame = detections[i]['frame']
    image = vid.get_data(frame)
    boxes = detections[i]['boxes']
    bboxes = []
    for dict_box in boxes:
        bboxes.append(BoundingBox(dict_box))
    # detection_img = visualizer.draw_labeled_bboxes(image,bboxes)
    # writer2.write(detection_img)
    # visualizer.draw_image(detection_img)

    tracker.prediction()

    tracker.update(bboxes)

    # print(tracker.get_number_of_tracks())
    track_result = visualizer.draw_tracking(image, tracker)
    writer1.write(track_result)