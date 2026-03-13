import random
while True:
 choice = input("Girar dado? (S/N): ").lower()
 if choice == "s":
    dado1 = random.randint(1,6)
    dado2 = random.randint (1,2)
    print(f"({dado1}, {dado2})")
 elif choice == "n":
    print("Gracias por jugar!")
    break
 else:
   print("Elección invalida")