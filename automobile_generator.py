from Automobile import Automobile

def main():
    # Create instance of automobiles
    auto1 = Automobile("Honda", "Accord", "23456", 2.4, "Alice", 2024, "Blue")
    auto2 = Automobile("Ferrari", "F-50", "12345", 4.8, "Bob", 2022, "Black")
    # Change some property values

    auto1.set_color("Red")
    auto2.set_owner("Zack")
    auto2.set_color("Green")
    # Create a list of automobiles

    # auto_list = list []
    auto_list: list[Automobile] = []
    auto_list.append(auto1)
    auto_list.append(auto2)

    # print all automobile data
    for auto in auto_list:
        auto.print_data()
    
    print ()
main()
