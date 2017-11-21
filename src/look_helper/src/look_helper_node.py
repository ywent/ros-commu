import rospy
from look_manager import *
from realsense_person.msg import PersonDetection

def person_classification_callback(manager, data):
    rospy.loginfo("Person classification data: " + str(data))


def init_message_listeners(manager):
    def person_callback(data):
        person_classification_callback(manager, data)

    rospy.Subscriber("/camera/person/detection_data", PersonDetection, person_callback)


def init_message_publishers(manager):
    pass


if __name__ == '__main__':
    rospy.init_node("look_helper")
    rospy.loginfo("Starting look_helper node..")

    rospy.loginfo("Creating LookManager..")
    manager = LookManager()

    init_message_listeners(manager)
    init_message_publishers(manager)

    #manager.start(utter, threaded=True, perpetual=True)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass
