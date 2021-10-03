word_count = {}

with open("poem.txt", "r") as f:
    for line in f:
        tokens = line.split(' ')
        for token in tokens:
            token = token.replace("\n", '')
            if token in word_count:
                word_count[token] += 1
            else:
                word_count[token] = 1

print(word_count)

# No need for creating List and importing all the words in poem in it and making it a count..
# having a '\n' adding to the words(tokens), so using this, to solve this problem,
# gives O(n2) complexity
# if created an array - sending all the elents to it by reading and replacing '\n' with words gives O(n2) complexity
# and again when trying to count the word with the word.count(i) we used to use O(n3) complexity which takes more Space and Time
# Best Way of Approach
