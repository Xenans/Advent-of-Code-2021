file = open('./Day 16/input.txt', 'r')
input = file.read().strip()
# print(input)


def pop_header(data):
    packet_version = data[:3]
    packet_id = data[3:6]
    data = data[6:]
    return data, packet_version, packet_id


def pop_literal(data):
    literal = ''
    end = False
    while not end:
        group = data[:5]
        data = data[5:]
        end = group[0] == '0'
        literal += group[1:]
    value = [int(literal, 2)]
    return data, value


def pop_operator(data):
    length_type = data[0]
    data = data[1:]
    version_sum = 0
    values = []
    if length_type == '0':
        # Next 15 bits indicate total length of bits
        length = int(data[:15], 2)
        data = data[15:]
        consumed_data = data[:length]
        while consumed_data:
            consumed_data, temp_values, temp_version = pop_packet(
                consumed_data)
            version_sum += temp_version
            values.extend(temp_values)
        data = data[length:]
    else:  # length_type == '1'
        # Next 11 bits represent number of sub-packets contained
        packet_count = int(data[:11], 2)
        data = data[11:]
        for i in range(packet_count):
            data, temp_values, temp_version = pop_packet(data)
            version_sum += temp_version
            values.extend(temp_values)

    return data, values, version_sum


def pop_packet(data):
    data, packet_version, packet_id = pop_header(data)
    version_sum = int(packet_version, 2)
    id_int = int(packet_id, 2)
    values = []
    if id_int == 0:
        data, values, temp_version = pop_operator(data)
        version_sum += temp_version
        print('Trying to sum', values)
        values = [sum(values)]
    elif id_int == 1:
        data, values, temp_version = pop_operator(data)
        version_sum += temp_version
        product = 1
        for value in values:
            product *= value
        values = [product]
    elif id_int == 2:
        data, values, temp_version = pop_operator(data)
        version_sum += temp_version
        values = [min(values)]
    elif id_int == 3:
        data, values, temp_version = pop_operator(data)
        version_sum += temp_version
        values = [max(values)]
    elif id_int == 4:
        # Do literal stuff
        print('Literal detected:', packet_version, packet_id)
        data, value = pop_literal(data)
        values.extend(value)
    elif id_int == 5:
        data, values, temp_version = pop_operator(data)
        version_sum += temp_version
        values = [values[0] > values[1]]
    elif id_int == 6:
        data, values, temp_version = pop_operator(data)
        version_sum += temp_version
        values = [values[0] < values[1]]
    elif id_int == 7:
        data, values, temp_version = pop_operator(data)
        version_sum += temp_version
        values = [values[0] == values[1]]

    else:
        print('ERROR INCORRECT ID DETECTED')
        data, values, temp_version = pop_operator(data)
        version_sum += temp_version
    return data, values, version_sum


# input = '9C0141080250320F1802104A08'

integer = int(input, 16)
length = 4 * len(input)
data = f'{integer:0>{length}b}'
print(data)
output = pop_packet(data)
print(output)


# For each packet:
# Pop the first 3 bits of the string to get version
# Pop the next 3 bits of the string to get ID

# ID 1: Operator
# ID 2: Operator
# ID 3: Operator
# Pop a single bit: length type ID
# If 0, then next 15 bits is the number of bits for the packet
# If 1, then next 11 bits is number of sub-packets inside

# ID 4: Literal
# Continously pop in groups of 5 until the leading bit of the group is 0
