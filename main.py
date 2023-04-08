from utlis import *
if __name__ == '__main__':

    last_five_sorted = sort_by_date()

    for operation in last_five_sorted:
        date_actual = get_date(operation)
        description = operation['description']
        sender = get_operation(operation)
        receiver = get_receiver(operation)
        amount = get_amount(operation)
        currency = get_currency(operation)
        print(f'{date_actual} {description}\n'
              f'{sender} -> {receiver}\n'
              f'{amount} {currency}\n')
        print()






















