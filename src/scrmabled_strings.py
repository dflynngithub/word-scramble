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

dictionary_import_error = "In main: dictionary file does not exist! File name = {dictionary}"
input_import_error = "In main: search string input file does not exist! File name = {input}"


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

    A = make_frequency_array(['a', 'a', 'b', 'd', 'z'])
    print(A)

    # Having identified all matching dictionary words for each search string,
    # print results to an output file
    logging.info("Finished matching search strings with dictionary words")
    with open("output/results.txt", "w") as r:
        for idx, matches in enumerate(results):
            r.write("Case #"+str(idx+1)+": "+str(matches))


# When to actually run the main program
if __name__ == "__main__":
    main()
