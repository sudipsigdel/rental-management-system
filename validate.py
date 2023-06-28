import rent
import bill

item_id = []
item_rent = []
item_brand = []
item_price = []
item_quantity = []
item_amount = []


def quantity_validate(q, o):
    """This function validates if the enterd quantity of costume is in the list or not and update accordindly"""

    quantity = q
    option = o

    selected_item = rent.stock_dict[option]

    if quantity > 0:
        if quantity <= int(selected_item[3]):
            print("---------------------------------------------")
            print("\tQuantity is available")
            print("---------------------------------------------\n")

            update_qty = int(selected_item[3])-quantity
            selected_item[3] = str(update_qty)

            global item_id
            global item_rent
            global item_brand
            global item_price
            global item_quantity
            global item_amount

            item_id.append(option)
            item_rent.append(selected_item[0])
            item_brand.append(selected_item[1])
            item_price.append(selected_item[2])
            item_quantity.append(quantity)
            item_amount.append(
                float(selected_item[2].strip().strip("$"))*quantity)

            rent.stock_update()
            print(rent.stock_dict)

            loop = True
            while (loop == True):

                choice = input(
                    "\nDo you want to rent another item (y/n): ")

                if (choice == "y"):
                    rent.rent_costume()

                else:
                    name = input("\nEnter your name: ")
                    bill.generate_bill(name)
                    bill.txt_file(name)

                    item_id = []
                    item_rent = []
                    item_brand = []
                    item_price = []
                    item_quantity = []
                    item_amount = []
                loop = False

        else:
            print(
                "----------------------------------------------------------------------")
            print("\tQuantity provided is greater than what we have in stock")
            print(
                "----------------------------------------------------------------------\n")

            print(rent.stock_dict)
            print("")
            rent.rent_costume()

    else:
        print("----------------------------------------------------------------------")
        print("\tQuantity provided must be greater than 0")
        print("----------------------------------------------------------------------\n")

        print(rent.stock_dict)
        print("")
        rent.rent_costume()
    
