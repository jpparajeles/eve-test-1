__author__ = 'josep'

import bcrypt

def pre_anvandaren_post_callback(request):
    print(request.data)

def ch_pass(list):
    for data in list:
        data["losenord"] = bcrypt.hashpw(data["losenord"], bcrypt.gensalt())
