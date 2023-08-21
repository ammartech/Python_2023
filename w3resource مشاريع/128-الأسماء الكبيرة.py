
def is_lower_string(string):
    for char in string:
        if char.islower():
            return True
    return False

if __name__=="__main__":
    string= "Ammar Yasser"
    print(is_lower_string(string))
