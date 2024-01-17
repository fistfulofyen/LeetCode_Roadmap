from collections import *
from itertools import groupby

def groupAnagrams(strs):
    anagram_groups = defaultdict(list)

    # Iterate through each string in the input array
    for s in strs:
        # Sort the characters of the string and use it as a key for grouping
        sorted_str = "".join(sorted(s))
        anagram_groups[sorted_str].append(s)

    # Convert the values of the dictionary into a list to get the grouped anagrams
    grouped_anagrams = list(anagram_groups.values())
    return grouped_anagrams

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagrams(strs)