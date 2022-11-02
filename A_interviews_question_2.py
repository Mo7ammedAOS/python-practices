''' Write a function that takes in a string of one or more words,
and returns the same string, but with all five or more letter
words reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.'''

# test = 'this is me'
# print(test.split(' '))

# list = ['This','is','us']
# sentence = ' '.join(list)
# print(sentence)

def spin_words(sentence):
    # first convert the sentece to list
    the_list = sentence.split(' ')
    # prepare an empty list to store processed items from the_list
    processed_list = []
    for item in the_list:
        if len(item)>=5:
            item = item[::-1]
        processed_list.append(item)

    the_final_sentence = ' '.join(processed_list)

    return print(the_final_sentence)

spin_words('this is notis')
