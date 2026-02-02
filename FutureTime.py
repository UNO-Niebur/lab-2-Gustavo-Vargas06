#FutureTime.py
#Name: Gustavo Vargas
#Date: 02/1/2026
#Assignment: FutureTime Lab 2

# datetime will allow us to access the system date and time.
import datetime 

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print (currentHour,":", currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  hours = int(input("How many hours? :"))
  #Ask user for minutes
  minutes = int(input("How many minutes? :"))
  #Calculate the time after the user-supplied time has passed.
  futureHour = currentHour + hours
  print(futureHour)
  futureMin = currentMinute + minutes
  print(futureMin)
  #Do not use any if statements in calculating the time.
  futureMin = futureMin % 60
  overmin = (currentMinute + futureMin) % 60
  print(overmin)
  futureHour = (futureHour + overmin) % 12
  #Output the future time in standard format "HH:MM"
  print ("your future time is", futureHour,":", futureMin)
  
if __name__ == '__main__':
  main()
