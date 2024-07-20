from API_Quiz import Validator
import pytest

def test_charatersCheck():
    assert Validator.charatersCheck('Melody') is None
    assert Validator.charatersCheck('Melody123') is None
    assert Validator.charatersCheck('Melody 123') is None
    assert Validator.charatersCheck('Melody@') == 'Name contains non-English characters'

def test_capitalizedCheck():
    assert Validator.capitalizedCheck('Melody Holiday Inn') is None
    assert Validator.capitalizedCheck('melody holiday inn') == 'Name is not capitalized'

def test_currencyCheck():
    assert Validator.currencyCheck('TWD') is None
    assert Validator.currencyCheck('USD') is None
    assert Validator.currencyCheck('EUR') == 'Currency format is wrong'