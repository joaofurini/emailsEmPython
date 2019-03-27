class Cliente:

    def __init__(self, login, senha, servidor):
        self.login = login
        self.senha = senha
        self.servidor = servidor

    def getLogin(self):
        return self.login 
    
    
    def getSenha(self):
        return self.senha
    
    
    def getServidor(self):
        return self.servidor

    def montaConta(self):
        usuario = "Nome: " + self.login + "Servidor: " + self.senha
        return usuario
    

