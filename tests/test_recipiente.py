from classes.recipiente import Recipiente


def test_recipiente_atributos(rec_comum: Recipiente):
    assert (
        rec_comum.tamanho == 100.0
    ), "Verifique se o tamanho do recipiente está sendo atribuido corretamente"
    assert (
        rec_comum.conteudo == 0.0
    ), "Verifique se o conteudo do recipiente esta sendo inicializado em 0"
    assert rec_comum.esta_limpo(), "Verifique se o recipiente esta limpo inicialmente"
    assert (
        rec_comum.limpo
    ), "Verifique se o atributo limpo do recipiente foi inicializado como verdadeiro"


def test_recipiente_tamanho_negativo(rec_negativo: Recipiente):
    assert (
        rec_negativo.tamanho == 0
    ), "Verifique se, ao passar um valor negativo como tamanho do recipiente, ele é inicializado em 0"


def test_recipiente_estado(rec_comum: Recipiente):
    assert (
        rec_comum.estado()
    ), "Verifique se o metodo estado do recipiente retorna `limpo` inicialmente"


def test_recipiente_esta_vazio(rec_comum: Recipiente):
    assert (
        rec_comum.esta_vazio()
    ), "Verifique se o recipiente esta sendo inicializado como vazio"


def test_recipiente_sujar(rec_comum: Recipiente):
    rec_comum.sujar()

    assert (
        not rec_comum.esta_limpo()
    ), "Verifique se o recipiente se torna sujo ao sujar"

    assert (
        rec_comum.estado() == "sujo"
    ), "Verifique se o estado do recipiente se torna sujo ao sujar"

    assert (
        rec_comum.__repr__() == "Um recipiente sujo não especificado"
    ), "Verifique se o __repr__ do recipiente está correto"
    assert (
        rec_comum.__str__() == "Um recipiente sujo não especificado"
    ), "Verifique se o __str__ do recipiente está correto"


def test_recipiente_rotina(rec_comum: Recipiente):
    rec_comum.conteudo = 100.0
    rec_comum.sujar()
    rec_comum.lavar()

    assert (
        rec_comum.esta_limpo()
    ), "Verifique se o recipiente ficou limpo depois de lavar"
    assert rec_comum.conteudo == 0, "Verifique se o conteudo foi zerado após lavar"

    assert (
        rec_comum.__repr__() == "Um recipiente limpo não especificado"
    ), "Verifique se o __repr__ do recipiente está correto"
    assert (
        rec_comum.__str__() == "Um recipiente limpo não especificado"
    ), "Verifique se o __str__ do recipiente está correto"
