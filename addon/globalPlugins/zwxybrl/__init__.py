# Copyright (C) 2024-2025 ZhongWen XingYi Braille Core Team

import os

from brailleTables import getTable as getBRLtable
from logHandler import log
from nvwave import playErrorSound
from scriptHandler import script
import addonHandler
import braille
import characterProcessing
import globalPluginHandler
import globalVars
import ui

addonHandler.initTranslation()

xybrl_bimap = {
    "zh-tw.ctb": "zzh-tw---ncb_che.ctb",
    "zzh-tw---ncb_che.ctb": "zh-tw.ctb",
    "zz-nosp.ctb": "zh-tw.ctb",
    "zzh-tw---char.ctb": "zh-tw.ctb",
}

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
            if locale == "zh_TW" and braille.handler.table in map(getBRLtable, set(xybrl_bimap) - {"zh-tw.ctb"}):
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
    @script(
        description=_("Quickly switches between XingYi braille and the current braille"),
        category=addonHandler.getCodeAddon().manifest["summary"],
    )
    def script_quickSwitchWithXYbrl(self, gesture):
        if braille.handler.table.fileName not in xybrl_bimap:
            ui.message("No matching XingYi braille output translation table.")
            return
        try:
            target = getBRLtable(xybrl_bimap[braille.handler.table.fileName])
        except:
            log.error(f"Failed to find the target braille table: {braille.handler.table.fileName}", exc_info=True)
            playErrorSound()
            return
        braille.handler.table = target
        ui.message(_("The braille output translation table has been changed to: {0}").format(braille.handler.table.displayName))
