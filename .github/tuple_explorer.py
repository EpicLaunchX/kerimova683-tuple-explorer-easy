def get_items():
        """
        Prompts the user to input a list of items separated by commas,
        converts the input into a tuple, and returns it.
        """
        user_input = input("Enter a list of items separated by commas: ")
        items_list = user_input.split(',')
        items_tuple = tuple(items_list)
        return items_tuple