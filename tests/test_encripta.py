from cifra_cesar.cifra_cesar import encripta


def test_encripta_eduardo_retorna_rqhneqb():
    assert encripta('Eduardo') == 'rqhneqb'


def test_encripta_rqhneqb_retorna_eduardo():
    assert encripta('rqhneqb') == 'eduardo'


def test_encripta_deve_retornar_minusculas():
    assert encripta('A').islower()


def test_encripta_deve_preservar_os_espacos():
    res = encripta('nome sobrenome')
    assert res[4] == ' '
