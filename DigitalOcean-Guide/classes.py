class Shark:
    #class variable
    animal_type = "fish"
    habitat = "ocean"

#constructor and instance variables
    def __init__(self, name, age, hat):
        self.name = name
        self.age = age
        self.hat = hat

    def swim(self):
        print(self.name + " is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome.")

    def wearing_hat(self):
        print(self.name + " is wearing a " + self.hat)

def main():
    sammy = Shark("Sammy", 10, "Cowboy")
    sammy.swim()
    sammy.wearing_hat()
    stevie = Shark("Stevie", 5, "Beanie")
    stevie.be_awesome()
    stevie.wearing_hat()

    print("Stevie and Sammy have a combined age of: " + str(stevie.age + sammy.age))
    print ("Stevie and Sammy live in the " + sammy.habitat)
if __name__ == "__main__":
    main()