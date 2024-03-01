from hello import hello


def test_default():
    assert hello() == "Hello, World"


def test_arrgument():
    for name in ["Ajay", "Rohit", "Mummy", "Papa"]:
        assert hello(name) == f"Hello, {name}"