import validate
import datetime

# This is the dictionary to store data from the text file "stock.txt"
stock_dict = {}


def rent_costume():
    """All the operations of renting costume is done within this function"""
    
    # This is used to count the number of data in dictionary
    count = 0

    while (True):
        global stock_dict
        print("_"*60)
        print("Id\tCostume Name\tBrand\tPrice\tQuantity")
        print("_"*60)

        file = open("stock.txt", "r")

        # read all data from a file
        costume_data = file.read()

        # spliting the number of string operations according to new line and put them in a list
        costume_data = costume_data.split("\n")

        # This while loop is used to remove empty string
        while ("" in costume_data):
            costume_data.remove("")

        count = 0

        for i in range(len(costume_data)):

            # for checking empty list
            if costume_data[i] != []:
                count = count+1
                stock_dict[count] = costume_data[i].split(",")

        for key, value in stock_dict.items():
            print(key, end="\t")
            for i in value:
                print(i, end="\t")
            print("\n")
        print("_"*60)
        print("\n")

        while (True):
            try:
                option = int(input("Enter the id of costume: "))
                break

            except:
                print("\nProvide the value in int datatype!\n")

        if option > 0 and option <= count:
            print("Costume ID is ", option)

            print("++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\tCostume is available")
            print("++++++++++++++++++++++++++++++++++++++++++++++++\n")

            while (True):
                try:
                    qty = int(input("Enter the quantity of costume: "))
                    break

                except:
                    print("\nProvide the value in int datatype!\n")

            validate.quantity_validate(qty, option)
            break

        else:
            print("\n++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\tPlease provide a valid Costume ID!!")
            print("++++++++++++++++++++++++++++++++++++++++++++++++\n")


def stock_update():
    """Write the updated data in the text file."""
    print("Stock updated!")
    f = open("stock.txt", "w")

    for value in stock_dict.values():
        f.write(",".join(value))
        f.write("\n")
    f.close()
