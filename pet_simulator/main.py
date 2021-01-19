from pet import Pet, CuddlyPet
from toy import Toy
from treat import ColdPizza, Bacon, VeganSnack
from menu import Menu

# Begin with no pets.
pets = []

main_menu = [   
    "Adopt a Pet",
    "Play with Pet",
    "Feed Pet",
    "View status of pets",
    "Give a toy to all your pets",
    "Do nothing",
    "Give your pets a snack"
]

adoption_menu = [
    "Pet",
    "Cuddly Pet"
]

treat_menu = [
    "ColdPizza",
    "Bacon",
    "VeganSnack"
]

def main():
    app = Menu("Please choose an option", main_menu)
    types = Menu("Please choose a type of pet", adoption_menu)
    treats = Menu("please choose a type of treat", treat_menu)
    while True:
        choice = app.get_user_choice()
        if choice == 1:
            pet_name = input("What would you like the pet name to be?")
            type_choice = types.get_user_choice()
            if type_choice == 1:
                pets.append(Pet(pet_name))
            elif type_choice == 2:
                pets.append(CuddlyPet(pet_name))
            num_pets = len(pets)
            print(f"You now have {num_pets} pets")
        elif choice == 2:
            for pet in pets:
                pet.get_love()
        elif choice == 3:
            for pet in pets:
                pet.eat_food()
        elif choice == 4:
            for pet in pets:
                print(pet)
        elif choice == 5:
            for pet in pets:
                pet.get_toy(Toy())
        elif choice == 6:
            for pet in pets:
                pet.be_alive()
        elif choice == 7:
            print("Please choose your type of treat:")
            treat_choice = treats.get_user_choice
            if treat_choice == 1:
                for pet in pets:
                    pet.eat_treat(ColdPizza())
            elif treat_choice == 2:
                for pet in pets:
                    pet.eat_treat(Bacon())
            elif treat_choice == 3:
                for pet in pets:
                    pet.eat_treat(VeganSnack())

main()