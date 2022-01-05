from utils import capital_case, suma

def test_suma():
    assert suma(4,6) == 10

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_capital_capital_case():
    assert capital_case('Semaphore') == 'Semaphore'

def test_failed_capital_case():
    assert capital_case('semaphore') != 'semaphore'
