import rent
import return_


def main():
    """The main function through which all program is accessed"""
    # Header text
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("         Welcome to costume rental application")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    # The repeated task to be done is defined under function.
    def option():
        """The function through which all option are accessed"""
        print("\n\nSelect a desirable option")
        print("(1) || Press 1 to rent a costume.")
        print("(2) || Press 2 to return a costume.")
        print("(3) || Press 3 to exit.")

    # This variable is defined so that program can run under loop until terminated
    program = True

    while (program == True):
        # Calling function
        option()

        while (True):
            try:
                # Asking input from user
                z = int(input("Enter a option: "))
                break

            except:
                print("\nPlease provide the valid input!")

        if z == 1:
            print("\n\nLet's rent a costume.")
            rent.rent_costume()

        elif z == 2:
            print("\n\nLet's return a costume.")
            return_.return_costume()

        elif z == 3:
            print("\n\n        Thank You for using our application.")
            break

        else:
            print("\n\nInvalid input!!!!")


main()
