def Sign():

    message = input('Введіть назву файла з повідомленням, яке хочете підписати: ')
    private_key = input('Введіть назву файла зі своїм особистим ключем: ')

    with open(message, 'r') as f:
        m = int(f.read(), 16)

    with open(private_key, 'r') as f:
        d_p_q = f.readlines()

    d = int(d_p_q[0].strip(), 16)
    p = int(d_p_q[1].strip(), 16)
    q = int(d_p_q[2].strip(), 16)

    n = p*q
    
    s = hex(pow(m, d, n))

    with open('signed_message.txt', 'w') as f:
        f.write(f'{hex(m)}\n{s}')

    print('Ваше підписане повідомлення знаходиться у файлі signed_message.txt')



def Verify():

    message = input('Введіть назву файла з повідомленням, яке хочете перевірити: ')
    public_key = input('Введіть назву файла зі своїм відкритим ключем: ')

    with open(message, 'r') as f:
        m_s = f.readlines()

    m_signed = int(m_s[0].strip(), 16)
    s = int(m_s[1].strip(), 16)

    with open(public_key, 'r') as f:
        n_e = f.readlines()

    n = int(n_e[0].strip(), 16)
    e = int(n_e[1].strip(), 16)

    m = hex(pow(s, e, n))

    if m == hex(m_signed):
        print('Повідомлення не спотворене')
    else:
        print('Щось не так')


p=input("Введiть 1, якщо хочете підписати повідомлення та 2, якщо перевірити: ")
if int(p)==1:
    Sign()
elif int(p)==2:
    Verify()
else:
    print("Нормально треба користуватися програмою")

    
