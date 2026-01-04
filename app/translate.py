import random
from hashlib import md5

import requests
from flask import current_app
from flask_babel import _


def make_md5(s, encoding="utf-8"):
    return md5(s.encode(encoding)).hexdigest()


def translate(text, source_language, dest_language):
    # Dealing with the differences in encoding recognized by Baidu Translation and langdetect
    language_mapper = {"zh": "zh", "en": "en", "fr": "fra", "ja": "jp", "de": "de"}

    if (
        "TRANSLATION_APP_ID" not in current_app.config
        and "TRANSLATION_API_KEY" not in current_app.config
    ):
        return _("Error: the translation service is not configured.")

    appid = current_app.config["TRANSLATION_APP_ID"]
    api_key = current_app.config["TRANSLATION_API_KEY"]
    url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + text + str(salt) + api_key)

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = {
        "appid": appid,
        "q": text,
        "from": language_mapper.get(source_language, "auto"),
        "to": language_mapper.get(dest_language, dest_language),
        "salt": salt,
        "sign": sign,
    }

    try:
        r = requests.post(url, params=payload, headers=headers)
        return r.json()["trans_result"][0]["dst"]
    except Exception as exc:
        raise f"The translation service is failed: {exc}"
