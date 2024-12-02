#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7900562773:AAFV8bK5vUhc3l2KBiNum3kbIo4nDc9jldc")
    API_ID = int(os.environ.get("API_ID", "26512964"))
    API_HASH = os.environ.get("API_HASH", "e5d187c6c7a0919ccb8866f76f655701")
    AUTH_USERS = "7246728595"

