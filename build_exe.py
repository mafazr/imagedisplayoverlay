#!/usr/bin/env python3
"""
Build script for creating standalone executables of the QR Code Display Application.
This script helps create distributable packages for Windows and macOS.
"""

import os
import sys
import subprocess
import platform

def check_dependencies():
    """Check if required build dependencies are installed."""
    try:
        import PyInstaller
        print("✓ PyInstaller is installed")
        return True
    except ImportError:
        print("✗ PyInstaller is not installed")
        print("Installing PyInstaller...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("✓ PyInstaller installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("✗ Failed to install PyInstaller")
            return False

def build_executable():
    """Build the standalone executable."""
    print("Building standalone executable...")
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",           # Single executable file
        "--windowed",          # No console window on Windows/macOS
        "--name=QRCodeDisplay", # Executable name
        "--icon=icon.ico" if os.path.exists("icon.ico") else "", # Icon if available
        "qr_display_app.py"
    ]
    
    # Remove empty arguments
    cmd = [arg for arg in cmd if arg]
    
    try:
        subprocess.check_call(cmd)
        print("✓ Executable built successfully!")
        print(f"Location: {os.path.join('dist', 'QRCodeDisplay.exe' if platform.system() == 'Windows' else 'QRCodeDisplay')}")
    except subprocess.CalledProcessError as e:
        print(f"✗ Build failed with error: {e}")
        return False
    
    return True

def main():
    """Main build function."""
    print("QR Code Display Application - Build Script")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("qr_display_app.py"):
        print("✗ Error: qr_display_app.py not found in current directory")
        print("Please run this script from the project directory")
        return
    
    # Check and install dependencies
    if not check_dependencies():
        return
    
    # Build the executable
    if build_executable():
        print("\n🎉 Build completed successfully!")
        print("\nNext steps:")
        print("1. Check the 'dist' folder for your executable")
        print("2. Test the executable on a clean machine")
        print("3. Distribute the executable to users")
    else:
        print("\n❌ Build failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
