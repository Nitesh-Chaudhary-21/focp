print("Stop! Who would cross the Bridge of Death \nMust answer me these questions three, 'ere the other side he see.")

name = input("What is your name? ")

if"arthur" in name.lower():
    print("My liege! You may pass!")
    
else:
    quest = input("What is your quest? ")

    if "grail" in quest or "Grail" in quest:
        colour=input("What is your favourite colour? ")

        if name[0].capitalize()==colour[0].capitalize():
            print("you may pass")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")

    else:      
        print("Only those who seek the Grail may pass.")  
