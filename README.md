# 🔑 MacLock: Physical Key Switch for macOS

This project is for anyone who wants to unlock their Mac (from the lock screen) using a physical key. As a bonus, you can set the key's second position to do one more custom action. For example, mine opens Gemini!

## 🛠️ Parts for this project:
- 1x **Arduino Nano**
- 1x **12mm Key Switch** (ON-ON-OFF)
- 3x **30cm M-F Jumper Wires** (we only need three from a 40-pin ribbon)
- **A project box** for a good look. (If you have a 3D printer, you can make a custom case. I didn't have one, so I just cut a cardboard box and it works great!)

## 🔌 How to build & Wiring:
1. Take three M-F jumper wires and cut the male parts off.
2. Strip the wires and connect them to the Key Switch.
3. Connect the other ends to the Arduino Nano like this:

| Key Switch Pin | Arduino Nano Pin |
| :--- | :--- |
| **Pin A** | `A2` |
| **Pin B** | `A3` |
| **Center** | `GND` |

## 💻 About the Software:
For this project, we are going to need two codes: one for the Arduino to monitor the switch, and a lightweight Python script running in the background on the Mac.

- **For monitoring codes:** I used the Arduino IDE to write and flash the code to the Nano.
- **For the background codes:** I wrote the Python listener script in Thonny.

> ⚠️ **WARNING!** 
> To make the Python listener script work automatically every time you start or wake your Mac, we need to use the **Automator** app (it comes pre-installed with Macs). This ensures the background process is always running!


