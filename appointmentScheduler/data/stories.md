## bye
* bye
    - utter_bye

## greet
* greet
    - utter_greet

## Generated Story -5169498839831674046
* stop
    - utter_ask_continue
* affirm
    - schedule_form
    - utter_slots_values

## Generated Story 
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}    
	
## Happy path
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
    - form{"name": null}
    - utter_slots_values
* affirm
    - utter_confirmed
* bye
    - utter_bye        

## Happy path2
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
    - form{"name": null}
    - utter_slots_values
* deny
    - utter_reenter
* inform    
    - schedule_form    
    - form{"name": null}
    - utter_slots_values
* affirm
    - utter_confirmed
* bye
    - utter_bye 

## Happy path3
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
    - form{"name": null}
    - utter_slots_values
* inform    
    - schedule_form    
    - form{"name": null}
    - utter_slots_values
* affirm
    - utter_confirmed
* bye
    - utter_bye 

## unhappy path
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* chitchat
    - utter_chitchat
    - schedule_form
    - form{"name": null}
    - utter_slots_values 
* affirm
    - utter_confirmed
* bye
    - utter_bye         

## unhappy path2
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* chitchat
    - utter_chitchat
    - schedule_form
    - form{"name": null}
    - utter_slots_values
* deny
    - utter_reenter
* inform    
    - schedule_form    
    - form{"name": null}
    - utter_slots_values     
* affirm
    - utter_confirmed
* bye
    - utter_bye


## unhappy path3
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* chitchat
    - utter_chitchat
    - schedule_form
    - form{"name": null}
    - utter_slots_values 
* inform    
    - schedule_form    
    - form{"name": null}
    - utter_slots_values 
* affirm
    - utter_confirmed
* bye
    - utter_bye    

## very unhappy path
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* chitchat
    - utter_chitchat
    - schedule_form
* chitchat
    - utter_chitchat
    - schedule_form
* chitchat
    - utter_chitchat
    - utter_ask_continue
* affirm OR inform
    - schedule_form    
    - form{"name": null}
    - utter_slots_values 
* affirm
    - utter_confirmed
* bye
    - utter_bye     

## very unhappy path2
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* chitchat
    - utter_chitchat
    - schedule_form
* chitchat
    - utter_chitchat
    - schedule_form
* chitchat
    - utter_chitchat
    - utter_ask_continue 
* deny
    - action_deactivate_form
    - form{"name": null}


## stop but continue path
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* stop
    - utter_ask_continue
* affirm
    - schedule_form    
    - form{"name": null}
    - utter_slots_values 
* affirm
    - utter_confirmed
* bye
    - utter_bye       

## stop but continue path2
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* stop
    - utter_ask_continue
* affirm
    - schedule_form    
    - form{"name": null}
    - utter_slots_values 
* deny
    - utter_reenter
* inform    
    - schedule_form    
    - form{"name": null}
    - utter_slots_values 
* affirm
    - utter_confirmed
* bye
    - utter_bye 

## stop but continue path3
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* stop
    - utter_ask_continue
* affirm
    - schedule_form    
    - form{"name": null}
    - utter_slots_values 
* inform    
    - schedule_form    
    - form{"name": null}
    - utter_slots_values 
* affirm
    - utter_confirmed
* bye
    - utter_bye 
## stop and really stop path
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}    

    

## chitchat stop but continue path
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* chitchat
    - utter_chitchat
    - schedule_form
* stop
    - utter_ask_continue
* affirm
    - schedule_form    
    - form{"name": null}
    - utter_slots_values 
* affirm
    - utter_confirmed
* bye
    - utter_bye        

## chitchat stop but continue path2
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* chitchat
    - utter_chitchat
    - schedule_form
* stop
    - utter_ask_continue
* affirm
    - schedule_form    
    - form{"name": null}
    - utter_slots_values 
* deny
    - utter_reenter
* inform    
    - schedule_form    
    - form{"name": null}
    - utter_slots_values 
* affirm
    - utter_confirmed
* bye
    - utter_bye  

## chitchat stop but continue path3
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* chitchat
    - utter_chitchat
    - schedule_form
* stop
    - utter_ask_continue
* affirm
    - schedule_form    
    - form{"name": null}
    - utter_slots_values 
* inform    
    - schedule_form    
    - form{"name": null}
    - utter_slots_values 
* affirm
    - utter_confirmed
* bye
    - utter_bye  


## stop but continue and chitchat path
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* stop
    - utter_ask_continue
* affirm
    - schedule_form
* chitchat
    - utter_chitchat
    - schedule_form
    - form{"name": null}
    - utter_slots_values 
