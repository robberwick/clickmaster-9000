# ClickMaster 9000: Rotary Edition

## Overview

The ClickMaster 9000: Rotary Edition is a custom 12-key macropad with a rotary encoder and OLED display. Built with efficiency and customization in mind, this compact device allows you to program macros, shortcuts, and special functions to streamline your workflow.

Powered by the KMK firmware (CircuitPython-based), the ClickMaster 9000 is highly customizable and easy to program without requiring advanced programming skills.

## Features

- **12-Key Layout**: Mechanical switches for satisfying typing experience
- **Rotary Encoder**: For volume control, scrolling, or other dial-based inputs
- **OLED Display**: Shows current layer, status, and custom graphics
- **KMK Firmware**: CircuitPython-based for easy customization
- **Multiple Layers**: Switch between different key configurations

## Hardware Specifications

- Microcontroller: Seeed XIAO RP2040
- OLED: 128x64 pixel display
- Rotary Encoder

## Setup and Installation

### Prerequisites

- CircuitPython-compatible board
- CircuitPython installed on your board
- Basic understanding of Python (helpful but not required)

### Installation Steps

1. Install CircuitPython on your Seeed XIAO RP2040
   - Download the latest CircuitPython UF2 file for XIAO RP2040 from the [CircuitPython website](https://circuitpython.org/board/seeeduino_xiao_rp2040/)
   - Connect the XIAO RP2040 to your computer while pressing the BOOT button
   - Drag and drop the UF2 file to the RPI-RP2 drive that appears
   - The board will restart and a CIRCUITPY drive will appear

2. Install KMK Firmware
   ```bash
   # Clone the KMK repository
   git clone https://github.com/KMKfw/kmk_firmware.git
   
   # Copy KMK files to your CIRCUITPY drive
   cp -r kmk_firmware/kmk /path/to/CIRCUITPY/
   cp -r kmk_firmware/boot.py /path/to/CIRCUITPY/
   ```

3. Copy the ClickMaster firmware files from this repository to your CIRCUITPY drive
   ```bash
   cp code.py /path/to/CIRCUITPY/
   cp -r lib/* /path/to/CIRCUITPY/lib/
   ```

4. Your macropad should restart and load the new firmware

## Customization

The ClickMaster 9000 is designed to be easily customizable. Modify the `code.py` file to change key mappings, rotary encoder functionality, or OLED display content.
