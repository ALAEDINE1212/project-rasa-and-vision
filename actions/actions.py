# Importing necessary modules
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionProvideName(Action):
    def name(self) -> str:
        return "action_provide_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Retrieve name slot
        name = tracker.get_slot("name")
        if name:
            dispatcher.utter_message(text=f"Hello {name}, nice to meet you!")
        else:
            dispatcher.utter_message(text="Can you please provide me with your name?")
        return []


class ActionProvideEmail(Action):
    def name(self) -> str:
        return "action_provide_email"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Retrieve email slot
        email = tracker.get_slot("email")
        if email:
            dispatcher.utter_message(text=f"Got your email as {email}. Thank you!")
        else:
            dispatcher.utter_message(text="Can you please provide me with your email?")
        return []


class ActionThankYou(Action):
    def name(self) -> str:
        return "action_thank_you"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        name = tracker.get_slot("name")
        email = tracker.get_slot("email")

        if name and email:
            dispatcher.utter_message(text=f"Thank you {name}, we've noted your email as {email}.")
        else:
            dispatcher.utter_message(text="Thank you for your information.")

        return []


class ActionCheckUserInfo(Action):
    def name(self) -> str:
        return "action_check_user_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        name = tracker.get_slot("name")
        email = tracker.get_slot("email")

        # Check if both name and email are filled
        if name and email:
            dispatcher.utter_message(text=f"Your name is {name} and your email is {email}.")
        elif name:
            dispatcher.utter_message(text=f"Your name is {name}, but I still need your email.")
        elif email:
            dispatcher.utter_message(text=f"Your email is {email}, but I still need your name.")
        else:
            dispatcher.utter_message(text="I still need both your name and email.")
        return []
