__author__ = 'josep'

import bcrypt


def ch_pass(list):
    for data in list:
        data["losenord"] = bcrypt.hashpw(data["losenord"], bcrypt.gensalt())
