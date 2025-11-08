from src.conta_bancaria import ContaBancaria

def test_conta_comeca_com_saldo_zero():
    conta = ContaBancaria()
    assert conta.saldo == 0

def test_deposito_aumenta_saldo():
    conta = ContaBancaria()
    conta.depositar(100)
    assert conta.saldo == 100