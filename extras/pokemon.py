def longest_pokemon_sequence():
    pokemons = "audino bagon baltoy banette bidoof braviary bronzor "\
        "carracosta charmeleon cresselia croagunk darmanitan deino "\
        "emboar emolga exeggcute gabite girafarig gulpin haxorus "\
        "heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune "\
        "landorus ledyba loudred lumineon lunatone machamp magnezone "\
        "mamoswine nosepass petilil pidgeotto pikachu pinsir "\
        "poliwrath poochyena porygon2 porygonz registeel relicanth remoraid "\
        "rufflet sableye scolipede scrafty seaking sealeo silcoon "\
        "simisear snivy snorlax spoink starly tirtouga trapinch treecko "\
        "tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"

    original_list = pokemons.split(' ')
    pokemon_list_options = []
    longest_list = []

    def pokemon_starts_with(last_character, poke_list):
        """ Finds the next index from the list which fulfills the requirement.

        Args:
            last_character (str): The last character to compare with the
            first of every item in the poke_list
            poke_list (list): The remaining unique elements in the array
            that can be compared against the last character

        Returns:
            int/boolean: int if it finds an item in "poke_list" that starts
            with the "last character" or boolean, False, when it doesn't
            find a match.
        """
        for index, name in enumerate(poke_list):
            if name.startswith(last_character):
                return index
        return False

    def generate_list(first_name, poke_list):
        """Function to create the temporal list that is started by the
        first_name provided

        Args:
            first_name (str): First element on the list
            poke_list (list): A copy of the original array of names which
            will be modified with every iteration.

        Returns:
            list: The resulting list of pokemon names in the order that
            are inserted to the list.
        """
        index = pokemon_starts_with(first_name, poke_list)
        result = []
        # getting the last character of the last element in the list
        while index:
            previous = poke_list[index]
            poke_list.pop(index)
            result.append(previous)
            last_character = previous[-1]

            index = pokemon_starts_with(last_character, poke_list)
        return result

    for pokemon_name in original_list:
        temp_list = generate_list(pokemon_name, original_list[:])

        if len(temp_list) > len(longest_list):
            longest_list = temp_list
        elif len(temp_list) == len(longest_list):
            if len(pokemon_list_options) > 0:
                if len(pokemon_list_options[0]) < len(temp_list):
                    pokemon_list_options = [temp_list]
                else:
                    pokemon_list_options.append(temp_list)
            else:
                pokemon_list_options = [temp_list]

    pokemon_list_options.append(longest_list)

    print("Se encontraron las siguientes {} secuencias como las más largas posibles a partir de la lista provista: ".format(len(pokemon_list_options)))

    for current_list in pokemon_list_options:
        print(", ".join(current_list))


if __name__ == '__main__':
    longest_pokemon_sequence()
