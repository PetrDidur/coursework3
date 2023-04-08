import json


def get_all():
    with open("operations.json", encoding="utf-8") as f:
        data = json.load(f)
        return data


def sort_by_date():
    sorted_data = sorted(get_all(), key=lambda x: (x.get('date', ""), x.get('state', "")), reverse=True)
    executed_data = [op for op in sorted_data if op.get('state') == 'EXECUTED']
    last_five_sorted = executed_data[:5]
    return last_five_sorted


def get_date(operation):
    date = operation['date'].split('T')
    date_only = date[0].split('-')[::-1]
    date_actual = ",".join(date_only).replace(',', '.')
    return date_actual


def get_operation(operation):
    from_data = operation.get('from')
    if from_data is None:
        return f"No information"
    elif "Maestro" in from_data:
        from_data_actual = from_data.split(" ")
        card = from_data_actual[0]
        card_number = from_data_actual[1]
        blocks = [card_number[i:i + 4] for i in range(0, len(card_number), 4)]
        blocks_str = "".join(blocks)
        masked_number = blocks_str[:6] + '*'*(len(blocks_str) - 10) + blocks_str[-4:]
        return f"{card} {masked_number}"
    elif "Visa" in from_data:
        from_data_actual = from_data.split(" ")
        card = from_data_actual[0] + " " + from_data_actual[1]
        card_number = from_data_actual[2]
        blocks = [card_number[i:i + 4] for i in range(0, len(card_number), 4)]
        blocks_str = "".join(blocks)
        masked_number = blocks_str[:6] + '*' * (len(blocks_str) - 10) + blocks_str[-4:]
        return f"{card} {masked_number}"





