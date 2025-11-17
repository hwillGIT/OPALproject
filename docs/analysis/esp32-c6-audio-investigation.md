ESP32-C6 Touch LCD 1.69" Audio System Investigation Report
Executive Summary
Date: November 2025
Board: Waveshare ESP32-C6-Touch-LCD-1.69
Issue: No audio output - only clicking sound
Root Cause: NS4150B amplifier control pins floating (hardware design flaw)
Hardware Architecture
Audio Signal Path
ES8311 Codec → NS4150B Amplifier → Speaker
    ↓              ↓
  I2S Data    Control Pins
   (Working)   (FLOATING!)
Component Analysis
ES8311 Audio Codec (Working ✅)

Status: Properly configured and functional
I2C Communication: Working at address 0x18
I2S Interface: Data transmitting correctly
Output Pins:

OUTP (Pin 12) → 100nF → 150K → NS4150B IN+
OUTN (Pin 13) → 100nF → 150K → NS4150B IN-



NS4150B Class-D Amplifier (Not Working ❌)

Issue: Control pins are floating/unconnected
Pin 1 (CTRL): No connection - Should be HIGH to enable
Pin 2 (Bypass): No connection - Should be LOW for normal operation
Result: Amplifier in undefined state, producing only power-on click

Problem Details
Symptoms

Single click sound when powered on
No audio output despite:

Codec properly configured
I2S data transmitting (800+ buffers)
Volume at 100%
DAC enabled and unmuted



Root Cause Analysis
The NS4150B amplifier control pins are completely floating in the schematic:

No GPIO connections
No pull-up/pull-down resistors
No test points provided
Apparent design oversight

Why Only a Click?
When power is applied, the floating control pins momentarily pick up charge (causing the click), then settle to an undefined state that disables the amplifier.
Solutions
Solution 1: Hardware Modification (Immediate Fix)
Add external pull resistors to force proper logic levels:
NS4150B Pin 1 (CTRL) → 10KΩ → 3.3V (Enable amplifier)
NS4150B Pin 2 (Bypass) → 10KΩ → GND (Normal operation)
Implementation:

Use 30-36 AWG magnet wire
Solder directly to NS4150B pins (likely MSOP-8 package)
Add 10KΩ resistors to appropriate rails

Solution 2: GPIO Control (Permanent Fix)

Find two unused GPIOs on ESP32-C6
Solder wires from GPIOs to NS4150B control pins
Control amplifier in software:

cpp#define PA_CTRL_PIN    GPIO_NUM_XX  // Choose free GPIO
#define PA_BYPASS_PIN  GPIO_NUM_XX  // Choose free GPIO

void init_amplifier() {
    gpio_config_t io_conf = {};
    io_conf.pin_bit_mask = (1ULL << PA_CTRL_PIN) | (1ULL << PA_BYPASS_PIN);
    io_conf.mode = GPIO_MODE_OUTPUT;
    io_conf.pull_up_en = GPIO_PULLUP_DISABLE;
    io_conf.pull_down_en = GPIO_PULLDOWN_DISABLE;
    gpio_config(&io_conf);

    gpio_set_level(PA_CTRL_PIN, 1);    // Enable amplifier
    gpio_set_level(PA_BYPASS_PIN, 0);  // Normal operation
}
Solution 3: Alternative Hardware

Looking for alternatives with WiFi, Bluetooth, LCD Touch, and working audio that match the ESP32-C6's capabilities:

Direct ESP32-C6 Alternatives with Display + Audio

1. ESP32-S3-BOX-3 (Espressif Official) ⭐ BEST MATCH

MCU: ESP32-S3 (WiFi 802.11n, BLE 5.0)
Display: 2.4" IPS capacitive touch (320×240)
Audio: ES8311 codec + DPA17211 amplifier (PROPERLY WIRED!)
Wireless: 2.4GHz WiFi, BLE 5.0 + Mesh
Extras: 2 mics, speaker included, 16MB Flash, 8MB PSRAM
Price: ~$45
Why Better: Same codec, working amplifier control, official support

2. M5Stack CoreS3 (Latest 2024 Model)

MCU: ESP32-S3FN16R8 (WiFi, BLE 5.0)
Display: 2.0" IPS capacitive touch (320×240)
Audio: AW88298 I²S amplifier with proper enable control
Wireless: 2.4GHz WiFi, BLE 5.0
Extras: Camera, IMU, mic, RTC, battery
Price: ~$65
Why Better: Everything integrated and tested

3. LILYGO T-Deck Plus (2024)

MCU: ESP32-S3 (WiFi, BLE 5.0)
Display: 2.8" capacitive touch
Audio: I2S with MAX98357A (auto-enable)
Wireless: WiFi + BLE 5.0 + optional LoRa
Extras: Keyboard, trackball, battery
Price: ~$50
Why Better: Unique form factor, proven audio

ESP32-C6 Specific Boards (Newer Options)

4. Seeed Studio XIAO ESP32-C6 + Expansion

