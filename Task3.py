from random import choice

def isemail(email,domain):
    if email.count("@")!=1:
        return False
    
    if len(email.split("@")[0])<2:
        return False

    if email.split("@")[1]!=domain:
        return False
    
    return True

networ_error=[True,True,True,True,True,True,True,True,True,False]
server_name=["harry","may","paul"]
exit_statement=["bye","exit","help"] 
no_output=["hmm","i see"]
print("Welcome to Pop Chat \nOne of our operators will be pleased to help you today.\n")
email=input("Please enter your Poppleton email address:")

if(isemail(email,"pop.ac.uk")):
    print("Hi, {}! Thank you, and Welcome to PopChat!".format(email.split("@")[0]))
    print(f"My name is {choice(server_name)}, and it will be my pleasure to help you.")
    while True:
        exit=False
        sent=input("-->")
        if choice(networ_error)==False:
            print("Network error")
            print("Thanks, {}, for using PopChat. See you again soon!".format(email.split("@")[0]))
            break
        for i in exit_statement:
            if i in sent:
                exit = True
        if exit:
            print("Thanks, {}, for using PopChat. See you again soon!".format(email.split("@")[0]))
            break
        elif("library" in sent):
            print("The library is closed today.")
        elif("WiFi" in sent):
            print("WiFi is excellent across the campus.")
        elif "deadline" in sent:
            print( "Your deadline has been extended by two working days.")
        elif "books" in sent:
            print( "The library is on the first floor")
        elif "classes" in sent:
            print( "classes will start next week")
        elif "teacher" in sent:
            print( "The teacher is unavailable")
        
        else:
            print(choice(no_output))
            
else:
    print("This email is not valid")
