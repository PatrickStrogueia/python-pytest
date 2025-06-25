def soma(a, b):
    return a + b

def comprimento(lista):
    return len(lista)

def test_soma_e_comprimento():
    assert soma(3, 2) == 5
    assert comprimento([1,2,3,4,5]) == 5
    