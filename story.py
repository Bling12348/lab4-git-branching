def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")
        print("")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("You pull on the sword and feel a tingling sensation in your hand.")
    print("After a strong tug it comes loose!")
    print("A large dragon names Gorlock flies overhead")
    print("Gorlock swoops down and breathes fire on you but is ineffective against your new sword.")
    print("With a single swing of your sword you defeat Gorlock")
    print("The local pesants cheer for you and give you a beer")


def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

if __name__ == "__main__":
    intro()