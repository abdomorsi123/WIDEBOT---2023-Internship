class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class SpellChecker:
    def __init__(self):
        self.root = TrieNode()
    
    def build_dictionary(self, dictionary):
        for word in dictionary:
            self.insert_word(word)


    def insert_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True


    def find_nearest_4_words(self, word):
        def dfs(node, path):
            if len(found_words) >= 4:
                return
            if node.is_end_of_word:
                found_words.append("".join(path))
            for char, child in node.children.items():
                dfs(child, path + [char])

        found_words = []
        node = self.root
        for char in word:
            if char not in node.children:
                return found_words
            node = node.children[char]

        # Traverse the trie to find words starting from the current node

        dfs(node, list(word))
        return found_words

    def add_word_to_dictionary(self, word):
        self.insert_word(word)

if __name__ == "__main__":

    spell_checker = SpellChecker()

    with open('dictionary.txt', 'r') as file:
        dictionary = [line.strip() for line in file]

    spell_checker.build_dictionary(dictionary)

    # Test the Spell Checker

    choices = ["Add new word", "Test a word\n"]

    print("What do you want to do ?\n")
    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")

    try:
        user_choice = int(input("Enter the number of your choice: \n"))
    except ValueError:
        print("Invalid input. Please enter a number. \n")
    

    if user_choice < 1 or user_choice > len(choices):
        print("Invalid choice. Please select a number within the given range. \n")


    if user_choice == 1:
        input_word = input("Enter the word you want to add: \n")
        spell_checker.add_word_to_dictionary(input_word) 
        print(f"the word \"{input_word}\" added. \n")
    else:
        input_word = input("Enter the word you want to test: \n")
        if input_word in dictionary:
            print(f"{input_word} is in the dictionary. \n")
        else:
            nearest_words = spell_checker.find_nearest_4_words(input_word)
            print(f"{input_word} is not in the dictionary.")
            print(f"Nearest words: {nearest_words} \n")