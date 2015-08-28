__author__ = 'josep'

import bcrypt
import datetime


def ch_pass(list):
    for data in list:
        data["losenord"] = bcrypt.hashpw(data["losenord"], bcrypt.gensalt())

def log_log(list):
    for data in list:
        data["Date"]=str(datetime.datetime.now())