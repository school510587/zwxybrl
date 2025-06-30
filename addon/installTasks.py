# Copyright (C) 2024-2025 ZhongWen XingYi Braille Core Team

from logHandler import log
import config

def onUninstall():
    if config.conf["braille"]["translationTable"] in ("zzh-tw---ncb_che.ctb", "zz-nosp.ctb", "zzh-tw---char.ctb"):
        log.info("Reset the braille output translation table to zh-tw.ctb.")
        config.conf["braille"]["translationTable"] = "zh-tw.ctb"
        config.conf.save()
