class Mensagem:
    def __init__(self, remetente, destinatario, assunto, corpo):
        self.remetente = remetente
        self.destinatario = destinatario
        self.assunto = assunto
        self.corpo = corpo
    
    def getRemetente(self):
        return self.remetente
    
    def getDestinatario(self):
        return self.destinatario

    def getAssunto(self):
        return self.assunto
    
    def getCorpo(self):
        return self.corpo

    def montaMensagem(self):
        mensagemMontada= "De: "+ self.remetente + "Para: " + self.destinatario + "Assunto: " + " Mensagem: " + self.corpo
        return mensagemMontada
    

