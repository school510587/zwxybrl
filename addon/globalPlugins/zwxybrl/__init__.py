# Copyright (C) 2024 ZhongWen XingYi Braille Core Team

import os

from logHandler import log
import characterProcessing
import globalPluginHandler
import globalVars

class CustomCharacterDescriptions(characterProcessing.CharacterDescriptions):
    def __init__(self, locale: str):
        old_appDir = globalVars.appDir
        if locale == "zh_TW":
            globalVars.appDir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
            log.info(f"Read {locale} character descriptions from: {globalVars.appDir}")
        try:
            super().__init__(locale)
        finally:
            globalVars.appDir = old_appDir

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self, *args, **kwargs):
        super(GlobalPlugin, self).__init__(*args, **kwargs)
        characterProcessing._charDescLocaleDataMap = characterProcessing.LocaleDataMap(CustomCharacterDescriptions)
