import rospy

from user_input import *
from abstract_dialogue_line import AbstractDialogueLine
from dialogue_line_repeat_please import DialogueLineRepeatPlease


class DialogueLineBinaryResponse(AbstractDialogueLine):
    """
    DialogueLineBinaryResponse indicates a simple yes/no question. It uses a BinaryResponse wait for user input and
    chooses the next line based on it.
    """

    def __init__(self, utterance, cancelable, next_line_yes, next_line_no):
        # type: (str, bool, AbstractDialogueLine, AbstractDialogueLine) -> None
        self.utterance = utterance
        self.next_line_yes = next_line_yes
        self.next_line_no = next_line_no
        self.cancelable = cancelable

    def get_next_line(self, response):
        # type: (str) -> AbstractDialogueLine

        if response == BinaryButtonInput.BINARY_YES:
            rospy.loginfo("'yes' detected! Continuing conversation...")
            return self.next_line_yes

        rospy.loginfo("'no' detected! Continuing conversation...")
        return self.next_line_no

    def get_utterance(self):
        # type: () -> str
        return self.utterance

    def request_user_response(self):
        # type: () -> AbstractUserInput
        return BinaryButtonInput()

    def can_cancel(self):
        return self.cancelable
