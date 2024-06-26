class API:
    @classmethod
    def get_data(cls):
        lines = open('aa').readlines()
        #print(f"get_data: lines: {lines}")
        return lines


def get_only_numbers():
    #lines = API.get_data()
    #print(f"get_only_numbers: lines: {lines}")
    numbers = []
    for line in API.get_data():
        #print(f"line: {line}", end='')  # line je řetězec
        #line_items = line.split(',')    # line_items je seznam řetězců
        #print(f"line_items: {line_items}")
        """for line_item in line.split(','):
            #print(f"line_item: {line_item.strip()}")
            if line_item.strip().isdigit():
            #if isinstance(line_item, int):
                numbers.append(line_item.strip())"""

        numbers.extend([line_item.strip() for line_item in line.split(',') if line_item.strip().isdigit()])

    """numbers_to_return = ""   # "1|4|5|25|23|4|324|24|1|23|545|32"
    for number in numbers:
        numbers_to_return += number
        numbers_to_return += '|'
    return numbers_to_return[:-1]"""
    return '|'.join(numbers)


if __name__ == "__main__":
    print(get_only_numbers())
