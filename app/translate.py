import random
from hashlib import md5

import requests
from flask_babel import _
from iso639 import Language

from app import app


def make_md5(s, encoding="utf-8"):
    return md5(s.encode(encoding)).hexdigest()


def translate(text, source_language, dest_language):
    source_language = Language.from_part1(source_language).part2t
    dest_language = Language.from_part1(dest_language).part2t
    
    if (
        "TRANSLATION_APP_ID" not in app.config
        and "TRANSLATION_API_KEY" not in app.config
    ):
        return _("Error: the translation service is not configured.")

    appid = app.config["TRANSLATION_APP_ID"]
    api_key = app.config["TRANSLATION_API_KEY"]
    url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + text + str(salt) + api_key)

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = {
        "appid": appid,
        "q": text,
        "from": source_language,
        "to": dest_language,
        "salt": salt,
        "sign": sign,
    }

    r = requests.post(url, params=payload, headers=headers)
    return r.json()["trans_result"][0]["dst"]
