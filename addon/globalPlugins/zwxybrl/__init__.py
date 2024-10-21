# Copyright (C) 2024 ZhongWen XingYi Braille Core Team

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
        self.originalBRLtable = None
    @script(
        description=_("Quickly switches between XingYi braille and the current braille"),
        category=addonHandler.getCodeAddon().manifest["summary"],
    )
    def script_quickSwitchWithXYbrl(self, gesture):
        try:
            xyBRLtable = getBRLtable("zwxybrl.ctb")
        except:
            log.error("Failed to read the XingYi braille table.", exc_info=True)
            playErrorSound()
            return
        try:
            if braille.handler.table is not xyBRLtable:
                braille.handler.table, self.originalBRLtable = xyBRLtable, braille.handler.table
            elif self.originalBRLtable is not None and self.originalBRLtable is not xyBRLtable:
                braille.handler.table, self.originalBRLtable = self.originalBRLtable, None
            else: # The user has never set the braille output translation table to any other table since NVDA started.
                bopomofoBRLtable = getBRLtable("zh-tw.ctb")
                braille.handler.table, self.originalBRLtable = bopomofoBRLtable, None
            ui.message(_("The braille output translation table has been changed to: {0}").format(braille.handler.table.displayName))
        except:
            log.error("script_quickSwitchWithXYbrl performs no action.", exc_info=True)
            playErrorSound()
