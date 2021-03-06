def to_json(data):
    if isinstance(data, dict):
        out_str = "{"
        for key in data.keys():
            out_str += '"%s": %s, ' % (key, to_json(data[key]))

        out_str = out_str[:len(out_str) - 2]
        return out_str + "}"

    elif isinstance(data, list):
        some_str = "["
        for element in data:
            some_str += ', "%s"' % element
        some_str += "]"
        some_str = "[" + some_str[3:]
        return some_str

    elif isinstance(data, tuple):
        some_str = "["
        for element in data:
            some_str += ', "%s"' % element
        some_str += "]"
        some_str = "[" + some_str[3:]
        return some_str

    elif isinstance(data, str):
        return '"%s"' % data

    elif isinstance(data, int):
        return str(data)

    elif isinstance(data, float):
        return str(data)

    elif data:
        return "true"

    elif not data:
        return "false"

    elif data is None:
        return "null"

    else:
        return "incorrect input"


def main():
    print("\nDictionary:")
    print(to_json({"name": "Max", "age": 19, "sex": "male"}))

    print("\nTuple:")
    print(to_json(("Tree", "Apple")))

    print("\nTuple in dictionary:")
    print(to_json({"name": "Max", "age": 19, "sex": ("male", "female")}))

    print("\nString:")
    print(to_json("Check string working"))

    print("\nFloat numbers:")
    print(to_json(1234.1234))


main()
