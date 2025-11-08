class ContaBancaria:
    def __init__(self) -> None:
        self._saldo: float = 0.0

    @property
    def saldo(self) -> float:
        return self._saldo
    
    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        self._saldo += valor