def deepupdate(base_dict, update_with):

    for key, value in update_with.items():
        if isinstance(value, dict):
            base_dict[key] = deepupdate(base_dict.get(key, {}), value)
        else:
            base_dict[key] = value

    return base_dict
