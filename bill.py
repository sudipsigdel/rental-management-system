import datetime
import validate


def generate_bill(name):
    """All the operations of bill generation is done within this function"""

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

    print("ID\tCostume Name\tBrand\tPrice\tQuantity Amount")
    print("_"*60)

    for i in range(len(validate.item_rent)):
        bill_detail = []
        id = str(validate.item_id[i])
        a = validate.item_rent[i]
        b = validate.item_brand[i]
        c = str(validate.item_price[i])
        d = str(validate.item_quantity[i])
        e = str(validate.item_amount[i])

        bill_detail.append(id)
        bill_detail.append(a)
        bill_detail.append(b)
        bill_detail.append(c)
        bill_detail.append(d)
        bill_detail.append(e)
        print("\t".join(bill_detail))

    print("_"*60)
    print("\t\t\t\t    Total Price = $", sum(validate.item_amount))


def txt_file(name):
    """All the operations of writing details from bill in text file is done within this function"""

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
    save = "bill/rented-"+name+randomvalue + ".txt"

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

    for i in range(len(validate.item_rent)):
        bill_detail = []
        id = str(validate.item_id[i])
        a = validate.item_rent[i]
        b = validate.item_brand[i]
        c = str(validate.item_price[i])
        d = str(validate.item_quantity[i])
        e = str(validate.item_amount[i])

        bill_detail.append(id)
        bill_detail.append(a)
        bill_detail.append(b)
        bill_detail.append(c)
        bill_detail.append(d)
        bill_detail.append(e)
        file.write(", ".join(bill_detail))
        file.write("\n")
    file.write("_"*50)
    file.close()
