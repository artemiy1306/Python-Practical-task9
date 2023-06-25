import json

phone_book = {}
path = 'phones.json'


def open_file():
    global phone_book
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            phone_book = json.load(file)
        return True
    except:
        return False
def save_file():
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(phone_book, file, ensure_ascii=False)
        return True
    except:
            return False
    
def search(word: str) -> dict[int:dict[str, str]]:
    result = {}
    for index, contact in phone_book.items():
        if word.lower() in ' '.join(contact.values()).lower():
            result[index] = contact
        return result

def check_id():
    if phone_book:
        return max(list(map(int, phone_book)))+1
    return 1

def add_contact(new: {int: dict[str, str]}):
    contact = {check_id(): new}
    phone_book.update(contact)

def change_contact(index, new_cont):
    
    tmp = phone_book[index]
    n=tmp['name']
    p=tmp['phone']
    c=tmp['comment']
    name = new_cont[0]
    phone = new_cont[1]
    comment = new_cont[2]
    if name == '':
        name = n
    if phone == '':
        phone = p
    if comment == '':
        comment = c
    phone_book[index] = {'name': name, 'phone': phone, 'comment': comment}
    
        
def remove(index):
    name = phone_book.pop(str(index))
    return name.get('name')    