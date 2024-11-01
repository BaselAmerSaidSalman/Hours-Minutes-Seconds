import time
seconds = int(input("Enter the number of seconds: \n"))
print("Your time is = " + str(seconds // 3600) + " hours and " + str(seconds % 3600 // 60) + " minutes and " + str(seconds % 3600 % 60) + " seconds")
print("You were born in " + str(2024 - int(input("How old are you? \n"))))
time.sleep(2)