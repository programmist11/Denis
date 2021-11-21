import re
def your_function(text):
    one = re.findall(r'.', text)  ####разделение по буквам
    print(one)

    copy=one[:]
    noc = re.findall(r'[a-zA-Z_ _]', text)  #####исключение цифер
    print(noc)

    strr = ''.join(noc)  ###преобразование в строку
    print(strr)

    copystr = strr[:]
    copystr = copystr.split()
    copystr = ''.join([i for i in copystr if i.strip()])
    print()
    print(copystr)
    copystr = re.findall(r'.', copystr)
    print(copystr)
    print()
    print()

    sheclospace = []  # здесь будут храниться все числа
    for i in copy:
        if not (i in copystr):
            sheclospace.append(i)
    print(sheclospace)

    print()

    rez = list(i[::-1] for i in strr.split())  ###пословно переворачиваю слова
    print(rez)

    rez = ''.join([i for i in rez if i.strip()])
    print(rez+'0000000000000000')
    rez = re.findall(r'.', rez)

    print()
    print(rez)
    print()


    for j in range(0, len(sheclospace)):
        for i in range(0, len(one)):
            if sheclospace[j] == one[i]:
                rez.insert(i, sheclospace[j])
                one[i] = '11'
                break


    print(''.join(rez))
    return ''.join(rez)

text = input('введите предложение-----')  ## ввод строки
reversd_text = your_function(text)