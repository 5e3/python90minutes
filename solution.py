# FIRST LINE: Ask the user how many jelly beans they start with.
# This is not in the while loop, so it only happens once.
bean_count = input ("How many jelly beans do you have to start with? ") # You don't need to change this
bean_count_int = int ( bean_count )# Finish this line. You need to cast the input to an integer -- see the quick reference
# This will have a test that evaluates to true/false 
while ( bean_count_int  > 0 ): 
   bean_eaten = input ("How many beans did you eat?") # Finish this line, ask about beans eaten
   bean_eaten_int = int ( bean_eaten )# Finish this line, cast to int
   bean_count_int = bean_count_int - bean_eaten_int # Finish this line, do some math
   print ("You have " + str (bean_count_int) + " beans left")# Finish this line, report remaining to user, you will need to cast an integer to a string to print it
# AFTER WHILE LOOP
# This is the end of the program. It only happens once, after the while
# loop is completed.
if (bean_count_int == 0 ): 
 print ("You are ALL OUT of jelly beans.")
else:
  print ("You are in jelly bean debt!") 
