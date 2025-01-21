# Key Programmer GUI

A Python-based GUI application for programming car keys and bypassing immobilizers using the OBDLink SX interface.

## Features

- Support for multiple vehicle manufacturers
- Key programming operations:
  - Add new key
  - Immobilizer bypass
  - Read key count
  - Clear all keys
- Real-time command logging
- Modern dark theme UI
- Extensible vehicle database

## Supported Vehicles

### Volkswagen
- Golf (2010-2023)
- Polo (2010-2023)
- Passat (2010-2023)
- Transporter (2010-2023)
- Tiguan (2010-2023)
- T-Cross (2018-2023)

### SEAT
- Ibiza (2010-2023)

### Skoda
- Octavia (2010-2023)
- Kodiaq (2016-2023)
- Superb (2010-2023)
- Fabia (2010-2023)

### Hyundai
- Elantra (2010-2023)
- Sonata (2010-2023)
- Tucson (2010-2023)
- Accent (2010-2023)
- Venue (2010-2023)
- Ioniq (2016-2023)
- Kona (2010-2023)
- i20 (2010-2023)
- i30 (2010-2023)
- Getz (2010-2023)

### Kia
- Sportage (2010-2023)
- Optima (2010-2023)
- Sorento (2010-2023)
- Pride (2010-2023)
- Picanto (2010-2023)

### Peugeot
- 208 (2012-2023)
- 308 (2010-2023)
- 3008 (2010-2023)
- 5008 (2010-2023)
- Partner (2010-2023)
- Rifter (2018-2023)

### Citroen
- C3 (2010-2023)
- C4 (2010-2023)
- C5 (2010-2023)

### BMW
- 3 Series (2010-2023)
- 5 Series (2010-2023)
- X3 (2010-2023)
- X5 (2010-2023)

### Mercedes
- C-Class (2010-2023)
- E-Class (2010-2023)
- GLC (2015-2023)
- GLE (2015-2023)

### Audi
- A3 (2010-2023)
- A4 (2010-2023)
- A6 (2010-2023)
- Q5 (2010-2023)

### Ford
- Focus (2010-2023)
- Fiesta (2010-2023)
- Mondeo (2010-2023)
- Kuga (2010-2023)

### Chevrolet
- Cruze (2010-2023)
- Malibu (2010-2023)
- Spark (2010-2023)
- Aveo (2010-2023)

### Fiat
- 500 (2010-2023)
- Panda (2010-2023)
- Tipo (2015-2023)
- Punto (2010-2023)

### Renault
- Clio (2010-2023)
- Megane (2010-2023)
- Captur (2013-2023)
- Kadjar (2015-2023)

### Opel/Vauxhall
- Corsa (2010-2023)
- Astra (2010-2023)
- Insignia (2010-2023)
- Mokka (2012-2023)

### Toyota
- Corolla (2010-2023)
- Camry (2010-2023)
- RAV4 (2010-2023)
- Yaris (2010-2023)

### Honda
- Civic (2010-2023)
- Accord (2010-2023)
- CR-V (2010-2023)
- HR-V (2015-2023)

### Nissan
- Qashqai (2010-2023)
- Juke (2010-2023)
- X-Trail (2010-2023)
- Micra (2010-2023)

### Mazda
- Mazda3 (2010-2023)
- Mazda6 (2010-2023)
- CX-5 (2012-2023)
- CX-30 (2019-2023)

### Subaru
- Impreza (2010-2023)
- Forester (2010-2023)
- XV/Crosstrek (2012-2023)
- Outback (2010-2023)

Each model supports:
- Key programming
- Immobilizer bypass
- Key count reading
- Key clearing
- PIN reading (where applicable)

## Requirements

- Python 3.8 or higher
- Python packages (installed automatically):
  - python-can
  - pyserial
  - python-obd
  - customtkinter
  - pillow
  - pyusb
- System requirements:
  - Git (for installation)
  - tkinter (usually comes with Python, if not see installation troubleshooting)
  - Microsoft Visual C++ Build Tools (might be required on Windows)

## Installation

1. Make sure you have Git installed on your system
2. Clone this repository:
```bash
git clone https://github.com/yourusername/key-programmer.git
cd key-programmer/gui
```

3. Install required packages:
```bash
# For Windows:
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Troubleshooting Installation

If you encounter any installation issues:

1. Make sure you have Git installed:
   - Download from: https://git-scm.com/download/win

2. If tkinter is missing:
   ```bash
   # For Windows:
   # Option 1: Reinstall Python and make sure to check "tcl/tk and IDLE" during installation
   # Option 2: Install tkinter using the Python installer:
   python -m pip install tk
   ```

3. If python-obd fails to install:
   ```bash
   pip install git+https://github.com/brendan-w/python-OBD.git
   ```

4. If you get "Microsoft Visual C++ Build Tools" error:
   - Install Visual Studio Build Tools from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
   - Select "Desktop development with C++" workload during installation

## Usage

1. Connect OBDLink SX device
2. Select vehicle manufacturer, model, and year
3. Choose desired operation:
   - Add New Key
   - Immobilizer Bypass
   - Read Key Count
   - Clear All Keys
4. Follow on-screen instructions

## Security Notice

This tool is for educational purposes only. Unauthorized access to vehicle security systems may be illegal in your jurisdiction. Only use on vehicles you own or have explicit permission to work on.

## Adding New Vehicles

Vehicle definitions are stored in `src/database/vehicles.json`. Each vehicle entry contains:

- Supported features
- Command sequences for each operation
- Expected responses
- Timing parameters

Example vehicle entry:
```json
{
    "Manufacturer": {
        "Model": {
            "Year": {
                "supports_key_add": true,
                "key_add_sequence": [
                    {
                        "description": "Enter programming mode",
                        "command": "31 01 00",
                        "expected_response": "71 01 00",
                        "delay": 1
                    }
                ]
            }
        }
    }
}
```

## Future Development
- Enhanced security features with proper authentication
- Additional manufacturer support
- Advanced diagnostic protocols
- Custom PID configurations
- Data logging and analysis
- Firmware updates
- Integration with manufacturer-specific tools

## Contributing
Contributions are welcome! Please feel free to submit pull requests.

## Developer
Developed by M Khanfar  
GitHub: [https://github.com/khanfar](https://github.com/khanfar)

## Copyright
 2025 M Khanfar. All rights reserved.

This software is provided for educational purposes only. The developer and contributors are not responsible for any misuse or damage caused by this tool. Always follow local laws and manufacturer guidelines when working with vehicle systems.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
