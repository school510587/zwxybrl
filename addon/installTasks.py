# Copyright (C) 2024 ZhongWen XingYi Braille Core Team

from logHandler import log
import config

def onUninstall():
    if config.conf["braille"]["translationTable"] == "zwxybrl.ctb":
        log.info("Reset the braille output translation table to zh-tw.ctb.")
        config.conf["braille"]["translationTable"] = "zh-tw.ctb"
        config.conf.save()
