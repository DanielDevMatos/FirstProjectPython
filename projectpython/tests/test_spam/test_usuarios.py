from projectpython.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='renzo', email='renzo@python.pro.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Daniel', email='daniel@python.pro.br'),
                Usuario(nome='Renzo', email='renzo@python.pro.br')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
