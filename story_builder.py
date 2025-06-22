# First off we need to open the file
with open("story.txt","r") as f:
    story = f.read()

#create a word list where we store all the words to be changed after filtering
words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i,char in enumerate(story): # enumerate basically gives access to location as well as the character in our story
    if char== target_start:
        start_of_word = i
    if char== target_end and start_of_word!=-1:
        word = story[start_of_word:i+1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("enter a word for "+ word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word,answers[word])


print(story)