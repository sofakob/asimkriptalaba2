def Sign():

    message = input('Введіть назву файла з повідомленням, яке хочете підписати: ')
    private_key = input('Введіть назву файла зі своїм особистим ключем: ')

    with open(message, 'r') as f:
        m = int(f.read())

    with open(private_key, 'r') as f:
        d_p_q = f.readlines()

    d = int(d_p_q[0].strip())
    p = int(d_p_q[1].strip())
    q = int(d_p_q[2].strip())

    n = p*q
    
    s = pow(m, d, n)

    with open('signed_message.txt', 'w') as f:
        f.write(f'{m}\n{s}')

    print('Ваше підписане повідомлення знаходиться у файлі signed_message.txt')



def Verify():

    message = input('Введіть назву файла з повідомленням, яке хочете перевірити: ')
    public_key = input('Введіть назву файла зі своїм відкритим ключем: ')

    with open(message, 'r') as f:
        m_s = f.readlines()

    m_signed = int(m_s[0].strip())
    s = int(m_s[1].strip())

    with open(public_key, 'r') as f:
        n_e = f.readlines()

    n = int(n_e[0].strip())
    e = int(n_e[1].strip())

    m = pow(s, e, n)

    if m == m_signed:
        print('Повідомлення не спотворене')
    else:
        print('Щось не так')


Verify()

    
