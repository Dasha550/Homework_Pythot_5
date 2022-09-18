def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res
#исходный текст хранится в файле 'Task_2.1.txt'
with open('Task_2.1.txt', "r") as f:
    text = f.read()
print(text)
#Текст после кодировки хранится в файле "Task_2.2.txt"
print(f"Текст после кодировки: {coding(text)}")
with open("Task_2.2.txt", "w") as f:
    f.write(coding(text))
#Текст после дешифровки хранится в файле"Task_2.3.txt"
print(f"Текст после дешифровки: {decoding(coding(text))}")
with open("Task_2.3.txt", "w") as f:
    f.write(decoding(coding(text)))