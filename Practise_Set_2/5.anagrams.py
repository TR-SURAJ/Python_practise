# Two words are anagrams if they have the same characters with the same frequencies.

def groupAnagrams(strs):

    anagram_groups = {}

    for s in strs:
        sorted_str = ''.join(sorted(s))

        if sorted_str in anagram_groups:
            anagram_groups[sorted_str].append(s)
        else:
            anagram_groups[sorted_str] = [s]

    return list(anagram_groups.values())

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))