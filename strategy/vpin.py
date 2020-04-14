# -*- coding: utf-8 -*-
import sys
import os

sys.path.append('./..')
import functions
import time
from API_Info import api_key
from datetime import datetime
import json


def main(param):
    pass


with open('./vpin.json') as f:
    param = json.load(f)

    main(param)
