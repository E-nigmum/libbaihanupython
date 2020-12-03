from libbaihanupython.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Lucas', email='lucasabreusilva.98@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Lucas', email='lucasabreusilva.98@gmail.com'),
                Usuario(nome='Renzo', email='lucasabreusilva.98@gmail.com')
                ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
