vowel_check = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}

char = input("Enter a character: ").lower()

print("Vowel" if vowel_check.get(char, False) else "Consonant")
