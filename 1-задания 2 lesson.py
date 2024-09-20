# Ввод строки от пользователя
sentence = input("Введите строку, разделенную пробелами: ")

# Разделение строки на слова
words = sentence.split()

# Поиск самого длинного слова
longest_word = max(words, key=len)

print(f"Самое длинное слово: {longest_word}")
