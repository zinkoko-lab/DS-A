from enum import Enum
from chained_hash import ChainedHash

Menu = Enum("Menu", ["Add", "Remove", "Search", "Dump", "End"])


def select_menu() -> Menu:
    """Select the menu."""
    s = [f"({m.value}){m.name}" for m in Menu]
    while True:
        print(*s, sep=" ", end="")
        n = int(input(" : "))
        if 1 <= n <= len(Menu):
            return Menu(n)


hash = ChainedHash(13)

while True:

    match menu := select_menu():

        case Menu.Add:
            key = int(input("key: "))
            value = input("value: ")
            if not hash.add(key, value):
                print("Failed to add!")

        case Menu.Remove:
            key = int(input("key: "))
            if not hash.remove(key):
                print("Failed to remove!")

        case Menu.Search:
            key = int(input(f"key: "))
            t = hash.search(key)
            if t is not None:
                print(f"そのキーをもつ値は{t}です。")
            else:
                print("該当するデータはありません。")

        case Menu.Dump:
            hash.dump()

        case _:
            break


# print(Menu(1))  # Menu.Add
# print(Menu(2))  # Menu.Remove
# print(Menu(3))  # Menu.Search
# print(Menu(4))  # Menu.Dump
# print(Menu(5))  # Menu.End
