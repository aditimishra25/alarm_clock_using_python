import time
import winsound
def myAlarm():
    try:
        myTime = list (map(int,input("Enter the time in hr min sec\n").split()))
        if len(myTime)==3:
            total_seconds=myTime[0]*60*60+myTime[1]*60+myTime[2]
            time.sleep(total_seconds)
            frequency= 2500 # setting frequency to 2500 hertz
            duration = 1000 # setting duration to 1000ms=1sec
            winsound.Beep(frequency,duration)

        else:
            print("Please enter time in the the correct format\n")
            myAlarm()
    except Exception as e:
        print("This is an exception\n",e,"So, please enter correct details")
        myAlarm()
myAlarm()

