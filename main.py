from PIL import Image, ImageChops, ImageGrab, ImageOps
import pytesseract
import pyautogui
import time
import re
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'path\\to\tesseract.exe'

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 1.3,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 1.5))

wowZones = {
  "allerianstron": "Outland",
  "altarofshatar": "Outland",
  "sylvan": "Outland",
  "cenarionrefuge": "Outland",
  "sylvtaanaar": "Outland",
  "aeriepeak": "Eastern Kingdoms",
  "azurewing": "Legion",
  "tarrenmil": "Eastern Kingdoms",
  "janel": "Legion",
  "conquesthold": "Northrend",
  "deliverancepoin": "Legion",
  "bradensbrook": "Legion",
  "esingwary": "Northrend",
  "onekeg": "Pandaria",
  "thundertotem": "Legion",
  "valiancekeep": "Northrend",
  "gadgetzan": "Kalimdor",
  "thundercleft": "Pandaria",
  "goldshir": "Eastern Kingdoms",
  "garadar": "Outland",
  "honorhold": "Outland",
  "tianmonastery": "Pandaria",
  "zabraj": "Outland",
  "halfhil": "Pandaria",
  "goldshire": "Eastern Kingdoms",
  "menethilharbo": "Eastern Kingdoms",
  "ramkahen": "Kalimdor",
  "thermoonstrong": "Kalimdor",
  "sentine": "Eastern Kingdoms",
  "area": "Outland",
  "shacklesden": "Legion",
  "longyingoutpo": "Pandaria",
  "thecrossroads": "Kalimdor",
  "tranquillien": "Eastern Kingdoms",
  "soggysgamble": "Pandaria",
  "frosthold": "Northrend",
  "stonard": "Eastern Kingdoms",
  "theargentstan": "Northrend",
  "warsonghold": "Northrend",
  "esingwarybasec": "Northrend",
  "dawnsblosso": "Pandaria",
  "zouchinvillage": "Pandaria",
  "wyrmresttempl": "Northrend",
  "everlook": "Kalimdor",
  "bril": "Eastern Kingdoms",
  "thrallmar": "Outland",
  "deliverancepoir": "Legion",
  "kamagua": "Northrend",
  "lorlathil": "Legion",
  "lordanel": "Kalimdor",
  "greywatch": "Legion",
  "cosmowrench": "Outland",
  "astranaar": "Kalimdor",
  "lionslanding": "Pandaria",
  "nordrassil": "Kalimdor",
  "bootybay": "Eastern Kingdoms",
  "valdisdall": "Legion",
  "skyhorn": "Legion",
  "camponeqwa": "Northrend",
  "meredil": "Legion",
  "klaxxivess": "Pandaria",
  "whisperwindgro": "Kalimdor",
  "moakiharbor": "Northrend",
  "nighthaven": "Kalimdor",
  "kharanos": "Eastern Kingdoms"  
}

myScreenshot = ImageGrab.grab()

starting_width = myScreenshot.size[0] * 22.23 / 100
starting_height = myScreenshot.size[1] * 58.33 / 100

gap = myScreenshot.size[0] * 10.94 / 100

del myScreenshot


input("Press any key to start:")

print("Starting in 3...")
time.sleep(1)
print("Starting in 2...")
time.sleep(1)
print("Starting in 1...")
time.sleep(1)

fails = 0
start_time = time.perf_counter()
end_time = start_time

while end_time - start_time < 60:
    readZone = []
    myScreenshot = ImageGrab.grab()
    myScreenshot = crop_center(myScreenshot, 1050, 220)
    myScreenshot = myScreenshot.convert('L')
    myScreenshot = ImageOps.invert(myScreenshot)

    strOfImg = pytesseract.image_to_string(np.array(myScreenshot), config='--psm 6')
    strOfImg2 = pytesseract.image_to_string(np.array(myScreenshot), config='--psm 13')
    
    readZone.append((re.sub("[^a-z\,A-Z]+", "", strOfImg)).lower())
    readZone.append((re.sub("[^a-z\,A-Z]+", "", strOfImg2)).lower())
       
    if fails > 2:
        pyautogui.moveTo(starting_width + gap*1, starting_height)
        pyautogui.click(button='right')
        fails = 0
    else:
        for key in wowZones:
            if key in readZone[0] or key in readZone[1]:
                del readZone
                if wowZones[key] == "Kalimdor":
                    pyautogui.moveTo(starting_width + gap*0, starting_height)
                    pyautogui.click(button='right')
                    fails = 0
                    break
                elif wowZones[key] == "Eastern Kingdoms":
                    pyautogui.moveTo(starting_width + gap*1, starting_height)
                    pyautogui.click(button='right')
                    fails = 0
                    break
                elif wowZones[key] == "Outland":
                    pyautogui.moveTo(starting_width + gap*2, starting_height)
                    pyautogui.click(button='right')
                    fails = 0
                    break
                elif wowZones[key] == "Northrend":
                    pyautogui.moveTo(starting_width + gap*3, starting_height)
                    pyautogui.click(button='right')
                    fails = 0
                    break
                elif wowZones[key] == "Pandaria":
                    pyautogui.moveTo(starting_width + gap*4, starting_height)
                    pyautogui.click(button='right')
                    fails = 0
                    break
                elif wowZones[key] == "Legion":
                    pyautogui.moveTo(starting_width + gap*5, starting_height)
                    pyautogui.click(button='right')
                    fails = 0
                    break
        else:
            fails = fails + 1
    time.sleep(0.6)
    end_time = time.perf_counter()
