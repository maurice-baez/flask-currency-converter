from unittest.case import _AssertRaisesContext
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import Decimal

rates = CurrencyRates(force_decimal=True)
codes = CurrencyCodes()
# rates = CurrencyRates(force_decimal=True)


def check_currency_code(code):
    """ Check currency codes are valid """

    #check that a given code is valid


def convert_currency(convert_from_code, convert_to_code, amount):

        return rates.convert(convert_from_code, convert_to_code, Decimal(amount))


