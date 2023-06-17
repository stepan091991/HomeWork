def if_polidrom(text):
    if text == text[::-1]:
        return True
    else:
        return False
print(if_polidrom(input("Введите текст:")))