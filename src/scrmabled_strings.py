"""
-- SCRMABLED-STRINGS --
This program accepts a user-specified dictionary file and a list of
strings, then identifies all of the occurences of dictionary words 
(as well as their scrambled permutations) in each string.
Results are printed to an output file.
"""

import click  # Library for input and output


@click.command()
@click.option("--dictionary", required=True, help="Name of the dictionary file.")
@click.option("--input", required=True, help="A series of strings to search for words within.")
def main(dictionary, input):  # Main program

    # Import the dictionary file into an array of words
    with open(dictionary) as f:
        dictionary_words = f.read().splitlines()

    # Import the search string input file into an array of words
    with open(input) as f:
        search_strings = f.read().splitlines()


# When to actually run the main program
if __name__ == "__main__":
    main()
