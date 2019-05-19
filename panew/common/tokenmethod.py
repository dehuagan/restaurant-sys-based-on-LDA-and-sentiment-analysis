
import time
def encryptoken(password):
    datetime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    password_hash = password + datetime
    return password_hash

