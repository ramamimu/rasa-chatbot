# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# from rasa_sdk.interfaces import Action, Tracker

class ActionCustom(Action):
    def name(self):
        return "action_custom"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Hello World!")
        return []
    
# class ActionName(Action):
#     def name(self):
#         return "action_name"

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_message("My name is Rasa!")
#         return []

class ActionShoe(Action):
    def name(self):
        return "action_shoe"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        shoe_size = tracker.get_slot("shoesize")

        if not shoe_size:
            dispatcher.utter_message("Please provide your shoe size!")
            return []
        else:
            dispatcher.utter_message("Your shoe size is {}".format(shoe_size))
        return []