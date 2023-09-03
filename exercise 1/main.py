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

# 统计单词出现次数
total_occurrences = count_occurrences(word_to_count, file_to_read)
print(f"单词 '{word_to_count}' 出现的总次数: {total_occurrences}")

# 替换单词并写入 result.txt
if total_occurrences > 0:
    if total_occurrences % 2 == 0:
        replace_word(file_to_read, word_to_count, "pathetic")
    else:
        replace_word(file_to_read, word_to_count, "marvellous")
    print("替换完成。请查看 result.txt 获取更新后的内容。")
else:
    print("未找到该单词的出现次数。")

