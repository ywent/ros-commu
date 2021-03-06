import time
from threading import Thread

import cv2
import numpy as np
import rospy
from cv_bridge import CvBridge
from ssd.msg import ClassifiedObjectArray

import util


class DebugHandler:

    def __init__(self, classification_topic, window_name="Debug window"):
        rospy.loginfo("Initializing DebugHandler..")
        self.window_name = window_name
        self.image_bridge = CvBridge()
        self.image_margin = 50

        self.image_size = None
        self.latest_cv_image = None
        self.latest_utter_cv_image = None
        self.latest_utter_until = time.time()
        self.latest_look_cv_image = None
        self.latest_classification_image = None

        self.display_image = None

        self.thread = None

        rospy.loginfo("Subscribing to '%s' topic for classification results..", classification_topic)
        rospy.Subscriber(classification_topic, ClassifiedObjectArray, self.classification_received)

        self.spin_image_window()

    def classification_received(self, data):
        self.latest_cv_image = util.image_to_opencv(data.image)
        self.image_size = self.latest_cv_image.shape

        cv_image = np.zeros(self.image_size, np.uint8)
        cv_image = util.add_alpha_layer(cv_image, 0)
        cv_image = util.draw_image_margin(cv_image, self.image_margin)

        self.latest_classification_image = util.draw_bounding_boxes(cv_image, data.objects, self.image_margin)

    def commu_utter_received(self, utterance, blocking, english):
        if self.image_size is None:
            return

        cv_image = np.zeros(self.image_size, np.uint8)
        cv_image = util.add_alpha_layer(cv_image, 0)
        cv_image = util.draw_image_margin(cv_image, self.image_margin)

        string = "Saying: \"{}\"...".format(utterance)

        cv_image = util.draw_crosshair(cv_image, 100, 100)
        cv_image = util.draw_text(cv_image, string, 0, 0, background=True, color=(0, 0, 0, 255), background_color=(255, 255, 0, 255))

        self.latest_utter_cv_image = cv_image
        self.latest_utter_until = time.time() + util.approximate_say_time(utterance)

    def commu_look_received(self, x, y, z):
        if self.image_size is None:
            return

        cv_image = np.zeros(self.image_size, np.uint8)
        cv_image = util.add_alpha_layer(cv_image, 0)
        cv_image = util.draw_image_margin(cv_image, self.image_margin)

        # Note: these coordinates are very rough approximations.
        cv_image = util.draw_crosshair(cv_image, x + self.image_margin + self.image_size[0], y + self.image_margin + self.image_size[1])

        self.latest_look_cv_image = cv_image

    def merge_images(self):
        merge_look_image = self.latest_look_cv_image is not None
        merge_utter_image = self.latest_utter_until >= time.time()
        merge_classification_image = self.latest_classification_image is not None

        self.display_image = util.draw_image_margin(self.latest_cv_image)

        if merge_classification_image:
            self.display_image = util.draw_overlay_image(self.display_image, self.latest_classification_image)

        if merge_utter_image:
            self.display_image = util.draw_overlay_image(self.display_image, self.latest_utter_cv_image)

        if merge_look_image:
            self.display_image = util.draw_overlay_image(self.display_image, self.latest_look_cv_image)

    def spin_image_window(self):
        rospy.loginfo("Starting window image thread...")

        if self.thread is not None:
            rospy.loginfo("Someone tried to start two image windows of the same instance. This is not supposed to happen.")
            return

        def worker():
            rospy.loginfo("Initializing DebugHandler cv2 window with name: '%s'..", self.window_name)
            cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(self.window_name, 1280, 960)

            rospy.loginfo("Starting image worker thread.")

            while not rospy.is_shutdown():
                if self.latest_cv_image is not None:
                    self.merge_images()
                    cv2.imshow(self.window_name, self.display_image)

                cv2.waitKey(1000 / 30)

            cv2.destroyWindow(self.window_name)
            rospy.loginfo("Stopping image worker thread.")

        self.thread = Thread(target=worker)
        self.thread.start()



