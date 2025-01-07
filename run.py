#!/usr/bin/python
import difflib
from wallet import Wallet

def search_text_file(file_path, query, similarity_threshold=0.2):
    """
    Searches a text file for lines resembling the input query.

    Args:
        file_path (str): Path to the text file.
        query (str): The input string to search for.
        similarity_threshold (float): A threshold between 0 and 1 for line similarity.

    Returns:
        list: A list of lines resembling the query.
    """
    results = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                ### Calculate similarity using difflib
                similarity = difflib.SequenceMatcher(None, query, line).ratio()
                if similarity >= similarity_threshold:
                    results.append((line, similarity))
        ### Sort Lines by Similarity
        results.sort(key=lambda x: x[1], reverse=True)
    
    except FileNotFoundError:
        print(f"Error: The line '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return results


def help_menu():
    """ 
    Provides user with help about Bookcoin.

    Args: None

    Returns: Help message

    """
    print("""\n

### HELP ###

Not sure how this works? Well, each BookCoin is a classic work of literature, which
is then made up of PageCents! 

PageCents are the number of pages within the literature in question, For instance:

Moby Dick (Herman Melville) = 1 BookCoin & 672 PageCents
Inferno (Dante) = 1 BookCoin & 224 PageCents

Bigger books are more valuable! There are 1407 BookCoins in total corresponding to 
the complete list of Penguin Classics. \n

                """)

def menu():
    """
    Prints out the menu for the BookCoin example app
    """
    print("""\n
 ################################################################################
                                                                 ______ _ ______
 #####  ###### ###### #  #  ######  ######  ####### ##     #    |      | |      |
 #    # #    # #    # # #   #       #    #     #    # #    #    |~~~~~~| |~~~~~~|
 ###### #    # #    # ##    #       #    #     #    #  #   #    |~~~~~~| |~~~~~~|
 #    # #    # #    # ##    #       #    #     #    #   #  #    |~~~~~~| |~~~~~~|
 #    # #    # #    # # #   #       #    #     #    #    # #    |~~~~~~| |~~~~~~|
 ###### ###### ###### #  #  ######  ######  ####### #     ##    |______|_|______|

 ################################################################################

 Welcome dear user to your BookCoin wallet! 

 #### MENU ####

 Please select from the following be typing to number:

 1 What is this all about? (Help)

 2 Create New Wallet (Start your BookCoin Journey!)

 3 Search For a BookCoin

 4 Check incoming BookCoins\n

    """)
    try:
        UserSelect = int(input("Please Select Now: "))
        if UserSelect == 1:
            help_menu()
            back_to_menu = str(input("\nMAKES SENSE RIGHT? CONTINUE? [Y/N]:"))
            if back_to_menu == "y" or back_to_menu == "Y":
                menu()
            else:
                help_menu()

        elif UserSelect == 2:
            ### Generate a new key pair
            private_key, public_key = Wallet.generate_keys()

            ### Export the public and private keys
            public_key_pem = Wallet.export_key(public_key, key_type='public')
            private_key_pem = Wallet.export_key(private_key, key_type='private')

            ### Print the exported keys
            print("Public Key (PEM format):")
            print(public_key_pem)
            print("\nPrivate Key (PEM format):")
            print(private_key_pem)

        elif UserSelect == 3:
            file_path = "BookCoins_List.txt" 
            search_list = str(input("SEARCH: "))
            matches = search_text_file(file_path, search_list)
            if matches:
                print("Matching lines:")
                for line, similarity in matches:
                    print(f"Line: {line} (Similarity: {similarity:.2f})")
            else:
                print("No matching lines found.")
                menu()

        elif UserSelect == 4:
            print("Not finished")

    except ValueError as err:
        "Invalid try again"
menu()
