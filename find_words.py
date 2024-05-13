from collections import Counter

def findWords(inputString, dictionary):
    """
    Args:
    inputString (str): The string used to form words
    dictionary (list): List of words to check against the input string
    
    Returns:
    list: List of words that can be formed from the input string
    """
    result = []
    # Counter creates a dictionary of the character counts for the string passed in
    char_count = Counter(inputString)
    
    for word in dictionary:
        word_char_count = Counter(word)
        
        # Check if char count in inputString is sufficient for each char in the current word's char count
        if all(char_count[char] >= word_char_count[char] for char in word_char_count):
            result.append(word)
    
    return result

def main():
    result = findWords("ate", ["ate", "eat", "tea", "dog", "do", "god", "goo", "go", "good"])
    assert result == ["ate", "eat", "tea"]
    
    result = findWords("oogd", ["ate", "eat", "tea", "dog", "do", "god", "goo", "go", "good"])
    assert result == ["dog", "do", "god", "goo", "go", "good"]

    result = findWords("lazier", ["a", "air", "hair", "hazy", "i", "lair", "lazy"])
    assert result == ["a", "air", "i", "lair"]

    result = findWords("i", ["air", "hair", "hazy", "lair", "lazy"])
    assert result == []

main()
