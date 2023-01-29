def search(surn):
    res_list = []
    with open('book.txt', 'r', encoding='utf-8') as file:
        while True:
            my_book = file.readline()
            if not my_book:
                if not my_book:
                    break
            if my_book.rstrip() == surn:
                res_list.append(surn)
                for i in range(4):
                    res_list.append(file.readline().strip())
                # res_list.append('')
    if len(res_list) > 0:
        return res_list
    return 'Не найдено!'

def export(res):
    with open('book.txt', 'a', encoding='utf-8') as file:
        for ind in range(4):
            file.write(res[ind] + '\n')
        file.write(res[4])
