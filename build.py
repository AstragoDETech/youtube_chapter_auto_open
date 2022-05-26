import subprocess

version = "1.0.3"

# ============================================

subprocess.call(
    "dart compile js .\lib\main.dart -o ./build/youtube_chapter_auto_open.user.js", shell=True)

code = ""
metaData = f"""// ==UserScript==
// @name        YouTube chapter auto open
// @description Automatically opens the YouTube chapter selection.
// @namespace   Violentmonkey Scripts
// @match       https://www.youtube.com/*
// @match       https://m.youtube.com/*
// @grant       none
// @version     {version}
// @author      AstragoDE (https://github.com/AstragoDE)
// @run-at      document-end
// @downloadURL https://github.com/AstragoTech/youtube_chapter_auto_open/raw/main/build/youtube_chapter_auto_open.user.js
// @updateURL   https://github.com/AstragoTech/youtube_chapter_auto_open/raw/main/build/youtube_chapter_auto_open.user.js
// @homepageURL https://github.com/AstragoTech/youtube_chapter_auto_open
// @icon        https://www.google.com/s2/favicons?domain=youtube.com
// @compatible  chrome Chrome + Tampermonkey or Violentmonkey
// @compatible  firefox Firefox + Greasemonkey or Tampermonkey or Violentmonkey
// @compatible  opera Opera + Tampermonkey or Violentmonkey
// @compatible  edge Edge + Tampermonkey or Violentmonkey
// @compatible  safari Safari + Tampermonkey or Violentmonkey
// ==/UserScript==

"""

with open("./build/youtube_chapter_auto_open.user.js", "r", encoding="UTF-8") as f:
    code = f.read()

with open("./build/youtube_chapter_auto_open.user.js", "w", encoding="UTF-8") as f:
    f.write(metaData + code)
