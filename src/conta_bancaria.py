class ContaBancaria:
    def __init__(self) -> None:
        self._saldo: float = 0.0

    @property
    def saldo(self) -> float:
        return self._saldo