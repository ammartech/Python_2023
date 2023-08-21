def limit_and_format_string(word,max_len):
    formatted_word=word[:max_len]
    if len(word) > max_len:
        formatted_word +='...'
    return formatted_word
print("تمت بحول الله!!")


if __name__=="__main__":
    string="Hi, I am Ammar"
    max_arch=9
    formatted_after=limit_and_format_string(string,max_arch)
    print(formatted_after)
