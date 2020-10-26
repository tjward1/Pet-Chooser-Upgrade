# Properties
# petID: getPetID(), setPetID()
# petName: getPetName(), setPetName()
# petAge: getPetAge(), setPetAge()
# animalType: getAnimalType(), setAnimalType()
# ownerName: getOwnerName(), setOwnerName()


class Pet:
    # private properties
    __petID: int = 1
    __petName: str = ""
    __petAge: int = 1
    __animalType: str = ""
    __ownerName: str = ""

    # instantiate copy of the class
    def __init__(self,
                 petID,
                 petName,
                 petAge,
                 animalType,
                 ownerName):
        # set all of our properties
        self.setPetID(petID)
        self.setPetName(petName)
        self.setPetAge(petAge)
        self.setAnimalType(animalType)
        self.setOwnerName(ownerName)

    # get and set the petID property
    def getPetID(self) -> int:
        return self.__petID

    def setPetID(self, petID: int) -> None:
        try:
            if petID:
                self.__petID = int(petID)
        except Exception as e:
            print(f"error occurred: {e}")

    # get and set petName property
    def getPetName(self) -> str:
        return self.__petName

    def setPetName(self, petName: str) -> None:
        try:
            if petName:
                self.__petName = petName
        except Exception as e:
            print(f"error occurred: {e}")

    # get and set the petAge property
    def getPetAge(self) -> int:
        return self.__petAge

    def setPetAge(self, petAge: int) -> None:
        try:
            if petAge:
                self.__petAge = int(petAge)
        except Exception as e:
            print(f"error occurred: {e}")

    # get and set the ownerName property
    def getOwnerName(self) -> str:
        return self.__ownerName

    def setOwnerName(self, ownerName: str) -> None:
        try:
            if ownerName:
                self.__ownerName = ownerName
        except Exception as e:
            print(f"error occurred: {e}")

    # get and set the animalType property
    def getAnimalType(self) -> str:
        return self.__animalType

    def setAnimalType(self, animalType: str) -> None:
        try:
            if animalType:
                self.__animalType = animalType
        except Exception as e:
            print(f"error occurred: {e}")
