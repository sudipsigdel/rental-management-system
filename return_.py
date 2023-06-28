import rent
import datetime

return_dict = {}
temp_dict = {}


def item_access():
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
            rent.stock_dict[count] = costume_data[i].split(",")


def return_costume():
    """All the operations of returning costume is done within this function"""

    totalprice = 0
    loop = True
    while loop == True:

        try:
            name = input("Enter your name: ")
            id = input("Enter your invoice id: ")
            rented = "bill/rented-"+name+id + ".txt"

            file = open(rented, "r")
            item_access()

            global return_dict
            global temp_dict
            print("\nItem you have rented!")
            print("_"*60)
            print("Id\tCostume Name\tBrand\tPrice\tQuantity  Amount")
            print("_"*60)

            # read all data from a file
            costume_data = file.read()

            # spliting the number of string operations according to new line and put them in a list
            costume_data = costume_data.split("\n")

            count = 0
            for i in range(6, len(costume_data)-1):
                count = count+1
                return_dict[count] = costume_data[i].split(",")

            countText = 0
            for data in costume_data:
                countText += 1
                temp_dict[countText] = data.split(",")

            for key, value in return_dict.items():
                for i in value:
                    print(i, end="\t")
                print("\n")
            print("_"*60)
            print("\n")

            while True:
                try:
                    costumeid = int(
                        input("Enter the Id of the costume you want to return: "))
                    break
                except:
                    print("Invalid Id!")

            for key in return_dict.keys():
                if costumeid == int(return_dict[key][0]):
                    while True:
                        try:
                            costumequantity = int(
                            input("Enter the quantity of the costume you want to return: "))
                            break
                        except:
                            print("enter valid data")

                    if costumequantity <= int(return_dict[key][4]):
                        fine = int(input("Enter the no of days you are late: "))
                        if (fine == 0):
                            fineamount = 0
                        else:
                            fineamount = float(return_dict[key][3].strip().strip(
                                "$")) * fine + float(5 * fine)

                        rent.stock_dict[costumeid][3] = str(
                            int(rent.stock_dict[costumeid][3]) + costumequantity)
                        return_dict[key][4] = str(
                            int(return_dict[key][4]) - costumequantity)
                        totalprice = float(return_dict[key][3].strip().strip(
                            "$"))*costumequantity + fineamount
                        rent.stock_update()
                        print(rent.stock_dict)

                    text_update(name, id)
                    generate_bill(name, costumeid, costumequantity, totalprice)
                    txt_file(name, costumeid, costumequantity, totalprice)
                    loop = False
        except:
            print("File not found")


def text_update(name, id):
    rented = "bill/rented-"+name+id+".txt"
    file = open(rented, "w")

    file.write(temp_dict[1][0])
    file.write("\n")
    file.write(temp_dict[2][0])
    file.write("\n")
    file.write(temp_dict[3][0])
    file.write("\n")
    file.write(temp_dict[4][0])
    file.write("\n")
    file.write(temp_dict[5][0])
    file.write("\n")
    file.write(temp_dict[6][0])
    file.write("\n")
    for key in return_dict.keys():
        join = ",".join(return_dict[key])
        file.write(join)
        file.write("\n")
    file.write(temp_dict[len(temp_dict)][0])


def generate_bill(name, returnId, quantity, totalprice):
    """All the operations of bill generation is done within this function"""
    item_access()

    dt = datetime.datetime.now()
    y = str(dt.year)
    m = str(dt.month)
    d = str(dt.day)
    h = str(dt.hour)
    min = str(dt.minute)
    sec = str(dt.second)

    newdate = "Date of Rent: " + y + "-" + m + "-" + d
    newtime = "Time of Rent: " + h + ":" + min + ":" + sec

    print("\nBill Generated!")
    print("_"*60)
    print("\t\t\t\t", newdate)
    print("\t\t\t\t", newtime)
    print("Name of Customer: ", name)
    print("_"*60)

    print("ID\tCostume Name\tBrand\tPrice\tQuantity")
    print("_"*60)

    print(returnId, "\t", rent.stock_dict[returnId][0], "\t", rent.stock_dict[returnId]
          [1], "\t", rent.stock_dict[returnId][2], "\t", quantity)

    print("_"*60)
    print("\t\t\t\t    Total Price = $", totalprice)


def txt_file(name, returnId, quantity, totalprice):
    """All the operations of writing details from bill in text file is done within this function"""
    templist = []

    dt = datetime.datetime.now()
    y = str(dt.year)
    m = str(dt.month)
    d = str(dt.day)
    h = str(dt.hour)
    min = str(dt.minute)
    sec = str(dt.second)

    newdate = y + "-" + m + "-" + d
    newtime = h + ":" + min + ":" + sec

    randomvalue = y+m+d+h+min+sec
    save = "bill/returned-"+name+randomvalue + ".txt"

    file = open(save, "w")
    file.write("Bill Details")
    file.write("\n")
    file.write("_"*50)
    file.write("\n")
    file.write(newdate)
    file.write("\n")
    file.write(newtime)
    file.write("\n")
    file.write(name)
    file.write("\n")
    file.write(randomvalue)
    file.write("\n")

    templist.append(str(returnId))
    templist.append(str(quantity))
    templist.append(str(totalprice))
    join = ",".join(templist)
    file.write(join)
    file.write("\n")

    file.write("_"*50)
    file.close()
