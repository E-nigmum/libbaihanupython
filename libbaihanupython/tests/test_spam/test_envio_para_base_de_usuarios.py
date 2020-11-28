from unittest.mock import Mock

import pytest

from libbaihanupython.spam.enviador_de_email import Enviador
from libbaihanupython.spam.main import EnviadorDeSpam
from libbaihanupython.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Lucas', email='lucasabreusilva.98@gmail.com'),
            Usuario(nome='Renzo', email='lucasabreusilva.98@gmail.com')
        ],
        [
            Usuario(nome='Lucas', email='lucasabreusilva.98@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'lucasabreusilva.98@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Lucas', email='lucasabreusilva.98@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'renzo@python.pro.br',
        'lucasabreusilva.98@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
