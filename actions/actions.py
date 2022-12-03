# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.types import DomainDict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
)


class ActionSetUniRostockPreference(Action):

     def name(self) -> Text:
         return "action_set_uni_rostock_preference"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             
              intent = tracker.latest_message["intent"].get("name")
              print(intent)

              if intent == "affirm":
                return [SlotSet("like_uni_rostock", True)]
            
              if intent == "deny":
                return [SlotSet("like_uni_rostock", False)]

              return []


class ActionGreetUser(Action):
    """Greets the user"""

    def name(self) -> Text:
        return "action_greet_user"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        intent = tracker.latest_message["intent"].get("name")
        name_entity = next(tracker.get_latest_entity_values("name"), None)
        name_is_asked = tracker.get_slot("name_is_asked")
        user_name = tracker.get_slot("name")
        
        if (intent == "greet" or intent== "enter_data") and name_is_asked == True:
            dispatcher.utter_message(response="utter_greet_name_again", name=user_name)
            return []
        if intent == "greet"  and user_name:
            dispatcher.utter_message(response="utter_greet_name_first_time", name=user_name)
            return [SlotSet("name_is_asked", True)]
        
        if intent == "greet":
            dispatcher.utter_message(response="utter_greet_noname")
            return []
        
        if (intent== "enter_data") and name_is_asked == False:
            if  name_entity:
                dispatcher.utter_message(response="utter_greet_name_first_time", name=name_entity)
                return [SlotSet("name_is_asked", True)]
            else:
                dispatcher.utter_message(response="utter_greet_noname")
                return []
         
        return []

class ActionCheckMentionedThings(Action):
    """Check Menthioned Things"""

    def name(self) -> Text:
        return "action_check_mentioned_things"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        intent = tracker.latest_message["intent"].get("name")
      
        name_entity = next(tracker.get_latest_entity_values("name"), None)
        
        name_is_asked = tracker.get_slot("name_is_asked")
        user_name = tracker.get_slot("name")
        
        if intent == "asking_about_mentioned_things" and name_is_asked == True:
            dispatcher.utter_message(response="utter_greet_name_again", name=user_name)
            return []
        

        if  intent == 'asking_about_mentioned_things' and name_is_asked == False:
            if  name_entity:
                dispatcher.utter_message(response="utter_never_says_name", name=name_entity)
                return [SlotSet("name_is_asked", True)]
            else:
                dispatcher.utter_message(response="utter_do_not_say_the_name")
                return []
         
        return []
