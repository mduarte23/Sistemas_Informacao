import pytest


#teste unitario para cada funçao
def teste_somar_strategy():
    from main import somar
    assert somar.executar(1,1) == 2
