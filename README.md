# vSpoofer

Python HWID Spoofer for 64-bit Windows (only tested on Windows 11)

You can download the two essential programs and the sys file if you don't trust them

AMIDEWINx64.exe & amifldrv64.sys are from [here](https://download.schenker-tech.de/package/dmi-edit-efi-ami/) made by [AMI](https://www.ami.com/)

Volumeid.exe is a [Sysinternal](https://learn.microsoft.com/en-us/sysinternals/) tool from [here](https://learn.microsoft.com/en-us/sysinternals/downloads/volumeid)

## Importart

The spoofer doesn't support MAC spoofing yet until then use something like [Technitium MAC Address Changer](https://technitium.com/tmac/)

## Features

### Spoofers
- Spoof System UUID
- Spoof System Serial Number
- Spoof Baseboard Serial Number
- Spoof CPU Serial Number
- Spoof Disk Serial Number
- Spoof PC Name (if you have Autologon set up it will stop working)
- Spoof GUID
- Spoof Product ID

### Cleaners
- Clean Ubisoft Cache
- Clean Valorant Cache
- Clean Battle.net Cache

## Run Locally

### Run terminal as administrator

```batch
  git clone https://github.com/vincuska/vSpoofer
  cd sudoku
```

```batch
  python main.py
```
