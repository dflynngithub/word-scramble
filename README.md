# Running the `scrmabled_strings` program

This repository contains a Python program which reads a dictionary and an input file which contains a list of search strings, then determines how many of the dictionary words (and their scrambled variants) match to each search string, and saves the results to an output file.

The example which was outlined in the instructions has been included in the repository as well, just to have everything in one place.

To run the program directly, you may first need to install a Python library:

```
pip3 install click
```

Then you should be able to navigate to the root directory and run the command:

```
python3 src/scrmabled_strings.py --dictionary input/dictionary.inp --input input/input.inp
```

When finished, the results will be stored in `output/results.txt`.

If you'd like to alter the dictionary or the list of search strings, simply upload some new files to the `input` directory and then update the CLI command appropriately.

# Discussion

In reading the Google Code Competition problem and analysis (detailed in the `docs` directory), I realised that the modular arithmetic-based solution scheme is a bit out of scope for the task at hand. (And what's more, their specified parameters haven't been supplied here.)

So instead, I opted to meet somewhere in the middle, and took care to mitigate possible causes of poor scaling with the following strategy:

-   Consider one search string `S` and one dictionary word `D` at a time.
-   Run over all letters in `S` which could begin a full dictionary word `D` and check whether they match the first letter of `D`.
-   If they do match, check whether a supplementary letter in `S` (determined by the length of `D`) matches the last letter of `D`.
-   Only check for a full dictionary word match if both of those conditions pass.
-   Construct a frequency array for the middle letters in `D` and compare it to a similar array for the candidate letters in `S` -- if the two are equivalent, then at least one scrambled permutation is a match.

There are some extra little tools that I've wielded here, which are fairly standard:

-   The `click` library, which allows me to specify the dictionary and search string input file directly within the command line, and its usage comes with some `@` decorators which simply pipe the recieved options into `main`.
-   The `logging` library, which comes for free with my Python installation, and which allows me to log info, debug and error information to an external file called `output/scrmabled_strings.log`.
-   The `os.path` library, which just allows me to check whether the input files actually exist and then handle errors accordingly.

Areas for possible improvement:

-   When one word `D` matches a given `S`, early-exit the pattern-matching algorithm, because we're not explicitly asked to find the number of matches per dictionary word. (This feature is buried in the code, if you'd like to change the rules around a little bit.)
-   Parallelise the process, so that processors each recieve a search string and the full dictionary, and are asked to return the number of dictionary word matches.
-   Pursue a character-to-integer mapping approach with modular arithmetic and chosen parameters, like the Google Code Competition suggests. (I'm not so sure about this one -- I'm guessing integer overflow limits are what set the 105 character limit provided in the documentation.)
-   Additional logging which provides metadata about how many matches have been found, and potentially the memory and computer time costs associated with the program.
-   More data validation around the program requirements, eg. check that any dictionary word contains 2-105 letters.

# Stretch goals

-   I've provided a Dockerfile for this program, just because that looked like a pretty easy stretch goal to meet! I haven't built it, because the instructions say that you're happy to do so. I think you'll find everything you need in `Dockerfile` and `requirements.txt`, in the relative root directory.
-   In a two-birds-one-stone maneuver, I've just attached this README directly to the Git repository, which should serve as enough documentation.
-   Logging for general info and errors.
-   Error handling and exception raising, which can usually be found alongside the logging.
-   I chose not to write unit tests here. (I was slightly perplexed by the first item under `Deliverable` in the instructions, but I suspect that refers to Pepperstone's internal tests that check the functionality of my program.) While I did _start_ to write unit tests, I soon realised that my logging and exception handling basically performed the same job for this fairly straightforward scenario. Hopefully I haven't interpreted the situation incorrectly!
