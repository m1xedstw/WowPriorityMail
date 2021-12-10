# WowPriorityMail

Python script that plays the mail game required for "Priority Mail" / "Post Haste" achievements in World of warcraft:
https://www.wowhead.com/postmaster-questline

The script works by creating a screenshot of the current displayed zone, reads the text off the screenshot using Tesseract OCR, then decides where to click by comparing the read value against all values in the wowZones dictionary.

How to use:

1) Run the script
2) Start the minigame in wow
3) Switch back to the script and press 'Enter' to start the countdown
4) Switch back to wow and let it do its thing
