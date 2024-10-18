# Copyright (C) 2024 ZhongWen XingYi Braille Core Team

import os

from brailleTables import getTable as getBRLtable
from logHandler import log
import braille
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

class CustomLocaleDataMap(characterProcessing.LocaleDataMap):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._xyCharDescLocaleDataMap = characterProcessing.LocaleDataMap(CustomCharacterDescriptions)
    def fetchLocaleData(self, locale: str, *args, **kwargs):
        try:
            if locale == "zh_TW" and braille.handler.table is getBRLtable("zwxybrl.ctb"):
                return self._xyCharDescLocaleDataMap.fetchLocaleData(locale, *args, **kwargs)
        except:
            log.error("Failed to read XingYi character descriptions", exc_info=True)
        return super().fetchLocaleData(locale, *args, **kwargs)
    def invalidateLocaleData(self, locale: str, *args, **kwargs):
        self._xyCharDescLocaleDataMap.invalidateLocaleData(locale, *args, **kwargs)
        return super().invalidateLocaleData(locale, *args, **kwargs)

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self, *args, **kwargs):
        super(GlobalPlugin, self).__init__(*args, **kwargs)
        characterProcessing._charDescLocaleDataMap = CustomLocaleDataMap(characterProcessing.CharacterDescriptions)
