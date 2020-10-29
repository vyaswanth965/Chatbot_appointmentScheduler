from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, FollowupAction
from rasa_core_sdk.forms import FormAction


from timefhuman import timefhuman




class FacilityForm(FormAction):
    """Custom form action to fill all slots required to find specific type
    of healthcare facilities in a certain city or zip code."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "schedule_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["city", "date","time","specialist","dr"]

    def slot_mappings(self) -> Dict[Text, Any]:

        return {"city": self.from_entity(entity="city",
                                                  intent=["inform",
                                                          "create_apt"]),
                "date": self.from_entity(entity="date",
                                             intent=["inform",
                                                     "create_apt"]),
                "time": self.from_entity(entity="time",
                                             intent=["inform",
                                                     "create_apt"]),
                "specialist": self.from_entity(entity="specialist",
                                             intent=["inform",
                                                     "create_apt"]),
                "dr": self.from_entity(entity="dr",
                                             intent=["inform",
                                                     "create_apt"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, print buttons for found facilities"""


        date = tracker.get_slot("date")
        time = tracker.get_slot("time")
        dr = tracker.get_slot("dr")
        city = tracker.get_slot("city")
        specialist = tracker.get_slot("specialist")
        try :
            date = str(timefhuman(date).date())
        except AssertionError as e:
            pass
        try :
            time = str(timefhuman(time).time())
        except AssertionError as e:
            pass        
        print(date ,time)
        dispatcher.utter_template("utter_submit", tracker)
        return [SlotSet('date',date), SlotSet('time',time)]
            