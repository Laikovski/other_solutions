def get_result(s, words):
    for i in words:
        s = s.replace(i, '')

    if s == '':
        return True
    return False


s = "onetwooe"
# s = "onetwoone"
words = ["one", "two"]

print(get_result(s, words))