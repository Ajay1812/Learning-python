from hello import hello

def test_default():
    assert hello() == "Hello, World"

def test_arrgument():
    assert hello("Ajay") == "Hello, Ajay"