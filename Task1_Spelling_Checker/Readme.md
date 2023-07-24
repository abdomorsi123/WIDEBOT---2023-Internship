## Time and Space Complexity:

### Building the trie (Operation 1):
- Time Complexity: O(N * M), where N is the number of words in the dictionary and M is the average length of a word.
- Space Complexity: O(N * M), for storing the trie nodes and characters.

### Finding nearest words (Operation 2):
- Time Complexity: O(M * 26^M), where M is the length of the input word. In the worst case, we explore all possible variations of the word.
- Space Complexity: O(1), as we only store the nearest 4 words.

### Adding a word to the dictionary (Operation 3):
- Time Complexity: O(M), where M is the length of the word.
- Space Complexity: O(M), for storing the new word in the trie.
