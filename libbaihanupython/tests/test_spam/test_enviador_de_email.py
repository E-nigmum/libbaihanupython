from libbaihanupython.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'lucasabreusilva.98@gmail.com',
        'lucaseduardoabreusilva@gmail.com',
        'Cursos Python Pro',
        'Turma Jessica Ferrari'
    )
    assert 'lucasabreusilva.98@gmail.com' in resultado