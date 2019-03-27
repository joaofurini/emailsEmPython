from cliente import Cliente
from mensagem import Mensagem
class Servidor:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.listaUsuarios = []
        self.listaMensagens = []
    
    def getEmail(self):
        return self.email
    
    def getSenha(self):
        return self.senha
    
    def getMensagens(self):
        return self.mensagens

    def rodaServidor(self):
        cliente1 = Cliente(self.email, self.senha, "bol")
        self.listaUsuarios.append(cliente1.montaConta())
        mensagem1 = Mensagem(cliente1.login, input("Digite o destinatario: "), input("Digite o assunto: "),\
           input("Digite sua mensagem: "))
        self.listaMensagens.append(mensagem1.montaMensagem())





        

