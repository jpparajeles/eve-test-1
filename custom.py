import bcrypt
import datetime
__author__ = 'josep'


def ch_pass(list):
    for data in list:
        data["losenord"] = bcrypt.hashpw(data["losenord"], bcrypt.gensalt())


def ch_pass_u(update, _):
    update["losenord"] = bcrypt.hashpw(update["losenord"], bcrypt.gensalt())


def log_log(list):
    for data in list:
        data["Date"] = str(datetime.datetime.now())
