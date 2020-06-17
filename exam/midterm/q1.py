# Investment Bond Question

import numbers
import collections
import copy


def is_number(x):
    return isinstance(x, numbers.Number)


def is_zero_or_positive(x):
    return (x >= 0)


def is_positive(x):
    return (x > 0)


def is_keys_present(key_list, dict_ref):
    return all(key in dict_ref for key in key_list)


def calculate_ytm(price, face_value, duration):
    return round(((face_value / price) ** (1 / duration)) - 1, 4)


def calculate_price(ytm, face_value, duration):
    return round(face_value / ((1 + ytm) ** duration), 2)


def is_dictionary_ok(dict_ref):
    valid_keys = ["price", "duration", "ytm", "face_value"]

    if isinstance(dict_ref, collections.abc.Mapping):
        if is_keys_present(valid_keys, dict_ref):
            if all(is_number(value) for value in dict_ref.values()):
                if all(is_zero_or_positive(value) for value in dict_ref.values()):
                    if is_positive(dict_ref["duration"]) and is_positive(dict_ref["face_value"]):
                        if is_positive(dict_ref["price"]) or is_positive(dict_ref["ytm"]):
                            return True

    return False


def calculate_bond(dict_ref):
    if not is_dictionary_ok(dict_ref):
        return None

    output = copy.deepcopy(dict_ref)

    if dict_ref["price"] == 0:
        output["price"] = calculate_price(
            dict_ref["ytm"], dict_ref["face_value"], dict_ref["duration"])

    elif dict_ref["ytm"] == 0:
        output["ytm"] = calculate_ytm(
            dict_ref["price"], dict_ref["face_value"], dict_ref["duration"])

    return output
