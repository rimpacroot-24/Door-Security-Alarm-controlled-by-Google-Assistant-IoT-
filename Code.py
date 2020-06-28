import time                   #Import time to peform delay operations
import requests               #use requests to send mail via webhooks IFTTT
from boltiot import Bolt      #Import boliot to control GPIO pins through API

api_key = "4749fe75-6c61-45f1-bee5-f9a6a1bd9103"        #Get your API key from Bolt Cloud Website  
device_id  = "BOLT11691968"                             #Get your Bolt device ID form Bolt Cloud Website
mybolt = Bolt(api_key, device_id)

HIGH = '{"value": "1", "success": "1"}'                 #This will be returned by bolt API if digital read is high 
LOW = '{"value": "0", "success": "1"}'                  #This will be returned by bolt API if digital read is low

alarm = 0 #Alarm is turned off by default 

while True: #Infinite loop

    while alarm == 0: #If alarm is off
        response = mybolt.digitalRead('3')              #check if it is being activated 
        if (response == HIGH):
            print("Security System is activated")
            mybolt.digitalWrite('2', 'HIGH')            #Turn on LED to indicate Aalarm is activated 
            alarm = 1
        elif (response == LOW):
            print ("Waiting for Security System to be activated....")
        else:
            print ("Probelm in getting value form pin 3")
        time.sleep(5) #check once in every 5 seconds to avoid exceeding API rate lmit  
    

    while alarm == 1:                                   #If alarm is on 
        response = mybolt.digitalRead('4')              #check is it is being de-activated 
        if (response == HIGH):
            print("Security System is De-activated")
            mybolt.digitalWrite('2', 'LOW')             #Turn off LED to indicate Aalarm is De-activated 
            alarm = 0 
            time.sleep(5)
        elif (response == LOW):
            print ("Security System is currently active can be deactivated from google assistant")
        else:
            print ("Probelm in getting value form pin 4")

        response = mybolt.digitalRead('0')               #check if hall sensor is triggered 
        if (response == HIGH):                           #if magnet is not present      
            print ("Alert! Security breach Buzzer ON")
            mybolt.digitalWrite('1', 'HIGH')
            requests.get('https://maker.ifttt.com/trigger/Breach/with/key/i6nPcZ5ZlzaVdbYITw6VGcpM...')            #webhook link to trigger mail through IFTTT
            time.sleep(5)
            mybolt.digitalWrite('1', 'LOW')
            print ("Buzzer OFF")
        elif (response == LOW):
            print ("No probelm, all good!")
        else:  
            print ("Problem in reading the value of button")
        time.sleep(5)
