# Exercise is to take an input/weight
# And convert it to either Kilograms or Pounds

#Take and store user initial input
weight = float(input("Weight: "))

#Ask for either Kg or Lbs
weight_unit = input("(K)g or (L)bs: ")

#Return the converted value
if weight_unit.lower() == "k":
    #Kg to Lbs
    weight_conversion = weight * 2.2
    print("Weight in Lbs: " + str(weight_conversion))
elif weight_unit.lower() == "l":
    #Lbs to Kg
    weight_conversion = weight / 2.2
    print("Weight in Kg: " + str(weight_conversion))