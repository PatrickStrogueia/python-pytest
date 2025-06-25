# python -m pytest -m "lento"
# python -m pytest -m "not lento"
# python -m pytest -m "rapido"
# python -m pytest -m "not rapido"
# python -m pytest -m "lento or rapido"
# python -m pytest -m "lento and not rapido"
# python -m pytest -m "rapido and not lento"
# python -m pytest -k "o" -- que contém a palavra "o"

import pytest
import time

@pytest.mark.rapido
def test_soma_rapida():
    assert 1 + 2 == 3

@pytest.mark.lento
def test_soma_lenta():
    time.sleep(2)
    assert 1 + 2 == 3

@pytest.mark.rapido
@pytest.mark.lento
def test_soma_mista():
    time.sleep(1)
    assert 1 + 2 == 3
