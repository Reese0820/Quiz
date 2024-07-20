from API_Quiz import FinanceInspector
import pytest

def test_priceCheck():
    assert FinanceInspector.priceCheck(1500) == 1500
    assert FinanceInspector.priceCheck(2500) == 'Price is over 2000'

def test_twdExchanger():
    price, currency = FinanceInspector.twdExchanger(100, 'USD')
    assert price == 3100
    assert currency == 'TWD'

    price, currency = FinanceInspector.twdExchanger(1500, 'TWD')
    assert price == 1500
    assert currency == 'TWD'