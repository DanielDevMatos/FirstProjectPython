import pytest as pytest

from projectpython.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['renzo@python.pro.br', 'foo@bar.com']
)

def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'luciano@python.pro.br',
        'Curso Python Pro',
        'Primeira turma aberta'
    )
    assert remetente in resultado

@pytest.mark.parametrize(
    'remetente',
    ['', 'foobar.com']
)

def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'luciano@python.pro.br',
            'Curso Python Pro',
            'Primeira turma aberta'
        )
