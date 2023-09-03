def count_occurrences(word, filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            count += line.count(word)
    return count

def replace_word(filename, old_word, new_word):
    with open(filename, 'r') as file:
        content = file.read()
        occurrences = content.count(old_word)
        new_content = content.replace(old_word, new_word, occurrences)
    with open('result.txt', 'w') as file:
        file.write(new_content)

word_to_count = "terrible"
file_to_read = "file_to_read.txt"

# Count the occurrences of a word
total_occurrences = count_occurrences(word_to_count, file_to_read)
print(f"Total occurrences of the word '{word_to_count}': {total_occurrences}")

# Replace the word and write to result.txt
if total_occurrences > 0:
    if total_occurrences % 2 == 0:
        replace_word(file_to_read, word_to_count, "pathetic")
    else:
        replace_word(file_to_read, word_to_count, "marvellous")
    print("Replacement completed. Please check result.txt for the updated content.")
else:
    print("No occurrences of the word found.")