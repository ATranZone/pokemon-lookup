import requests


def print_pokemon_data(pokemon_info):
    name = pokemon_info["name"]
    poke_type = pokemon_info["types"]
    moves_set = pokemon_info["learnable moves"]
    print_moves = ""

    if len(poke_type) > 2:
        print_type = (poke_type[0] + "and" + poke_type[1] + "type.")
    else:
        print_type = (poke_type[0] + " type");

    for x in moves_set:
        if x == moves_set[-1]:
            print_moves = print_moves[:-1] + "."
        else:
            print_moves = print_moves + " " + x + ","

    print(f"{name.capitalize()} is a " + print_type + f" Pokemon. \nIt can learn these moves:{print_moves}")


def get_pokemon_data(pokemon_name):
    api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(api_url)

    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_info = {
            "name": pokemon_data["name"],
            "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]],
            "learnable moves": [moves_data["move"]["name"] for moves_data in pokemon_data["moves"]]
        }
        print_pokemon_data(pokemon_info)
    else:
        print("Either that name does not exist or something went wrong!")


def main():
    pokemon_input = input("What Pokemon do you want to look up?\n")
    get_pokemon_data(pokemon_input)


if __name__ == "__main__":
    main()


