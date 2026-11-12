def say_hello(name=None):
    if name:
        print(f"Hallo, {name}!")
    else:
        print("Hallo, Welt!")

say_hello()
say_hello("Anna")
say_hello(name="Ben")
say_hello("")
say_hello("Jonathan")
