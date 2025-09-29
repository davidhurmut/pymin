from minifier.core import minify

def test_basic_minify():
    code = "def greet(name):\n    print('hi', name)\n"
    result = minify(code)
    assert "def a" in result
    assert "print" in result
