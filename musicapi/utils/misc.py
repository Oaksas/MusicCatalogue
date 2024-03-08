import yaml


def yaml_coerce(value):
    # convert value into python
    if isinstance(value, str):
        # yaml.load returns a Python object from the yaml string
        # Converts a str dict to a Python dict
        # Useful because sometimes we need to stringify settings this way (like in Dockefiles)
        return yaml.load(f'dummy:{value}', Loader=yaml.SafeLoader)['dummy']
    return value
