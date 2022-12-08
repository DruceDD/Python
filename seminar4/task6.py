# 6. Дан текст: в первой строке задано число строк, далее идут сами строки.
# Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов
# несколько, выведите то, которое меньше в лексикографическом порядке.

sp = ['apple', 'orange', 'banana', 'banana', 'orange', 'banana', 'orange']
word = {}
for el in sp:
    word[el] = word.get(el, 0) + 1
print(word)

word = dict(sorted(word.items()))
print(word)

max_count = max(word.values())
for key, value in word.items():
    if value == max_count:
        print(key)