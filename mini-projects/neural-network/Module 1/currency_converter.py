conversions = {
    "USD": 1,
    "EUR": .9,
    "CAD": 1.4,
    "GBP": .9,
    "REAL": .35,
    "JPY": 1.9,
}


def currency_converter(quantity: float, source_curr: str, target_curr: str):
    if quantity <= 0:
        raise ValueError
    in_usd = quantity / conversions[source_curr]
    in_target = in_usd * conversions[target_curr]
    return in_target


def main():
    euros = float(input("How many Euros do you want to converto to dollars?  "))
    print(f"{euros:.2f} Euros is "
          f"{currency_converter(euros, 'EUR', 'USD'):.2f} dollars")


if __name__ == "__main__":
    main()
