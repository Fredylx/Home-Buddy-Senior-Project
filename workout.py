'''
Author:       Fredy H Lopez
Title:        workout
Date:         
Style:        Python

----------------------------- Work In Progress----------------------------
this is a the script ment for the workout buddy simulation. For IoT Introduction class.
was done during lockdown. Made for simulation in Packet Tracer or a real life Arduino or Raspberry Pi build
'''


def workout(): while(True):
  delay(1000)
  customWrite(3, 'Hey you...\nLets GO') delay(2000)
  customWrite(3,'Press the Button\nTo Start') if(digitalRead(0,True)):
  ups section
  #Push-
  for n in range(0, 1):
   sleep(1) customWrite(3,'Push-ups\nGet Ready') sleep(3)
   countdown()
   sleep(1)
   customWrite(3,'UNDERWAY!')
   sleep(1)
   digitalWrite(1,HIGH)
   sleep(1)
   digitalWrite(1,LOW) digitalWrite(2,HIGH)
   sleep(2.5)
   digitalWrite(2,LOW)
   pushups()
   sleep(timeRest)
   legraises()
  
  #First Set(Push-ups & Leg Raises)
  for n in range(1,(int(numsetsmin))): 
   customWrite(3,'Nice work')
   sleep(1)
   customWrite(3,numrepsmin + 'more to go\nGet ready') sleep(timeRest)
   customWrite(3,'Push-ups')
   sleep(2)
   customWrite(3,'3')
   sleep(1)
   customWrite(3,'2')
   sleep(1)
   customWrite(3,'1')
   sleep(1)
   customWrite(3,'GO')
   sleep(1) customWrite(3,' ')
   
  for m in range(0, int(numsetsmin)): 
   digitalWrite(1,HIGH)
   sleep(1)
   digitalWrite(1,LOW) digitalWrite(2,HIGH) sleep(2.5) digitalWrite(2,LOW) pushups()
  for m in range(1): #Leg Raises
   customWrite(3,'Leg Raises\nGet ready') digitalWrite(2,LOW)
   sleep(.5)
   digitalWrite(5,HIGH)
   sleep(.5) digitalWrite(5,LOW) sleep(5) digitalWrite(5,HIGH) legraises()
   customWrite(3,'Great job\nAgain?')
   sleep(5) if(digitalRead(0,True)):
  return repeat() elif(digitalRead(0,True)):
  customWrite(4,'Good Work Today') sleep(2)
  return
  #Push-ups
