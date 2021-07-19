#Read in the text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

#open an exsiting text file to read its content
madLibs = open('madLibsRaw.txt', 'r')

content = madLibs.read()

#To make a list of words in the text file
content = content.split()

#List accumulation for later use
word_list = []

#Iterate through the list to find the word ADJECTIVE, NOUN, VERB and append them in the word_list
for word in content:
    if word == 'NOUN' or word == 'NOUN.' or word == 'NOUN."':
        noun = str(input('Enter a noun:\n'))
        word_list.append(noun)
    elif word == 'ADJECTIVE' or word == 'ADJECTIVE.' or word == 'ADJECTIVE."':
        adj = str(input('Enter an adjective:\n'))
        word_list.append(adj)
    elif word == 'VERB' or word == 'VERB.' or word == 'VERB."':
        verb = str(input('Enter a verb:\n'))
        word_list.append(verb)

madLibs.close()

#Write a text file filled with user inputted word
finalText = open('finalText.txt', 'w')
finalText.write(f'''Once upon a time there were three {word_list[0]} pigs. One day, their mother said, "It's time for you to {word_list[1]} on your own." So they went off to {word_list[2]} their home. The first built the house out of {word_list[3]}. The second buit the house out of {word_list[4]}. The third built the house out of {word_list[5]}. They were very {word_list[6]}. Then one day a wolf knocked on the first pig's {word_list[7]}. Knock, knock, knock. "Open up or I'll {word_list[8]} your house down." The pig didn't {word_list[9]}. So the wolf blow down the {word_list[10]}.''')
finalText.close()
