import random

from dialogue import Dialogue
from dialogue_action import *
from dialogue_manager import DialogueLibrary


class DialogueLibraryQuiz(DialogueLibrary):
    """
    A DialogueLibrary that can be used when a CommU robot sees an object. This plays 'object hide-and-seek' with the user.
    """

    def get_dialogue_for_topic(self, topic):
        # type: (str) -> Dialogue
        """
        Get the dialogue that can be used when CommU sees an object.
        :param topic:   The label assigned by the ssd network
        :return:        The Dialogue concerning the object.
        """
        #return Dialogue(DialogueLibraryQuiz.select_convo(self,topic))
        return Dialogue(DialogueLibraryQuiz.dialogue_string_test(self))

        # return Dialogue(
        #     DialogueActionLook(
        #         look_type=DialogueActionLook.LOOK_TYPE_WATCH_CONVERSATION_PARTNER,
        #         cancelable=False,
        #         next_action=
        #         DialogueActionSleep(
        #             sleep_time=1,
        #             cancelable=False,
        #             next_action=
        #             DialogueActionTalkBinaryResponse(
        #                 utterance="Do you also see {}?".format(self.__add_a_to_noun(self.__get_object_noun(topic))),
        #                 cancelable=False,
        #                 next_action_yes=
        #                 DialogueActionTalkNoResponse(
        #                     utterance=random.choice(self.positive_response_list),
        #                     cancelable=False,
        #                     next_action=
        #                     DialogueActionLook(
        #                         look_type=DialogueActionLook.LOOK_TYPE_WATCH_ENVIRONMENT,
        #                         cancelable=True,
        #                         next_action=None
        #                     )
        #                 ),
        #                 next_action_no=
        #                 DialogueActionLook(
        #                     look_type=DialogueActionLook.LOOK_TYPE_WATCH_CONVERSATION_TOPIC,
        #                     cancelable=False,
        #                     next_action=
        #                     DialogueActionTalkNoResponse(
        #                         utterance=random.choice(self.negative_response_list),
        #                         cancelable=False,
        #                         next_action=
        #                         DialogueActionSleep(
        #                             sleep_time=2,
        #                             cancelable=False,
        #                             next_action=DialogueActionLook(
        #                                 look_type=DialogueActionLook.LOOK_TYPE_WATCH_ENVIRONMENT,
        #                                 cancelable=True,
        #                                 next_action=None
        #                             )
        #                         )
        #                     ),
        #                 )
        #             )
        #         )
        #     )
        # )



    # import requests
    # r = requests.get("http://example.com/foo/bar")
    # print r.header
    #
    # print function

    def select_convo(self,topic,intcount=0,):

        if topic!='dog':
            return DialogueActionTalkNoResponse(
                utterance="hey",
                cancelable=False,
                next_action=None
            )

        else:
            # change g1 to received code

            #######################################################
            # sample dog convo, query from server/dictionary later#
            #######################################################
            dog1 = {}
            dog1[1] = {"utterance": "Are you interested in {}", "cancelable": "No","nextaction": "g11".format(self.__add_a_to_noun(self.__get_object_noun(topic)))}
            dog1[2] = {"utterance": "And why is that so?", "cancelable": "No", "nextaction": "g12"}
            dog1[3] = {"utterance": "And why is that so?", "cancelable": "No", "nextaction": "None", }
            dog1["last_interaction"] = {3}  # not needed i think
            # receive code here and assign it to something

            chosen_reply = dog1
            # change g1 to received code

            lastintcount = set.pop(chosen_reply["last_interaction"])

            return self.generating(intcount,lastintcount,topic,chosen_reply)

    def generating(self,intcount,lastintcount,topic,chosen_reply):

        intcount += 1
        # if intcount==lastintcount:
        if chosen_reply[intcount]['nextaction'] == 'None':
            return ("None")

        else:
            # for intcount<lastintcount:
            # not needed if not using lastintcount
            return (DialogueActionTalkNoResponse(
                utterance=chosen_reply['intcount']['utterance'],
                cancelable=chosen_reply['intcount']['cancelable'],
                next_action=self.generating(self, intcount, lastintcount, chosen_reply)
                )
            )



    def __add_a_to_noun(self, noun):
        # type: (str) -> str

        if noun[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            return 'an ' + noun
        else:
            return 'a ' + noun

    def __get_object_noun(self, label):
        return self.object_proper_name_map.get(label, label)

    object_proper_name_map = {
        'aeroplane': 'airplane',
        'diningtable': 'dining table',
        'pottedplant': 'potted plant',
        'tvmonitor': 'screen'
    }

    positive_response_list = [
        "Cool, you're good!",
        "Nice, me too!",
        "I see it too!"
    ]

    negative_response_list = [
        "I see it over there",
        "It's over there",
        "I can help you. It's over here"
    ]


    def dialogue_string_test(self):

        dia = "DialogueActionTalkNoResponse(utterance='one',cancelable=False,next_action=DialogueActionTalkNoResponse(utterance='two',cancelable=False,next_action=None))"

        return eval(dia)