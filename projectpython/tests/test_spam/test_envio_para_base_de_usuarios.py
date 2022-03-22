import pytest as pytest

from projectpython.spam.enviador_de_email import Enviador
from projectpython.spam.main import EnviadorDeSpam
from projectpython.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
        Usuario(nome='Daniel', email='renzo@python.pro.br'),
        Usuario(nome='Renzo', email='renzo@python.pro.br')
        ],
        [
        Usuario(nome='renzo', email='renzo@python.pro.br')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Cursos Python Pro',
        'Confira os Modulos Fantasticos'
    )
    assert len(usuarios) == enviador.qnd_email_enviados
