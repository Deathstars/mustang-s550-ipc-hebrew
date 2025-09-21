# Mustang S550 IPC Hebrew Support

Add Hebrew language support to the Mustang S550 instrument cluster (IPC) by modifying fonts and firmware for proper Hebrew display.

---

## Installation

To install Hebrew language support on your IPC:

- Just flash all the files from the [Mustang Buillit Firmware Hebrew](https://github.com/Deathstars/mustang-s550-ipc-hebrew/tree/main/Mustang%20Buillit%20Firmware%20Hebrew) folder to your instrument cluster using UCDS or a compatible flashing tool.
- Once complete, your IPC will support Hebrew display.

> **Note:** This project was tested using UCDS to flash the IPC, but it may also work with other tools.

---

## Scripts

### [Extract_ttf_from_bin.py](https://github.com/Deathstars/mustang-s550-ipc-hebrew/blob/main/scripts/Extract_ttf_from_bin.py)

- Used to extract the font file (TTF) from the `.bin` that was extracted from the Ford VBF file, [JR3T-14C088-MC.vbf](https://github.com/Deathstars/mustang-s550-ipc-hebrew/blob/main/Mustang%20Buillit%20Firmware%20Hebrew/JR3T-14C088-MC.vbf).

### [Insert_font_from_source_to_dest_heb.py](https://github.com/Deathstars/mustang-s550-ipc-hebrew/blob/main/scripts/Insert_font_from_source_to_dest_heb.py)

- Used to copy a font from one font file to another font file.

---

## Extracted Fonts

In the [Extracted_fonts](https://github.com/Deathstars/mustang-s550-ipc-hebrew/tree/main/Extracted_fonts) folder you can find all the fonts extracted from the firmware.

---

## Disclaimer

This project is intended for research and personal use. Use at your own risk and always back up your original firmware before flashing any files to your vehicle.


---

## Images

### Before: Cluster Without Hebrew Support

**Image:** `IPC_Before_Hebrew.jpg`  
*The instrument cluster display before adding Hebrew support.*

![IPC Before Hebrew](https://raw.githubusercontent.com/Deathstars/mustang-s550-ipc-hebrew/refs/heads/main/Images/Before.jpg)

---

### Music: Hebrew Song Title Display

**Image:** `IPC_Music_Hebrew.jpg`  
*Demonstrates proper Hebrew rendering for music track titles.*

![Music Hebrew](https://raw.githubusercontent.com/Deathstars/mustang-s550-ipc-hebrew/refs/heads/main/Images/Music.jpg)

---

### Phone Call: Hebrew Caller Name

**Image:** `IPC_Phone_Hebrew.jpg`  
*Displays a phone call screen with the caller’s name in Hebrew.*

![Phone Hebrew](https://raw.githubusercontent.com/Deathstars/mustang-s550-ipc-hebrew/refs/heads/main/Images/Phone_Call.jpg)

---

### Reference: Hebrew Font Used

**Image:** `Hebrew_Font_Sample.jpg`  
*Reference view of the custom Hebrew font integrated into the IPC display.*

![Font Sample](https://raw.githubusercontent.com/Deathstars/mustang-s550-ipc-hebrew/refs/heads/main/Images/Font_File_view.jpg)