* affirm
    - utter_confirmed
* bye
    - utter_bye     

## stop but continue and chitchat path2
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* stop
    - utter_ask_continue
* affirm
    - schedule_form
* chitchat
    - utter_chitchat
    - schedule_form
    - form{"name": null}
    - utter_slots_values 
* deny
    - utter_reenter
* inform    
    - schedule_form    
    - form{"name": null}
    - utter_slots_values
* affirm
    - utter_confirmed
* bye
    - utter_bye

## stop but continue and chitchat path3
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* stop
    - utter_ask_continue
* affirm
    - schedule_form
* chitchat
    - utter_chitchat
    - schedule_form
    - form{"name": null}
    - utter_slots_values 
* inform    
    - schedule_form    
    - form{"name": null}
    - utter_slots_values
* affirm
    - utter_confirmed
* bye
    - utter_bye    

## chitchat stop but continue and chitchat path
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* chitchat
    - utter_chitchat
    - schedule_form
* stop
    - utter_ask_continue
* affirm
    - schedule_form
* chitchat
    - utter_chitchat
    - schedule_form
    - form{"name": null}
    - utter_slots_values 
* affirm
    - utter_confirmed
* bye
    - utter_bye

## chitchat stop but continue and chitchat path2
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* chitchat
    - utter_chitchat
    - schedule_form
* stop
    - utter_ask_continue
* affirm
    - schedule_form
* chitchat
    - utter_chitchat
    - schedule_form
    - form{"name": null}
    - utter_slots_values 
* deny
    - utter_reenter
* inform    
    - schedule_form    
    - form{"name": null}
    - utter_slots_values
* affirm
    - utter_confirmed
* bye
    - utter_bye

## chitchat stop but continue and chitchat path3
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* chitchat
    - utter_chitchat
    - schedule_form
* stop
    - utter_ask_continue
* affirm
    - schedule_form
* chitchat
    - utter_chitchat
    - schedule_form
    - form{"name": null}
    - utter_slots_values 
* inform    
    - schedule_form    
    - form{"name": null}
    - utter_slots_values
* affirm
    - utter_confirmed
* bye
    - utter_bye

## chitchat, stop and really stop path
* greet
    - utter_greet
* create_apt
    - schedule_form
    - form{"name": "schedule_form"}
* chitchat
    - utter_chitchat
    - schedule_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}    


## bot
* bot_challenge
    - utter_iamabot
## Generated Story 9215004462807213085
* greet
    - utter_greet
* inform{"appointment": "appointment", "dr": "dr . krishna", "specialist": "dentist", "date": "tomorrow", "time": "3 pm", "city": "hubli"}
    - slot{"city": "hubli"}
    - slot{"date": "tomorrow"}
    - slot{"dr": "dr . krishna"}
    - slot{"specialist": "dentist"}
    - slot{"time": "3 pm"}
    - schedule_form
    - utter_slots_values
* affirm
    - utter_confirmed
* bye
    - utter_bye

## Generated Story 
* greet
    - utter_greet
* inform{"appointment": "appointment", "dr": "dr . krishna", "specialist": "dentist", "date": "tomorrow", "time": "3 pm", "city": "hubli"}
    - slot{"city": "hubli"}
    - slot{"date": "tomorrow"}
    - slot{"dr": "dr . krishna"}
    - slot{"specialist": "dentist"}
    - slot{"time": "3 pm"}
    - schedule_form
    - utter_slots_values
* deny
    - utter_reenter
* inform
    - schedule_form
    - form{"name": null}
    - utter_slots_values 
* affirm
    - utter_confirmed
* bye
    - utter_bye


## Generated Story2
* greet
    - utter_greet
* inform{"appointment": "appointment", "dr": "dr . krishna", "specialist": "dentist", "date": "tomorrow", "time": "3 pm", "city": "hubli"}
    - slot{"city": "hubli"}
    - slot{"date": "tomorrow"}
    - slot{"dr": "dr . krishna"}
    - slot{"specialist": "dentist"}
    - slot{"time": "3 pm"}
    - schedule_form
    - utter_slots_values
* inform
    - schedule_form
    - form{"name": null}
    - utter_slots_values 
* affirm
    - utter_confirmed
* bye
    - utter_bye    

## Generated Story 3006162452132285807
* greet
    - utter_greet
* create_apt{"appointment": "appointment"}
    - schedule_form
    - utter_slots_values
* affirm
    - utter_confirmed

## chitchat
* greet
    - utter_greet
* chitchat
    - utter_chitchat 


