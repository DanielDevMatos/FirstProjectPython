from projectpython.spam.enviador_de_email import Enviador
from projectpython.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Cursos Python Pro',
        'Confira os Modulos Fantasticos'
    )
    