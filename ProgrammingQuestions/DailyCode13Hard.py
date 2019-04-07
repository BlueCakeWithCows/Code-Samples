"""Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb"."""

def longestSubstring(s, k):
    n = len(s)
    longest = 0
    current_substring_end = n
    current_substring = "";
    current_distinct_chars = set([])
    for i in reversed(range(n)):
        current_substring = s[i] + current_substring
        current_distinct_chars.add(s[i])
        while len(current_distinct_chars) > k:
            last_char = current_substring[len(current_substring)-1]
            current_substring = current_substring[0:len(current_substring)-1]
            if not last_char in current_substring:
                current_distinct_chars.remove(last_char)
        
        longest = max(longest, len(current_substring))
        
    return longest
        

if __name__ == "__main__":
    assert longestSubstring("abcba", 2) == 3
    assert longestSubstring("abcba", 3) == 5
    