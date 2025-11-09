def Encrypt():
    
    message = input('Введіть назву файла з повідомленням, яке хочете зашифрувати: ')
    public_key = input('Введіть назву файла з відкритим ключем адресата: ')

    with open(message, 'r') as f:
        m = int(f.read())

    with open(public_key, 'r') as f:
        n_e = f.readlines()

    n = int(n_e[0].strip())
    e = int(n_e[1].strip())

    c = pow(m, e, n)

    with open('cipher_text.txt', 'w') as f:
        f.write(str(c))

    print('Ваш шифротекст знаходиться у файлі cipher_text.txt')


def Decrypt():

    cipher_txt = input('Введіть назву файла з шифротекстом, який хочете розшифрувати: ')
    private_key = input('Введіть назву файла зі своїм особистим ключем: ')

    with open(cipher_txt, 'r') as f:
        c = int(f.read(), 16)

    with open(private_key, 'r') as f:
        d_p_q = f.readlines()

    d = int(d_p_q[0].strip())
    p = int(d_p_q[1].strip())
    q = int(d_p_q[2].strip())

    n = p*q
    
    m = pow(c, d, n)

    with open('message.txt', 'w') as f:
        f.write(hex(m))

    print('Ваше повідомлення знаходиться у файлі message.txt')


p=input("Введiть 1 якщо хочете зашифрувати повідомлення 2 якщо розшифрувати")
if int(p)==1:
    Encrypt()
elif int(p)==2:
    Decrypt()
else:
    print("Нормально треба користуватися програмою")