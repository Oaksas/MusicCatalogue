from utils.collections import deepupdate
from utils.settings import get_settings_from_environment

"""
This takes env variables with a matching prefix, strips away the prefix, and then adds it to the gloabal

example:
export CORESETTING_DEBUG=True

Could be referenced as global as:
DEBUG


"""

deepupdate(globals(), get_settings_from_environment(ENVVAR_PREFIX))  # type: ignore
