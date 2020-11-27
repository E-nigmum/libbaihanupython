from libbaihanupython.spam.enviador_de_email import Enviador
from libbaihanupython.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador)
    enviador_de_spam.enviar_emails(
        'lucasabreusilva.98@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
