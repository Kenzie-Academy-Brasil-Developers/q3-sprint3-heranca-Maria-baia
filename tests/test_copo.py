from classes import copo
from classes.copo import Copo


def test_copo_atributos(copo_comum: Copo):
    assert (
        copo_comum.tamanho == 300
    ), "Verifique se o tamanho do copo foi atribuido corretamente"

    assert (
        copo_comum.conteudo == 0
    ), "Verifique se o conteudo foi atribuido para zero inicialmente"

    assert copo_comum.esta_limpo(), "Verifique se o copo está limpo inicialmente"
    assert copo_comum.esta_vazio(), "Verifique se o copo está vazio inicialmente"
    assert (
        copo_comum.__repr__() == "Um copo vazio de 300.0ml"
    ), "Verifique se a mensagem __repr__ está correta"
    assert (
        copo_comum.__str__() == "Um copo vazio de 300.0ml"
    ), "Verifique se a mensagem __str__ está correta"


def test_copo_encher_cafe_rotina(copo_comum: Copo):
    copo_comum.encher("café")

    assert (
        copo_comum.bebida == "café"
    ), "Verifique se a bebida esta sendo atribuida corretamente"
    assert (
        copo_comum.estado() == "sujo"
    ), "Verifique se o copo está sendo sujo ao encher de bebida"
    assert (
        not copo_comum.esta_limpo()
    ), "Verifique se limpo está sendo mudado para falso ao encher um copo"
    assert (
        copo_comum.conteudo == 300.0
    ), "Verifique se o conteudo foi mudado para encher o copo"

    assert (
        copo_comum.__repr__() == "Um copo de 300.0ml contendo 300.0ml de café"
    ), "Verifique se a mensagem __repr__ está correta apos encher um copo"

    assert (
        copo_comum.__str__() == "Um copo de 300.0ml contendo 300.0ml de café"
    ), "Verifique se a mensagem __repr__ está correta apos encher um copo"


def test_copo_encher_e_beber_cafe(copo_comum: Copo):
    copo_comum.encher("café")
    copo_comum.beber(30)

    assert (
        copo_comum.conteudo == 270.0
    ), "Verifique se o conteudo foi mudado ao beber do copo"

    assert (
        copo_comum.__repr__() == "Um copo de 300.0ml contendo 270.0ml de café"
    ), "Verifique se a mensagem __repr__ está correta apos beber de copo"

    assert (
        copo_comum.__str__() == "Um copo de 300.0ml contendo 270.0ml de café"
    ), "Verifique se a mensagem __repr__ está correta apos beber de copo"


def test_copo_encher_beber_quantidade_negativa(copo_comum: Copo):
    copo_comum.encher()
    result = copo_comum.beber(-100)
    expected = "Quantidade deve ser positiva"
    assert (
        result == expected
    ), "Verifique se, ao passar uma quantidade negativa ao beber, é retornada a mensagem correta"


def test_copo_encher_beber_quantidade_maior_que_o_copo(copo_comum: Copo):
    copo_comum.encher()
    result = copo_comum.beber(600000000)
    expected = "Não há bebida suficiente no copo"
    assert (
        result == expected
    ), "Verifique se, ao passar uma quantidade maior que o copo ao beber, é retornada a mensagem correta"
    assert (
        copo_comum.esta_vazio
    ), "Verifique se, na falha em beber, o copo ainda esta vazio"


def test_copo_encher_agua(copo_comum: Copo):
    copo_comum.encher()

    assert (
        copo_comum.bebida == "água"
    ), "Verifique se o conteudo padrao ao encher um copo é `água`"


def test_copo_sujar(copo_comum: Copo):
    copo_comum.sujar()

    assert (
        not copo_comum.esta_limpo()
    ), "Verifique se, ao sujar, o copo muda o atributo limpo para falso"


def test_copo_encher_sujo(copo_comum: Copo):
    copo_comum.sujar()
    result = copo_comum.encher()
    expected = "Não se pode encher um copo sujo"

    assert result == expected, "Verifique se não é possivel encher um copo sujo"


def test_copo_lavar(copo_comum: Copo):
    copo_comum.encher("café")
    copo_comum.lavar()

    assert copo_comum.esta_limpo(), "Verifique se o copo fica limpo após lavar"
    assert (
        not copo_comum.bebida
    ), "Verifique se após lavar o copo, o atributo bebida mudou para None"
    assert (
        copo_comum.conteudo == 0.0
    ), "Verifique se após lavar o copo, o atributo conteudo mudou para 0.0"
