from pytest import fixture
from classes.copo import Copo
from classes.recipiente import Recipiente


@fixture
def copo_comum():
    return Copo(300)


@fixture
def rec_comum():
    return Recipiente(100)


@fixture
def rec_negativo():
    return Recipiente(-1000)
