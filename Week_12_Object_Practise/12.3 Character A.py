"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""

class Character:
    # TODO: the class implementation goes here.
    def __init__(self, name):
        """
        Create character.
        :param name: name of character
        """
        self.__name = name
        self.__all_items = []
        
    def get_name(self):
        return self.__name

    def give_item(self, item):
        self.__all_items.append(item)

    def has_item(self, item):
        return item in self.__all_items
    
    def how_many(self, item):
        count = 0
        for items in self.__all_items:
            if items == item:
                count += 1
        return count

    def remove_item(self, item):
        self.__all_items.remove(item)
    
    def printout(self):
        print(f"Name: {self.get_name()}")
        printed_items = []
        # loop all items
        for item in sorted(self.__all_items):
            # check if item already counted
            if item not in printed_items:
                count = 0
                # count all of not printed item
                for i in self.__all_items:
                    if i == item:
                        count +=1
                printed_items.append(item)
                print(f"  {count} {item}")
        if len(printed_items) == 0:
            print(f"  --nothing--")
            
def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
