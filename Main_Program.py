#Main Menu


def main():
    print("DATA STRUCTURE CALCULATOR")

    print("List of Data Structures")

    print("1. List\n2. Tuple\n3. Set\n4. Dictionary\n")
    option = int(input("Please select any one Data Structure: "))
    while option not in range(1,5):
        option = int(input("Enter the correct number to select Data Structure: "))

    if option == 1:
        import list_operations as li
        li.operations()
    elif option == 2:
        import tuple_operations as tup
        tup.operations()
    elif option == 3:
        import set_operations as se
        se.operations()
    elif option == 4:
        import dict_operations as di
        di.operations()
main()







