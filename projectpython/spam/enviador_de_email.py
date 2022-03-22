class Enviador:
    def __init__(self):
        self.qnd_email_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email remetente invalido: {remetente}')
        self.qnd_email_enviados += 1
        return remetente

class EmailInvalido(Exception):
    pass
