import random
random_number = random.randint(1, 5)                                                      #it will generate a random number between 1 and 5
no_of_tries = 0                                                                           #Variable to store the number of tries

# print(random_number)                                                                      #Printing the random number generated for testing purpose


while True:
    user_entry = int(input("Enter a number between 1 and 5: "))                        #Asking the user to enter a number between 1 and 100
    no_of_tries += 1                                                                      #Incrementing the number of tries by 1
    if user_entry == random_number:                                                       #Checking if the user entered number is equal to the random number                                  
        print("Wohoo!, You guessed the correct number in", no_of_tries, "tries")
        break
    else:
        print("That's incorrect. Please Try again.")                                                 #Printing a message to try again
        continue
    

