"""Functions for calculating steps in exchanging currency.

Python numbers documentation:
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling:
https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""


def exchange_money(budget, exchange_rate):
    """Calculate the amount of foreign currency received.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Calculate the remaining money after exchanging some.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Calculate the total value of the received bills.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """Determine how many whole bills can be obtained from the amount.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """Calculate the leftover amount that cannot be exchanged into full bills.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    return float(amount % denomination)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate the maximum value you can get from your budget in full bills,
    after applying the exchange rate and spread fee.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    # Adjust the exchange rate by adding the spread.
    adjusted_exchange_rate = exchange_rate * (1 + spread / 100)

    # Calculate how much foreign currency you can get with your budget
    total_foreign = budget / adjusted_exchange_rate

    # Get the number of whole bills you can receive
    number_of_bills = total_foreign // denomination

    # Multiply by denomination to get total value
    return int(number_of_bills * denomination)
