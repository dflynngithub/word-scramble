# Running the `scrmabled_strings` program

This repository contains a Python file which reads a dictionary and an input file (which contains a list of search strings), determines how many of the dictionary words (and their scrambled variants) match to each search string, and saves the results to an output file. The example which was outlined in the instructions has been included in the repsitory as well.

To run the program directly, navigate to the root directory and run the command:

```
python3 src/scrmabled_strings.py --dictionary input/dictionary.inp --input input/input.inp
```

When finished, the results will be stored in `output/results.txt`.

If you'd like to change the dictionary or the list of search strings, simply upload those files to the `input` directory and then update the command appropriately.

I have provided a Dockerfile as well, just because that looked like a pretty easy stretch goal to meet! I haven't built it, because the instructions say that you're happy to do so. I think you'll find everything you need in `Dockerfile` and `requirements.txt`, in the relative root directory.

# Discussion of the program

In reading the Google Code Competition problem and analysis, I realised that the modular arithmetic-based solution scheme is a bit out of scope for the task at hand. (And what's more, their specified parameters haven't been supplied here.)

So instead, I opted to meet somewhere in the middle, and took care to mitigate possible cases of poor scaling by:

-   Considering one search string `S` and one dictionary word `D` at a time.
-   Running across most letters in `S` and checking whether they matched the first letter of `D`.
-   If they do match, check whether the appropriate later letter in S matched the last letter of `D`.
-   Only check for a full dictionary word match if both of those conditions pass.
-   Constructing a frequency array for the middle letters in `D` and comparing it to a similar array for the candidate letters in `S` -- if the two are equivalent, then at least one scrambled permutation exists.

Areas for possible improvement:

-   Early-exit the pattern-matching algorithm when a single match has been found, because we're not explicitly asked to find the number of matches per dictionary word.
-   Parallelise the process, so that processors each recieve a search string and send back the number of dictionary word matches.
-   Pursue a character-to-integer mapping approach with modular arithmetic and chosen parameters, like the Google Code Competition suggests.
-   Additional logging which provides metadata about how many matches have been found, and potentially the memory and computer time costs associated with the program.
-   More data validation around the program requirements, eg. check that any dictionary word contains 2-105 letters.

There are some extra little tools that I've wielded here, which are fairly standard:

-   The `click` library, which allows me to specify the dictionary and search string input file directly within the command line, and its usage comes with some `@` decorators which simply pipe the recieved options into `main`.
-   The `logging` library, which comes for free with my Python installation, and which allows me to log info, debug and error information to an external file called `output/scrmabled_strings.log`.
-   The `os.path` library, which just allows me to check whether the input files actually exist and then handle errors accordingly.

I chose not to write unit tests here. (I was slightly perplexed by the first item under `Deliverable` in the instructions, but I suspect that refers to Pepperstone's internal tests that check the functionality of my program.) While I did _start_ to write unit tests, I soon realised that my logging and exception handling basically performed the same job for this fairly straightforward scenario. Hopefully I haven't interpreted the situation incorrectly!
