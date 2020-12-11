from random_word import RandomWords
from nltk.corpus import words
from random import sample

n = 6
arr = []
for i in range(100):
    rand_words = ' '.join(sample(words.words(), n))
    arr.append(rand_words.upper())
# print(arr)

f= open("promptsfix.txt","w+")
for i in range(100):
    # f.write(arr[i])
    f.write("*/sample%d " % (i+1))
    f.write("%s\r\n" % (arr[i]))
    
f.close()
# r = RandomWords()
# print("Hello world")
# Return a single random word
# print(' '.join(r.get_random_words(minLength=5, maxLength=10)))
# abc = r.get_random_words(minLength=5, maxLength=10)
# print(abc)
# # Return list of Random words
# for i in range(100):
# print(' '.join(r.get_random_words(minLength=5, maxLength=10, limit=11)))
# a = r.get_random_words(minLength=5, maxLength=10, limit=11)
# b = ' '.join(a)
# print(b)
# # Return Word of the day
# print(r.word_of_the_day())