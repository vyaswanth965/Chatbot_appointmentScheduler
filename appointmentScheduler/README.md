# Doctor-Appointment-Chatbot-using-Rasa
It Schedules Doctor Appointment using Rasa Framework, Data is collected from cities of Maharashtra.
The data colleted is Real time data and bot helps in booking for appointment in Tier II cities.

## deployment
cd appointmentScheduler
pip install -r requirements.txt
rasa run actions -vv
rasa train
rasa shell

# Following is the conversation flow between User and Bot

user:Hi bot

bot: Hi, how may i help you?

User:please book an appointment with doctor

bot:In whcih city would you like to book , Hubli or Dharwad?

User:Hubli

bot: What specialization are you looking for?

User: Dentist

bot: please select a date

user: Tuesday

bot:what time you would like to boo?

user: 3:00 PM

bot: Display list of Doctors (Doctor  name, city,address,phone number,Rating)

user: (will reply with doctor name and phone number.)

bot: your appointment with Dr..... at 3:00 PM successfully booked


user: thank you

bot: My pleasure to help you


#Reference
https://github.com/mukesh0290/Doctor-Appointment-Chatbot-using-Rasa

![alt text](https://github.com/vyaswanth965/Chatbot_appointmentScheduler/blob/main/appointmentScheduler/Screenshot%20from%202019-10-16%2013-37-59.png)
