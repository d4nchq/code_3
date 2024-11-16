word = input("Введіть слово: ").lower()  #переводимо слово в нижній регістр для зручності.
vowels = "аеєиіїоуюяaeiouy"  #список голосних літер (українські та англійські).
vowel_letters = []  #список для голосних.
consonant_letters = []  #список для приголосних.

#розподіляємо літери на голосні та приголосні.
for letter in word:
    if letter in vowels:
        vowel_letters.append(letter)
    else:
        consonant_letters.append(letter)

#виводимо результат.
print("\nГолосні літери:")
for vowel in vowel_letters:
    print(vowel)

print("\nПриголосні літери:")
for consonant in consonant_letters:
    print(consonant)
