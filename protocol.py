from rsa_signature import Verify

def SendKey():

    secret_k = input('Введіть назву файла з секретним значенням, яке хочете передати')
    public_key_A = input('Введіть назву файла зі своїм відкритим ключем: ')
    private_key_A = input('Введіть назву файла зі своїм особистим ключем: ')
    public_key_B = input('Введіть назву файла з відкритим ключем адресата: ')


    with open(secret_k, 'r') as f:
        k = int(f.read())
        
    with open(public_key_A, 'r') as f:
        n_e = f.readlines()

    n = int(n_e[0].strip())
    e = int(n_e[1].strip())

    with open(private_key_A, 'r') as f:
        d_ = f.readlines()

    d = int(d_[0].strip())

    with open(public_key_B, 'r') as f:
        n1_e1 = f.readlines()

    n1 = int(n1_e1[0].strip())
    e1 = int(n1_e1[1].strip())

    if n1 < n:
        print('Генеруйте собі іншу пару ключів')

    s = pow(k, d, n)
    k1 = pow(k, e1, n1)
    s1 = pow(s, e1, n1)

    with open('secret_k1_s1.txt', 'w') as f:
        f.write(f'{k1}\n{s1}')



def ReceiveKey():

    secret_k1_s1 = input('Введіть назву файла з секретним значенням, яке отримали')
    private_key_B = input('Введіть назву файла зі своїм особистим ключем: ')
    public_key_A = input('Введіть назву файла з відкритим ключем адресанта: ')

    with open(secret_k1_s1, 'r') as f:
        k1_s1 = f.readlines()

    k1 = int(k1_s1[0].strip())
    s1 = int(k1_s1[1].strip())

    with open(private_key_B, 'r') as f:
        d1_ = f.readlines()

    d1 = int(d1_[0].strip())

    with open(public_key_A, 'r') as f:
        n_e = f.readlines()

    n = int(n_e[0].strip())
    e = int(n_e[1].strip())

#тут точно треба доробити
    
#конфіденційність
    k = pow(k1, d1, n1)
    s = pow(s1, d1, n1)

#автентифікація
    k = pow(s, e, n)

    

    
    
    

    
    

    

    
    
