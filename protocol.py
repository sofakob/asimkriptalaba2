

def SendKey():

    secret_k = input('Введіть назву файла з секретним значенням, яке хочете передати: ')
    public_key_A = input('Введіть назву файла зі своїм відкритим ключем: ')
    private_key_A = input('Введіть назву файла зі своїм особистим ключем: ')
    public_key_B = input('Введіть назву файла з відкритим ключем адресата: ')


    with open(secret_k, 'r') as f:
        k = int(f.read(), 16)
        
    with open(public_key_A, 'r') as f:
        n_e = f.readlines()

    n = int(n_e[0].strip(), 16)
    e = int(n_e[1].strip(), 16)

    with open(private_key_A, 'r') as f:
        d_ = f.readlines()

    d = int(d_[0].strip(), 16)

    with open(public_key_B, 'r') as f:
        n1_e1 = f.readlines()

    n1 = int(n1_e1[0].strip(), 16)
    e1 = int(n1_e1[1].strip(), 16)

    if n1 < n:
        raise Exception('Генеруйте собі іншу пару ключів')

    s = pow(k, d, n)
    k1 = pow(k, e1, n1)
    s1 = pow(s, e1, n1)

    with open('secret_k1_s1.txt', 'w') as f:
        f.write(f'{hex(k1)}\n{hex(s1)}')

    print('Ваше секретне значення записано у файл secret_k1_s1.txt')


def ReceiveKey():

    secret_k1_s1 = input('Введіть назву файла з секретним значенням, яке отримали: ')
    private_key_B = input('Введіть назву файла зі своїм особистим ключем: ')
    public_key_A = input('Введіть назву файла з відкритим ключем адресанта: ')

    with open(secret_k1_s1, 'r') as f:
        k1_s1 = f.readlines()

    k1 = int(k1_s1[0].strip(), 16)
    s1 = int(k1_s1[1].strip(), 16)

    with open(private_key_B, 'r') as f:
        d1_ = f.readlines()

    d1 = int(d1_[0].strip(), 16)
    p = int(d1_[1].strip(), 16)
    q = int(d1_[2].strip(), 16)
    n1 = p*q
    
    with open(public_key_A, 'r') as f:
        n_e = f.readlines()

    n = int(n_e[0].strip(), 16)
    e = int(n_e[1].strip(), 16)
    
#конфіденційність
    k = pow(k1, d1, n1)
    s = pow(s1, d1, n1)

#автентифікація
    k = pow(s, e, n)

    with open('received_k.txt', 'w') as f:
        f.write(f'{hex(k)}')

    print('Отримане секретне значення знаходиться у файлі recieved_k.txt')
    

p=input("Введiть 1, якщо хочете надіслати секретне значення та 2, якщо отримати: ")
if int(p)==1:
    SendKey()
elif int(p)==2:
    ReceiveKey()
else:
    print("Нормально треба користуватися програмою")
    

    
    

    

    
    
