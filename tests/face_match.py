# 利用指定detector匹配人/佛脸
import os
import sys
import glob
import time

import dlib

faces_folder = "faces/buddhism"
# faces_folder = "examples/faces"

# Now let's use the detector as you would in a normal application.  First we
# will load it from disk.
detector = dlib.simple_object_detector("data/detector_buddhism.svm")

# We can look at the HOG filter we learned.  It should look like a face.  Neat!
win_det = dlib.image_window()
win_det.set_image(detector)

# Now let's run the detector over the images in the faces folder and display the
# results.
print("Showing detections on the images in the faces folder...")
win = dlib.image_window()
for f in glob.glob(os.path.join(faces_folder, "*.jpg")):
    print("Processing file: {}".format(f))
    img = dlib.load_rgb_image(f)
    dets = detector(img)
    print("Number of faces detected: {}".format(len(dets)))
    for k, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.left(), d.top(), d.right(), d.bottom()))

    win.clear_overlay()
    win.set_image(img)
    win.add_overlay(dets)
    # dlib.hit_enter_to_continue()
    time.sleep(2)




# # Next, suppose you have trained multiple detectors and you want to run them
# # efficiently as a group.  You can do this as follows:
# detector1 = dlib.fhog_object_detector("data/detector.svm")
# # In this example we load detector.svm again since it's the only one we have on
# # hand. But in general it would be a different detector.
# detector2 = dlib.fhog_object_detector("data/detector.svm")
# # make a list of all the detectors you want to run.  Here we have 2, but you
# # could have any number.
# detectors = [detector1, detector2]
# image = dlib.load_rgb_image(faces_folder + '/2008_002506.jpg')
# [boxes, confidences, detector_idxs] = dlib.fhog_object_detector.run_multiple(detectors, image, upsample_num_times=1, adjust_threshold=0.0)
# for i in range(len(boxes)):
#     print("detector {} found box {} with confidence {}.".format(detector_idxs[i], boxes[i], confidences[i]))




# # Finally, note that you don't have to use the XML based input to
# # train_simple_object_detector().  If you have already loaded your train
# # images and bounding boxes for the objects then you can call it as shown
# # below.
#
# # You just need to put your images into a list.
# images = [dlib.load_rgb_image(faces_folder + '/2008_002506.jpg'),
#           dlib.load_rgb_image(faces_folder + '/2009_004587.jpg')]
# # Then for each image you make a list of rectangles which give the pixel
# # locations of the edges of the boxes.
# boxes_img1 = ([dlib.rectangle(left=329, top=78, right=437, bottom=186),
#                dlib.rectangle(left=224, top=95, right=314, bottom=185),
#                dlib.rectangle(left=125, top=65, right=214, bottom=155)])
# boxes_img2 = ([dlib.rectangle(left=154, top=46, right=228, bottom=121),
#                dlib.rectangle(left=266, top=280, right=328, bottom=342)])
# # And then you aggregate those lists of boxes into one big list and then call
# # train_simple_object_detector().
# boxes = [boxes_img1, boxes_img2]
#
# # Now let's do the train.  The train_simple_object_detector() function has a
# # bunch of options, all of which come with reasonable default values.  The next
# # few lines goes over some of these options.
# options = dlib.simple_object_detector_training_options()
# # Since faces are left/right symmetric we can tell the trainer to train a
# # symmetric detector.  This helps it get the most value out of the train
# # data.
# options.add_left_right_image_flips = True
# # The trainer is a kind of support vector machine and therefore has the usual
# # SVM C parameter.  In general, a bigger C encourages it to fit the train
# # data better but might lead to overfitting.  You must find the best C value
# # empirically by checking how well the trained detector works on a test set of
# # images you haven't trained on.  Don't just leave the value set at 5.  Try a
# # few different C values and see what works best for your data.
# options.C = 5
# # Tell the code how many CPU cores your computer has for the fastest train.
# options.num_threads = 4
# options.be_verbose = True
#
# detector2 = dlib.train_simple_object_detector(images, boxes, options)
# # We could save this detector to disk by uncommenting the following.
# #detector2.save('detector2.svm')
#
# # Now let's look at its HOG filter!
# win_det.set_image(detector2)
# # dlib.hit_enter_to_continue()
# time.sleep(2)
#
# # Note that you don't have to use the XML based input to
# # test_simple_object_detector().  If you have already loaded your train
# # images and bounding boxes for the objects then you can call it as shown
# # below.
# print("\nTraining accuracy: {}".format(
#     dlib.test_simple_object_detector(images, boxes, detector2)))
#
# for f in glob.glob(os.path.join(faces_folder, "*.jpg")):
#     print("Processing file: {}".format(f))
#     img = dlib.load_rgb_image(f)
#     dets = detector2(img)
#     print("Number of faces detected: {}".format(len(dets)))
#     for k, d in enumerate(dets):
#         print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
#             k, d.left(), d.top(), d.right(), d.bottom()))
#
#     win.clear_overlay()
#     win.set_image(img)
#     win.add_overlay(dets)
#     # dlib.hit_enter_to_continue()
#     time.sleep(2)