# Copyright (C) 2024 ZhongWen XingYi Braille Core Team

from brailleTables import getTable as getBRLtable
from logHandler import log
import braille
import config

def onUninstall():
    if braille.handler.table is getBRLtable("zwxybrl.ctb"):
        braille.handler.table = getBRLtable("zh-tw.ctb")
        log.info("Returned the translation table object.")
    if config.conf["braille"]["translationTable"] == "zwxybrl.ctb":
        config.conf["braille"]["translationTable"] = "zh-tw.ctb"
        config.conf.save()
        log.info("Returned the translation table configuration.")
