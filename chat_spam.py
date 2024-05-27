# Membuat spam_chat sederhana "hehe masih belajar"

# Library
import pyautogui
import keyword
import time

# Pesan sebelum memulai
print("Akan mulai dalam 5 detik")

# Jeda 5 detik sebelum memulai
time.sleep(5)

# Buka file dan lakukan operasi di dalam blok with
with open('spamfile.txt') as op:
    # Perulangan for untuk membaca baris demi baris dari file
    for line in op:
        pyautogui.typewrite(line)
        pyautogui.press('enter')
