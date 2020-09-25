speed = int(input("What was your average speed?"))
allowed_speed = int(input("What was the allowed speed on the road?"))
if speed > allowed_speed:
    demerit=(speed-allowed_speed)//5
    print(demerit)
    if demerit>=12:
        print("Time to go to jail!")





