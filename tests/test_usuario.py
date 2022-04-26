from src.leilao.dominio import Usuario, Leilao
import pytest



@pytest.fixture
def vini():
    return Usuario('Vini', 800.0)

@pytest.fixture
def leilao():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(vini, leilao):

    vini.propoe_lance(leilao, 50.0)

    assert vini.carteira == 750.0

def test_deve_permitir_propor_lance_quando_o_valor_e_menor_que_o_saldo_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 1.0)

    assert vini.carteira == 799.0

def test_deve_permitir_propor_lance_quando_o_valor_e_igual_ao_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 800.0)

    assert vini.carteira == 0.0

def test_deve_negar_propor_lace_quando_o_valor_e_maior_que_o_saldo_da_carteira(vini, leilao):
    with pytest.raises(ValueError):

        vini.propoe_lance(leilao, 900.0)
