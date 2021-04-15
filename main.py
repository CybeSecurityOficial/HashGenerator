import os
import requests

def md5():
    os.system('clear')

    plv = input('Digite o texto para gerar a hash: ')
    request = requests.get(f'https://api.hashify.net/hash/md5/hex?value={plv}').json()

    print('\nHash gerada\n\nHash: {}\nTipo: {}\n'.format(request['Digest'], request['Type']))
    sair = input('Deseja gerar uma nova hash? s/n: ')

    if sair == 's' or sair == 'S':
        md5()

    else:
        main()

def md4():
    os.system('clear')

    plv = input('Digite o texto para gerar a hash: ')
    request = requests.get(f'https://api.hashify.net/hash/md4/hex?value={plv}').json()

    print('\nHash gerada\n\nHash: {}\nTipo: {}\n'.format(request['Digest'], request['Type']))
    sair = input('Deseja gerar uma nova hash? s/n: ')

    if sair == 's' or sair == 'S':
        md4()

    else:
        main()

def main():
    os.system('clear')
    print('''
██╗  ██╗ █████╗ ███████╗██╗  ██╗
██║  ██║██╔══██╗██╔════╝██║  ██║
███████║███████║███████╗███████║
██╔══██║██╔══██║╚════██║██╔══██║
██║  ██║██║  ██║███████║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
            _Cyber Security_

[01] = Gerar hash MD5
[02] = Gerar hash MD4
[03] = Sair\n''')

    opc = input('--> ')

    if opc == '1' or opc == '01':
        md5()

    elif opc == '2' or opc == '02':
        md4()

    elif opc == '3' or opc == '03':
        os.system('clear')
        print('_Cyber Security_\n')
        exit()

    else:
        main()

main()
