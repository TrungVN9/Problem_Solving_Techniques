def ceasar_cipher(string, rotate):
    length_ = len(string)
    ans = ''
    for index in range(length_):
        if ord(string[index]) in range(97,123):
            ans += (chr((ord(string[index]) + rotate - 97) % 26 + 97))
        elif ord(string[index]) in range(65,91):
            ans += (chr((ord(string[index]) + rotate - 65) % 26 + 65))
        else:
            ans += (string[index])
    return ans

print(ceasar_cipher("middle-Outz", 2))
            