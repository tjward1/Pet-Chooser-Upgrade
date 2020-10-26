# Taylor Ward
# Purpose: Connect to mysql and interact with the pets database
# use object oriented programming to make a pet chooser game where the user can edit the pets

from library import editPetName, editPetAge
from pets_class import Pet
import pymysql.cursors
from creds import *

petDict = {}


# list pet id's and pet names for user to choose from
def listOurPets():
    for petID in petDict:
        print(f"[{petID}] {petDict[petID].getPetName()}")
    print("[Q] Quit")


# connect to the database
try:
    myConnection = pymysql.connect(host=hostname,
                                   user=username,
                                   password=password,
                                   db=database,
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)

except Exception as e:
    print(f"An error has occurred.  Exiting: {e}")
    print()
    exit()

try:
    with myConnection.cursor() as cursor:
        # our sql statement, easy to read
        sqlSelect = """
               select pets.id as 'PetID',pets.name as 'PetName',pets.age as 'PetAge',
               types.animal_type as 'AnimalType',owners.name as 'OwnerName' 
               from pets join owners on pets.owner_id = owners.id join types on pets.animal_type_id = types.id;
              """
        # execute query - select
        cursor.execute(sqlSelect)
        # create a temporary pet object so we can put info from database into a dictionary
        for row in cursor:
            tempPet = Pet(petID=row['PetID'],
                          petName=row['PetName'],
                          petAge=row['PetAge'],
                          animalType=row['AnimalType'],
                          ownerName=row['OwnerName'])
            petDict[row['PetID']] = tempPet

except Exception as e:
    print(f"An error has occurred.  Exiting: {e}")
    print()
# close connection
finally:
    myConnection.close()
    # print("Connection to database closed.\n")

choose = 0
while choose == 0:
    # tell the user to choose a pet using its ID number
    print("\nPlease choose a pet from the list below using its ID number!")
    print("You can enter the letter 'Q' to quit.")

    # print all pet ids and names from the dictionary
    listOurPets()

    try:
        # let the user specify their pet by the pet id
        pet = input("I choose pet number: ")
        # user can choose to quit playing at any time
        if pet == 'Q':
            print("Bye! Thanks for playing!")
            break

        # user enters a valid pet ID
        else:
            myPet = petDict[int(pet)]
            # give user all info about the pet chosen
            print(f"You have chosen {myPet.getPetName()}, the {myPet.getAnimalType()}. "
                  f"{myPet.getPetName()} is {myPet.getPetAge()} years old. "
                  f"{myPet.getPetName()}'s owner is {myPet.getOwnerName()}.\n")

            # ask user for next step - keep playing, quit, or edit a pet
            while True:
                choice = input("Would you like to [C]ontinue, [Q]uit, or [E]dit a pet? ")

                # enter Q to leave game
                if choice == 'Q':
                    print("Bye! Game over!")
                    exit()
                # enter C to continue game
                elif choice == 'C':
                    print("\n")
                    break

                # enter E to edit a pet of user's choosing
                elif choice == 'E':
                    print("\n=======Edit Process=======")
                    # the number the user enters is the petID of the pet they want to edit
                    petToEdit = input("Which pet would you like to edit? ")
                    choosePetEditID = petDict[int(petToEdit)]
                    # tell user the name of the pet they chose to edit
                    print(f"You have chosen to edit {choosePetEditID.getPetName()}.\n")
                    print("You can press [Enter] if you would not like to change the name or age"
                          "\nYou can enter 'QUIT' to leave the game during edit process\n")

                    # let user edit the pet's name or press enter to not change it or 'QUIT' to exit game
                    newName = input("New Name: ")
                    if newName == "":
                        print("no change")
                    elif newName.upper() == 'QUIT':
                        print("Bye! Game over!")
                        exit()
                    else:
                        # call editPetName() function from library
                        editPetName(petEditID=choosePetEditID.getPetID(), editName=newName)
                        print(f"pet {choosePetEditID.getPetID()}'s name changed to '{newName}' in database")

                    # let user edit the pet's age or press enter to not change it or 'QUIT' to exit game
                    newAge = input("New Age: ")
                    if newAge == "":
                        print("no change")
                    elif newAge.upper() == 'QUIT':
                        print("Bye! Game over!")
                        exit()
                    elif newAge.isnumeric():
                        # call editPetAge() function from library
                        editPetAge(petEditID=choosePetEditID.getPetID(), editAge=newAge)
                        print(f"pet {choosePetEditID.getPetID()}'s age changed to '{newAge}' in database")
                    else:
                        # if user does not press enter, type 'quit', or a number... invalid input
                        print("Invalid input")
                    break
                else:
                    # remind user to enter a valid choice
                    print("Please enter 'C' or 'Q' or 'E'")

    # catch exceptions so that the user can keep playing until q is entered
    except EOFError as e:
        print(f"Game Over! Thanks for playing!")
        break
    except ValueError as e:
        print(f"Invalid input. Please try again!\n")
    except Exception as e:
        print(f"Error occurred: {e}")


