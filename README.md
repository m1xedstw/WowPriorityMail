# WowPriorityMail
Python script that plays the mail game required for "Priority Mail" / "Post Haste" achievements

The script works by creating a screenshot of the current displayed zone, reads the text off the screenshot using Tesseract OCR, then decides where to click by comparing the read value against all values in the wowZones dictionary.
