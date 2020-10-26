import pymysql.cursors
from creds import *


# user editing pet name function
def editPetName(petEditID, editName):
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
            sqlUpdateName = """
                    update
                        pets
                    set
                        pets.name = %s
                    where
                        pets.id = %s;
                    """
            # execute the name update
            cursor.execute(sqlUpdateName, (f'{editName}', petEditID))

            # commit updated pet name to the database
            myConnection.commit()

    # If there is an exception, show what that is
    except Exception as e:
        print(f"An error has occurred.  Exiting: {e}")
        print()

    # Close connection
    finally:
        myConnection.close()


# user editing pet age function
def editPetAge(petEditID, editAge):
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
            # our second sql statement, easy to read
            sqlUpdateAge = """
                               update
                                   pets
                               set
                                   pets.age = %s
                               where
                                   pets.id = %s;
                               """
            # execute the age update
            cursor.execute(sqlUpdateAge, (editAge, petEditID))

            # commit updated pet age to the database
            myConnection.commit()

    # If there is an exception, show what that is
    except Exception as e:
        print(f"An error has occurred. Exiting: {e}")
        print()

    # Close connection
    finally:
        myConnection.close()

