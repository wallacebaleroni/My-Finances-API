def get_field(content, field, required=False, is_number=False):
    if required and field not in content.keys():
        raise KeyError("{0} field is required".format(field))

    value = content.get(field)
    if is_number:
        if value is None:
            return value
        else:
            return int(value)
    else:
        if value is None:
            return ""
        else:
            return value
