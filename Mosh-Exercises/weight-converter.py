# Exercise is to take an input/weight
# And convert it to either Kilograms or Pounds
loop_exit = True

while loop_exit:
    #Take and store user initial input
    weight = float(input("\nWeight: "))

    #Ask for either Kg or Lbs
    weight_unit = input("(K)g or (L)bs: ").lower()

    #Return the converted value
    if weight_unit == "k":
        #Kg to Lbs
        weight_conversion = round(weight * 2.2, 2)
        print("Weight in Lbs: " + str(weight_conversion))
    elif weight_unit == "l":
        #Lbs to Kg
        weight_conversion = round(weight / 2.2, 2)
        print("Weight in Kg: " + str(weight_conversion))

    if exit == True:
        user_quit = input("\nWould you like to (Q)uit: ").lower()

        if user_quit == "q":
            loop_exit = False
            print("Goodbye!\n")
            