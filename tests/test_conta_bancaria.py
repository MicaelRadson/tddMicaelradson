from src.conta_bancaria import ContaBancaria

def test_conta_comeca_com_saldo_zero():
    conta = ContaBancaria()
    assert conta.saldo == 0