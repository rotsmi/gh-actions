from add import addition

def test_addition():
    assert addition(4,10) == 14

def test_addition_fail():
    assert addition(10,10) != 21
