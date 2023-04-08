from utlis import *
if __name__ == '__main__':

    last_five_sorted = sort_by_date()

    for operation in last_five_sorted:
        #print(operation)
        result = ''
        date_actual = get_date(operation)
        description = operation['description']
        card_number = get_operation(operation)
        print(card_number)















