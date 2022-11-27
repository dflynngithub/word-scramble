"""
-- SCRMABLED-STRINGS --
This program accepts a user-specified dictionary file and a list of
strings, then identifies all of the occurences of dictionary words 
(as well as their scrambled permutations) in each string.
Results are printed to an output file.
"""

import click  # Library for input and output
import logging  # Library for error/debug/info logging
from os.path import exists  # Assists us to check whether files exist

# Specify a log file
logging.basicConfig(filename="output/scrmabled_strings.log",
                    encoding="utf-8", level=logging.DEBUG)

# A template for possible errors
dictionary_import_error = "In main: dictionary file does not exist! File name = {dictionary}"
input_import_error = "In main: search string input file does not exist! File name = {input}"
word_match_size_error = "Error in word_matches_in_string: expect search string to be bigger than dictionary word."


def word_matches_in_string(search_string: str, dictionary_word: str) -> bool:
    """
    Determine how many instances of a dictionary word (as well as its scrambled
    permutations) exist in a given search string.
    """

    # Initialise a counter that tracks the number of matches
    matches = 0

    # Length of search string and of dictionary word
    N = len(search_string)
    M = len(dictionary_word)

    # Input validation: the search string must be at least as big as the dictionary word
    if M > N:
        logging.error(word_match_size_error)
        raise Exception(word_match_size_error)

    # Split the search string and dictionary word into letter lists
    string_letters = list(search_string)
    word_letters = list(dictionary_word)

    # Make a frequency array out of the middle of the dictionary word
    A = make_frequency_array(word_letters[1:M-1])

    # Loop over the possible starting points of a matched dictionary word in the string,
    # from the first index to the maximal index which can still fit the dictionary word.
    for i in range(0, N-M+1):
        # Is this current string letter (S1) equal to the first letter of the dictionary word?
        if string_letters[i] == word_letters[0]:
            # Is the Mth-next letter (S2) equal to the last letter of the dictionary word?
            if string_letters[i+M-1] == word_letters[M-1]:
                # Construct a frequency array for the letters between S1 and S2
                B = make_frequency_array(string_letters[i+1:i+M-1])
                # If the frequency arrays are equal, we have a match
                if A == B:
                    matches += 1

    # Even though we have counted the total number of matches so far, the instructions
    # only require that we record whether the dictionary word matches at least once
    return True if matches > 0 else False


def make_frequency_array(letters: list[str]) -> list[int]:
    """
    Map a list of letters (characters within a word) onto a frequency array,
    which counts the number of occurrences of each letter in that word.
    """

    # Initialise an empty frequency array
    freq_array = [0]*26

    # Loop over each letter and update the frequency array,
    # using the in-built 'ord' method and translating by 97
    for letter in letters:
        i = ord(letter)-97
        freq_array[i] += 1

    return freq_array


@click.command()
@click.option("--dictionary", required=True, help="Name of the dictionary file.")
@click.option("--input", required=True, help="A series of strings to search for words within.")
def main(dictionary, input):  # Main program

    # Error handling in case the nominated dictionary file does not exist
    if (not exists(dictionary)):
        msg = dictionary_import_error.format(dictionary=dictionary)
        logging.error(msg)
        raise Exception(msg)

    # Import the dictionary file into an array of words
    logging.info("Importing dictionary file "+dictionary)
    with open(dictionary) as f:
        dictionary_words = f.read().splitlines()

    # The number of dictionary words
    D = len(dictionary_words)
    logging.info("Number of dictionary words: D = "+str(D))

    # Error handling in case the nominated dictionary file does not exist
    if (not exists(input)):
        msg = input_import_error.format(input=input)
        logging.error(msg)
        raise Exception(msg)

    # Import the search string input file into an array of words
    logging.info("Importing search string input file "+input)
    with open(input) as f:
        search_strings = f.read().splitlines()

    # The number of search strings
    T = len(search_strings)
    logging.info("Number of search strings: T = "+str(T))

    # Initialise an array of results
    results = [0]*T

    # Find the number of scrambled dictionary word matches for each search string
    for idx, search_string in enumerate(search_strings):
        for dictionary_word in dictionary_words:

            # Test whether this dictionary word is contained in the search string
            is_match = word_matches_in_string(search_string, dictionary_word)

            # For each successful match, add one to the counter
            results[idx] += int(is_match)

    # Having identified all matching dictionary words for each search string,
    # print results to an output file
    logging.info("Finished matching search strings with dictionary words")
    with open("output/results.txt", "w") as r:
        for idx, matches in enumerate(results):
            r.write("Case #"+str(idx+1)+": "+str(matches))


# When to actually run the main program
if __name__ == "__main__":
    main()
