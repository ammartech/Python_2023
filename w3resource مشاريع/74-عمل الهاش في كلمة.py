def custom_hash(word):
    hash_value = 0
    for char in word:
        hash_value += ord(char)+5
    return hash_value

word = "example"
hashed_word = custom_hash(word)

print("بعد عمل الهاش:", hashed_word)
