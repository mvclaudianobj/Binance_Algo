import os

if (os.path.exists("binance_f/privateconfig.py")):
    from binance_f.privateconfig import *

    g_api_key = p_api_key
    g_secret_key = p_secret_key
else:
    g_api_key = "MzMpp87JoYDm7LnWFzugndSuvPBM5RdJ1BEoHNeBCcSUuVfKM5MzJpPFVxo24r3w"
    g_secret_key = "i4yIelhKoT5RCsXp5QyeETXI2TCym6ix3abJ4x1XrGrDhStFYbY7lMpjkcD63ToC"

g_account_id = 12345678
