import json

import pytest

from utlis import get_all, sort_by_date, get_date, get_operation, get_receiver, get_amount, get_currency


def test_get_all_returns_data():
    with open("operations.json", encoding="utf-8") as f:
        expected_data = json.load(f)
        data = get_all()
        assert data == expected_data


def test_get_all_returns_non_empty_data():
    data = get_all()
    assert len(data) > 0


def test_sort_by_date():
    data = sort_by_date()
    assert len(data) == 5


def test_sort_by_date_not_empty():
    data = sort_by_date()
    assert len(data) != 0


def test_sort_by_date_not_empty():
    data = sort_by_date()
    assert len(data) == 5


def test_get_date_valid_date():
    operation = {'id': 1, 'date': '2022-04-09T10:30:00Z', 'state': 'EXECUTED'}
    assert get_date(operation) == '09.04.2022'


def test_get_operation_with_maestro_card():
    operation = {'from': 'Maestro 1234 5678 9012 3456'}
    result = get_operation(operation)
    assert result != 'Maestro 1234 **** **** 3456'


def test_get_operation_with_no_information():
    operation = {'to': 'Maestro 1234 5678 9012 3456'}
    result = get_operation(operation)
    assert result == 'No information'


def test_get_receiver():
    operation1 = {"to": "Jane 1234567890123456"}
    assert get_receiver(operation1) == "Jane **3456"

    operation2 = {"to": "John 1111222233334444"}
    assert get_receiver(operation2) == "John **4444"

    operation3 = {"to": "Mike 9876543210987654"}
    assert get_receiver(operation3) == "Mike **7654"

def test_get_amount():
    operation_1 = {'operationAmount': {'amount': 100}}
    operation_2 = {'operationAmount': {'amount': 999.99}}
    operation_3 = {'operationAmount': {'amount': -50}}

    assert get_amount(operation_1) == 100
    assert get_amount(operation_2) == 999.99
    assert get_amount(operation_3) == -50


def test_get_currency_usd():
    operation = {
        'operationAmount': {
            'amount': 100.00,
            'currency': {
                'name': 'USD'
            }
        }
    }
    assert get_currency(operation) == 'USD'


def test_get_currency_eur():
    operation = {
        'operationAmount': {
            'amount': 200.00,
            'currency': {
                'name': 'EUR'
            }
        }
    }
    assert get_currency(operation) == 'EUR'


def test_get_currency_rub():
    operation = {
        'operationAmount': {
            'amount': 300.00,
            'currency': {
                'name': 'RUB'
            }
        }
    }
    assert get_currency(operation) == 'RUB'


def test_get_currency_unknown_currency():
    operation = {
        'operationAmount': {
            'amount': 400.00,
            'currency': {
                'name': 'JPY'
            }
        }
    }
    assert get_currency(operation) == 'JPY'
