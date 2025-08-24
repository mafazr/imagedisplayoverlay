#!/usr/bin/env python3
"""
Test script for the QR Code Display Application.
This script tests the core QR code generation functionality without the GUI.
"""

import qrcode
import requests
from PIL import Image
import io

def test_qr_generation():
    """Test QR code generation with a sample URL."""
    print("Testing QR code generation...")
    
    # Test URL
    test_url = "https://example.com"
    
    try:
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(test_url)
        qr.make(fit=True)
        
        # Create image
        qr_image = qr.make_image(fill_color="black", back_color="white")
        
        print(f"✓ QR code generated successfully for: {test_url}")
        print(f"  Image size: {qr_image.size}")
        print(f"  Image mode: {qr_image.mode}")
        
        return True
        
    except Exception as e:
        print(f"✗ QR code generation failed: {e}")
        return False

def test_network_request():
    """Test network request functionality."""
    print("\nTesting network request...")
    
    test_url = "https://httpbin.org/get"
    
    try:
        response = requests.get(test_url, timeout=10)
        response.raise_for_status()
        
        print(f"✓ Network request successful to: {test_url}")
        print(f"  Status code: {response.status_code}")
        print(f"  Response size: {len(response.content)} bytes")
        
        return True
        
    except requests.RequestException as e:
        print(f"✗ Network request failed: {e}")
        return False

def test_pil_operations():
    """Test PIL image operations."""
    print("\nTesting PIL operations...")
    
    try:
        # Create a simple test image
        test_image = Image.new('RGB', (100, 100), color='white')
        
        # Save to buffer
        buffer = io.BytesIO()
        test_image.save(buffer, format='PNG')
        buffer.seek(0)
        
        # Load from buffer
        loaded_image = Image.open(buffer)
        
        print("✓ PIL operations successful")
        print(f"  Original size: {test_image.size}")
        print(f"  Loaded size: {loaded_image.size}")
        print(f"  Buffer size: {len(buffer.getvalue())} bytes")
        
        return True
        
    except Exception as e:
        print(f"✗ PIL operations failed: {e}")
        return False

def main():
    """Run all tests."""
    print("QR Code Display Application - Test Suite")
    print("=" * 50)
    
    tests = [
        ("QR Code Generation", test_qr_generation),
        ("Network Request", test_network_request),
        ("PIL Operations", test_pil_operations),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\nRunning: {test_name}")
        if test_func():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The application should work correctly.")
    else:
        print("❌ Some tests failed. Please check the error messages above.")
    
    return passed == total

if __name__ == "__main__":
    main()
