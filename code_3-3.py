sentence = input("Введіть речення: ")  #вводимо речення.
words = sentence.split()  #розділяємо речення на слова.

print("\nКількість літер у кожному слові:")
for word in words:
    #рахуємо лише літери в слові (ігноруючи знаки пунктуації).
    letter_count = sum(1 for char in word if char.isalpha())
    print(f"Слово '{word}' має {letter_count} літер.")