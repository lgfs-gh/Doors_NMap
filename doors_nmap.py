import os
import sys
from time import sleep
import nmap3
from stringcolor import *

slgn = cs("██▓ ██▓     ▓█████▄  ▒█████   ▒█████   ██▀███    ██████       ██▓ ██▓\n"
          "▓██▒▓██▒     ▒██▀ ██▌▒██▒  ██▒▒██▒  ██▒▓██ ▒ ██▒▒██    ▒      ▓██▒▓██▒\n"
          "▒██▒▒██▒     ░██   █▌▒██░  ██▒▒██░  ██▒▓██ ░▄█ ▒░ ▓██▄        ▒██▒▒██▒\n"
          "░██░░██░     ░▓█▄   ▌▒██   ██░▒██   ██░▒██▀▀█▄    ▒   ██▒     ░██░░██░\n"
          "░██░░██░     ░▒████▓ ░ ████▓▒░░ ████▓▒░░██▓ ▒██▒▒██████▒▒     ░██░░██░\n"
          "░▓  ░▓        ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░     ░▓  ░▓  \n"
          " ▒ ░ ▒ ░      ░ ▒  ▒   ░ ▒ ▒░   ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒  ░ ░      ▒ ░ ▒ ░\n"
          " ▒ ░ ▒ ░      ░ ░  ░ ░ ░ ░ ▒  ░ ░ ░ ▒    ░░   ░ ░  ░  ░        ▒ ░ ▒ ░\n"
          " ░   ░          ░        ░ ░      ░ ░     ░           ░        ░   ░  \n"
          "              ░                                                        ", "red")


def main():
    escolha = None

    while escolha != 'exit':
        print(f'\n\n{slgn}\n\n')  # Printa o slogan
        print('# NMAP VERSION\n'
              '# Criado por Luiz Gustavo para fins de estudo, baseado na aula\n'
              '# do Afonso da Silva na comunidade TDI.\n')
        print('1 - Realizar SCAN\n'
              '2 - Encerrar o programa')  # Menu Inicial
        escolha = input(bold('>> Entre com a sua escolha:\n>> '))
        if escolha == '1':
            dominio = input(bold('\n>> Digite o domínio:\n>> '))
            print(bold('\n-------- REALIZANDO O SCAN --------'))
            scan(dominio)
        else:
            break
    print(bold('\n-------- PROGRAMA ENCERRADO  --------'))
    sleep(1)
    exit(0)


def scan(dominio):
    res = []
    scan_completo = []
    porta = None
    servico = None
    estado = None

    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(dominio)
    for i in results.items():
        for x in i[1].items():
            try:
                for z in x[1]:
                    if len(z) > 1:
                        for v in z.items():
                            if v[0] == 'portid':
                                porta = v[1]
                            if v[0] == 'service':
                                servico = v[1]['name']
                            if v[0] == 'state':
                                estado = v[1]
                        if {'porta': porta, 'servico': servico, 'estado': estado} in res:
                            pass
                        else:
                            res.append({'porta': porta, 'servico': servico, 'estado': estado})
            except:
                pass

    for i in res:
        espaco = ' '
        tam_serv = 15 - len(i['servico'])
        tam_port = 6 - len(i['porta'])
        texto = f"SERVICO: {i['servico'].upper() + tam_serv * espaco} " \
                f"|| PORTA: {i['porta'] + tam_port * espaco}" \
                f" || ESTADO: {i['estado'].upper()}\n"
        scan_completo.append(f"SERVICO: {i['servico'].upper() + tam_serv * espaco} "
                             f"|| PORTA: {i['porta'] + tam_port * espaco}"
                             f" || ESTADO: {i['estado'].upper()}\n")
        for letra in texto:
            sys.stdout.write(letra)
            sys.stdout.flush()
            sleep(0.005)

    x = input(cs('\n--------- SCAN CONCLUIDO --------\n', 'green').bold() +
              '1) Salvar em arquivo (txt)\n'
              '2) Realizar outro scan\n'
              '3) Encerrar o programa\n'
              '>> ')
    if x == '1':
        with open(dominio + '_scan.txt', 'w') as arquivo:
            for linha in scan_completo:
                arquivo.write(linha)
            arquivo.close()
        print(bold(f"\n--------- ARQUIVO SERÁ SALVO COMO: {dominio + '_scan.txt'} --------"))
        sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif x == '3':
        print(bold('\n-------- PROGRAMA ENCERRADO --------'))
        sleep(1)
        exit(0)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