MCU: ESP32-C6 (WiFi 6, BLE 5.3, Zigbee)
Display: Add Round Display for XIAO (1.28" touch)
Audio: Add Grove Speaker module
Wireless: WiFi 6, BLE 5.3, 802.15.4
Build: Modular but reliable
Price: $5 + $15 display + $10 audio
Why Better: Same C6 chip, modular approach works

5. ESP32-C6-DevKitC-1 + Waveshare Display + Audio

MCU: ESP32-C6FH4
Display: Add Waveshare 2.8" Touch ESP32 display
Audio: Add Adafruit MAX98357 breakout
Wireless: WiFi 6, BLE 5.3, Thread/Zigbee
Price: $10 + $25 + $8
Why Better: Official dev board, proven modules

High-End Integrated Solutions

6. Elecrow ESP32-S3 Terminal (3.5" or 5")

MCU: ESP32-S3-WROOM-1
Display: 3.5" or 5" capacitive touch (480×320/800×480)
Audio: Built-in I2S amplifier with enable control
Wireless: WiFi, BLE 5.0
Extras: RS485, CAN bus, multiple I/O
Price: $60-90
Why Better: Industrial quality, everything works

7. LILYGO T-Display-S3 Pro

MCU: ESP32-S3R8 (WiFi, BLE 5.0)
Display: 2.33" IPS touch (320×480)
Audio: I2S interface + MAX98357A option
Wireless: WiFi + BLE 5.0
Extras: 16MB Flash, 8MB PSRAM, battery support
Price: ~$35
Why Better: Modern design, good support

Comparison with ESP32-C6 Features

| Feature | ESP32-C6 (Your Board) | Best Alternatives |
|---------|----------------------|-------------------|
| WiFi | WiFi 6 (802.11ax) | S3: WiFi 4/5, C6: WiFi 6 |
| Bluetooth | BLE 5.3 | S3: BLE 5.0, C6: BLE 5.3 |
| MCU | RISC-V 160MHz | S3: Dual Xtensa 240MHz |
| Display | 1.69" ST7789V2 | 2.0"-5.0" options |
| Touch | CST816T | Various capacitive |
| Audio Codec | ES8311 ❌ Broken | ES8311 ✅ Working |
| Amplifier | NS4150B ❌ Floating | Properly connected |
| Thread/Zigbee | Yes | C6 boards: Yes, S3: No |

My Top 3 Recommendations

1. ESP32-S3-BOX-3 ⭐⭐⭐⭐⭐
   - Why: Same ES8311 codec, working amplifier, official Espressif support, extensive documentation
   - Pros: Everything works out-of-box, AI voice examples
   - Cons: Slightly older WiFi (not WiFi 6)

2. M5Stack CoreS3 ⭐⭐⭐⭐
   - Why: Premium build, integrated everything, huge ecosystem
   - Pros: Best integration, UIFlow visual programming
   - Cons: More expensive, closed ecosystem

3. Seeed XIAO ESP32-C6 + Modules ⭐⭐⭐⭐
   - Why: Exact same ESP32-C6, modular approach ensures working audio
   - Pros: Latest C6 features, Thread/Zigbee support
   - Cons: Requires assembly, smaller display options

Important Audio Considerations

When evaluating alternatives, check for:

- Amplifier Enable Pin Connected: Must be GPIO-controlled
- I2S Pin Availability: MCLK, BCLK, WS, DATA all connected
- Proper Power Design: Separate analog/digital grounds
- Speaker Included or Specified: Know the impedance requirements

Development Ecosystem

Best supported platforms:

- Espressif (ESP32-S3-BOX): ESP-IDF, ESP-ADF audio framework
- M5Stack: Arduino, UIFlow, MicroPython
- Adafruit: CircuitPython, extensive tutorials
- LILYGO: Arduino, good GitHub examples

For your specific needs (working audio + display + wireless), the ESP32-S3-BOX-3 is strongly recommended as it's essentially what the current board should have been - same codec, but with properly connected amplifier controls and official Espressif support.

Verification Checklist
Before Hardware Modification:

 Measure NS4150B Pin 1 & 2 voltages
 Check for unpopulated resistor pads
 Look for solder jumpers on PCB bottom
 Verify speaker connection continuity

After Modification:

 NS4150B Pin 1 = 3.3V (enabled)
 NS4150B Pin 2 = 0V (not bypassed)
 Audio output verified with tone generator
 No excessive current draw

Test Code
cpp// Simple tone generator to verify audio after fix
#include "driver/i2s.h"
#include <math.h>

#define SAMPLE_RATE 48000
#define FREQUENCY   440  // A4 note

void generate_tone() {
    int16_t samples[256];

    for(int i = 0; i < 256; i++) {
        float sample = sin(2.0 * M_PI * FREQUENCY * i / SAMPLE_RATE);
        samples[i] = (int16_t)(sample * 32767);
    }

    size_t bytes_written;
    while(1) {
        i2s_write(I2S_NUM_0, samples, sizeof(samples),
                  &bytes_written, portMAX_DELAY);
    }
}
Lessons Learned
Design Review Points:

Always verify amplifier control pins are properly connected
Check for floating pins in audio signal path
Ensure test points for critical signals
Review reference designs from chip manufacturers

Red Flags in Schematics:

Unconnected amplifier control pins
Missing pull-up/pull-down resistors
No GPIO assignments for enable signals
Lack of test points for debugging

Conclusion
The Waveshare ESP32-C6-Touch-LCD-1.69 board has a fundamental design flaw where the NS4150B amplifier control pins are left floating. This renders the audio system non-functional despite the codec being properly configured.
Immediate Action: Add pull resistors to NS4150B control pins
Long-term Solution: Consider alternative hardware with properly designed audio systems
References
Datasheets:

ES8311 Low Power Audio Codec
NS4150B Class-D Audio Amplifier
ESP32-C6 Series Datasheet

Related Documentation:

ESP32-C6-Touch-LCD-1.69 Schematic
I2S Driver Documentation
ESP-IDF Audio Framework
