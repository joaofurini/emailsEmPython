from cliente import Cliente
from servidor import Servidor


s1 = Servidor(input("Digite o seu email: "), input("Digite a sua senha: "))

while True:
    s1.rodaServidor()
    print(s1.listaMensagens)
    print(s1.listaUsuarios)

    




