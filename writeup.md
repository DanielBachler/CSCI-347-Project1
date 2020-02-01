# Author: Dan Bachler

# Dataset
[Poker Hand Dataset](https://archive.ics.uci.edu/ml/datasets/Poker+Hand)

# Part 1
 This dataset was used for a research paper written by Robert Cattral and Franz Oppacher about evolutionary data mining with automatic rule generation.  There are 11 attributes for each entry and 1,025,010 entries.  Of the 11 attributes, 6 are ordinal (categorical) and 5 are numerical, there are 5 ordinal variables that should be one hot encoded, those are the face values of each of the 5 cards in a poker hand.  MISSING VALUES.  This dataset is interesting to me since it shows how rare certain hands in poker are, despite those hands seemingly appearing for a big win quite often.  Since there are 2 attributes for each of the 5 cards in a poker hand those are not nessicarily as useful as the single ordinal variable about the usefulness of said hand.

 # Part 2