
import csv
import random
pokemons = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])

# print(pokemons)

print("Pokemon list command:")

while True:
    print("1. Get pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by text in name")
    print("5. Search by length of name")
    print("6. Izdrukāt pirmos 10 pokemonus")
    print("7. Izdrukāt pēdējos 10 pokemonus")
    print("8. Izdrukāt 10 pokemonus")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        pokemonindex = input("Ieraksti skaitli un tev izdos pokemonu kurš bija zem šī skaitļa: ")
        print("Tu izvēlējies: " + pokemonindex)
        print(pokemons[int(pokemonindex)])
        pass
    elif choice == '2':
        pokemons.sort()
        print(pokemons)
        pass
    elif choice == '3':
        pokemons.sort(reverse = True)
        print(pokemons)
        pass
    elif choice == '4':
        pokeindex = []
        name = input("Uzraksti burtu(s) un tev parādīs pokemonus kuri sākās ar šo burtu vai tas burts ir iekļauts to pokemonu vārdā: ")
        for pokemon in pokemons:
            if name in pokemon:
                pokeindex.append(pokemon)

        print("Rekur pokemoni kuri sākās ar burtu/burtiem", str(name), pokeindex)
        pass
    elif choice == '5':
        lengthpokemons = []
        pokemonsearch = int(input("Ieraksti cik daudz burtu ir tavā pokemonā: "))
        lengthpokemons = [pokemon for pokemon in pokemons if len(pokemon) == pokemonsearch ]
        print("Rekur pokemoni ar šo burtu skaitu", lengthpokemons)
        pass
    elif choice == '6':
        print(pokemons[:10])
        pass
    elif choice == '7':
        print(pokemons[-10:])
        pass
    elif choice == '8':
        start = 0
        print(pokemons[start:start+10])
        choice2 = input("n/q: ")
        while choice2 == "n":
            start += 10
            print(pokemons[start:start+10])
            choice2 = input("n/q: ")
    if choice2 == '9':
        random_pokemons = random.sample(pokemons, 10)
        print(random_pokemons)
    elif choice2 == 'q':
        pass
    elif choice == '9':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 6")

    print("==========================")
