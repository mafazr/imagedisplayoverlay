# Image Display Overlay

A cross-platform native application that displays images (including QR codes) in a persistent window that stays on top of all other windows.

Use case: Trainer led sessions where persistent content like a QR code for attendance taking is needed to overlay on top of presentations and other windows. 

## Features

- **Cross-platform**: Works on Windows and macOS
- **Always on top**: Window stays above all other applications
- **Image display**: Display any image file or generate QR codes from URLs
- **Modern UI**: Clean, responsive interface with smooth animations
- **Error handling**: Comprehensive error handling for network and file issues
- **Responsive design**: Automatically scales images to fit the window

## Requirements

- Python 3.8 or higher
- PyQt5 (stable cross-platform GUI framework)
- qrcode library with PIL support
- requests library
- Pillow (PIL)

## Installation

1. **Clone or download this project** to your local machine

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install PyQt5 qrcode[pil] requests Pillow
   ```

## Usage

1. **Run the application**:
   ```bash
   python qr_display_app.py
   ```

2. **Enter a URL** in the input field (e.g., `https://example.com`)

3. **Click "Fetch QR Code"** or press Enter

4. **The QR code will be displayed** in the main area

5. **The window will stay on top** of all other applications

## How It Works

1. **URL Input**: The application accepts any valid URL
2. **QR Generation**: Generates a QR code from the entered URL
3. **Display**: Shows the QR code in a resizable window
4. **Always on Top**: Uses Qt's `WindowStaysOnTopHint` flag to keep the window above others

## Technical Details

- **Framework**: PyQt5 for cross-platform GUI (stable and reliable)
- **QR Generation**: Uses the `qrcode` library with PIL backend
- **Threading**: QR code generation runs in a separate thread to prevent UI blocking
- **Error Handling**: Comprehensive error handling for network and generation issues
- **Responsive Design**: Automatically scales content when the window is resized

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **Window not staying on top**: This is a known limitation on some systems. The application uses the strongest available method to keep the window on top.

3. **QR code not displaying**: Check that the URL is valid and accessible from your network.

### Platform-Specific Notes

- **Windows**: Tested on Windows 10/11 with PyQt5 (stable)
- **macOS**: Tested on macOS 10.15+
- **Linux**: Should work but not extensively tested

## Building Standalone Executables

To create standalone executables for distribution:

### Using PyInstaller (Windows/macOS):
```bash
pip install pyinstaller
pyinstaller --onefile --windowed qr_display_app.py
```

### Using cx_Freeze:
```bash
pip install cx_Freeze
python setup.py build
```

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application.
