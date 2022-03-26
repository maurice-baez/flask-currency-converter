from tabnanny import check
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import Decimal

from functions import check_currency_code, convert_currency

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"

rates = CurrencyRates(force_decimal=True)
codes = CurrencyCodes()


@app.get("/")
def render_home():

    return render_template("index.html")


@app.get("/convert")
def get_conversion():

    convert_from_code = request.args.get("convert-from")
    convert_to_code = request.args.get("convert-to")
    amount = float(request.args.get("amount"))

    check_currency_code(convert_from_code)
    check_currency_code(convert_to_code)

    conversion = convert_currency(convert_from_code, convert_to_code, amount)

    symbol = codes.get_symbol(convert_to_code)


    return render_template("show-conversion.html", conversion = conversion, symbol = symbol)