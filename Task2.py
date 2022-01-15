mph=[]
kph=[]
print("Swallow Speed Analysis: Version 1.0\n")
while True:
    swallow_speed=input("Enter the speed: ")
    if swallow_speed:
        if (swallow_speed[0].lower()!="u" and swallow_speed[0].lower()!="e") or swallow_speed[1:].isalpha():
            print("Invalid input")
            continue

        speed=float(swallow_speed[1:])

        if swallow_speed[0].lower()=="u":
            mph.append(speed)
            speed*=1.61
            kph.append(speed)
            
        else:
            kph.append(speed)
            speed/=1.61
            mph.append(speed)

        print("Reading saved.")
    else:
        break

if mph!=[]:
    maximumMPH=max(mph)
    minimumMPH=min(mph)
    averageMPH=sum(mph)/len(mph)
    maximumKPH=max(kph)
    minimumKPH=min(kph)
    averageKPH=sum(kph)/len(kph)
    
    print("\nResults Summary\n")
    print(f"{len(mph)} Readings Analysed.\n" if len(mph) >1 else f"{len(mph)} Reading Analysed\n")
    print("Max Speed:{:.2f} MPH,{:.2f} KPH".format(maximumMPH,maximumKPH))
    print("Min Speed:{:.2f} MPH,{:.2f} KPH".format(minimumMPH,minimumKPH))
    print("Avg Speed:{:.2f} MPH,{:.2f} KPH".format(averageMPH,averageKPH))

else:
    print("No readings entered. Nothing to do.") 