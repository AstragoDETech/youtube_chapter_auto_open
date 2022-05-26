import subprocess

subprocess.call(
    "dart compile js .\lib\main.dart -o ./build/youtube_chapter_auto_open.user.js", shell=True)

code = ""
metaData = """// ==UserScript==
// @name        YouTube chapter auto open
// @description Automatically opens the YouTube chapter selecttion.
// @namespace   Violentmonkey Scripts
// @match       https://www.youtube.com/*
// @match       https://m.youtube.com/*
// @grant       none
// @version     1.0
// @author      AstragoDE (https://github.com/AstragoDE)
// @run-at      document-end
// ==/UserScript==

"""

with open("./build/youtube_chapter_auto_open.user.js", "r", encoding="UTF-8") as f:
    code = f.read()

with open("./build/youtube_chapter_auto_open.user.js", "w", encoding="UTF-8") as f:
    f.write(metaData + code)
