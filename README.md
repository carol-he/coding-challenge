# Find Words

## Description
This project contains a function `findWords` that takes an input string and a list of words (dictionary). It returns a list of words that can be formed using the characters in the input string.

## High-Level Approach
In order to efficiently check the dictionary for words that can be formed with input string, we must store the character counts somehow to be checked with the character counts of the input string.

Using a dictionary makes this efficient because of the constant time to check for a key in a dictionary. We can use the Counter class in collections to succinctly create a dictionary of character counts for all our words.

The overall runtime of this is $O(w + n*k)$, where $w$ is the length of the input string, $n$ is the number of words in dictionary, and $k$ is the length of each word in dictionary.
