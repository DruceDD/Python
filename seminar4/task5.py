# 5. Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны. Для слова из словаря, записанного в последней строке, определите его синоним.

dict = {}
dict['Hello'] = 'Hi'
dict['Bye'] = 'Goodbye'
dict['List'] = 'Array'

# print(slovar)
# print(slovar.values())
# print(slovar.keys())
# print(slovar.items())

word = input('Введите слово: ')
for key, value in dict.items():
    if word == key:
        print(value)
    if word == value:
        print(key)
