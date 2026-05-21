def check_active():
    active = True
    print("Session Active: y/n")
    user_input = input().lower()

    while user_input != "y" and user_input != "n":
        user_input = input().lower()
    
    if user_input == "y":
        active = True
    else: 
        active = False

    return active