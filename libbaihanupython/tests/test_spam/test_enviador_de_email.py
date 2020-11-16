import pytest

from libbaihanupython.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com.br', 'lucasabreusilva.98@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'lucaseduardoabreusilva@gmail.com',
        'Cursos Python Pro',
        'Turma Jessica Ferrari'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'lucasabreusilva.98']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            remetente,
            'lucaseduardoabreusilva@gmail.com',
            'Cursos Python Pro',
            'Turma Jessica Ferrari'
        )
        assert remetente in resultado
