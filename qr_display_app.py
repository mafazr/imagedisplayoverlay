import sys
import requests
import qrcode
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                             QWidget, QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage
import io
from PIL import Image

class QRCodeFetcher(QThread):
    """Thread for fetching QR code from URL to avoid blocking the UI"""
    qr_code_ready = pyqtSignal(object)
    error_occurred = pyqtSignal(str)
    
    def __init__(self, url):
        super().__init__()
        self.url = url
    
    def run(self):
        try:
            # Fetch the webpage content
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            
            # Generate QR code from the URL
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(self.url)
            qr.make(fit=True)
            
            # Create QR code image
            qr_image = qr.make_image(fill_color="black", back_color="white")
            
            # Convert PIL image to QPixmap
            buffer = io.BytesIO()
            qr_image.save(buffer, format='PNG')
            buffer.seek(0)
            
            qpixmap = QPixmap()
            qpixmap.loadFromData(buffer.getvalue())
            
            self.qr_code_ready.emit(qpixmap)
            
        except requests.RequestException as e:
            self.error_occurred.emit(f"Failed to fetch URL: {str(e)}")
        except Exception as e:
            self.error_occurred.emit(f"Error generating QR code: {str(e)}")

class QRDisplayApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR Code Display")
        self.setGeometry(100, 100, 600, 500)
        
        # Set window flags to keep it on top
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint | 
            Qt.Window
        )
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # URL input section
        url_layout = QHBoxLayout()
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL here...")
        self.url_input.returnPressed.connect(self.fetch_qr_code)
        
        self.fetch_button = QPushButton("Fetch QR Code")
        self.fetch_button.clicked.connect(self.fetch_qr_code)
        
        url_layout.addWidget(QLabel("URL:"))
        url_layout.addWidget(self.url_input)
        url_layout.addWidget(self.fetch_button)
        
        layout.addLayout(url_layout)
        
        # QR code display area
        self.qr_label = QLabel("Enter a URL and click 'Fetch QR Code' to display the QR code")
        self.qr_label.setAlignment(Qt.AlignCenter)
        self.qr_label.setStyleSheet("""
            QLabel {
                border: 2px dashed #ccc;
                border-radius: 10px;
                padding: 20px;
                background-color: #f9f9f9;
                font-size: 14px;
                color: #666;
            }
        """)
        layout.addWidget(self.qr_label)
        
        # Initialize QR fetcher thread
        self.qr_fetcher = None
        
        # Set focus to URL input
        self.url_input.setFocus()
    
    def fetch_qr_code(self):
        """Fetch and display QR code for the entered URL"""
        url = self.url_input.text().strip()
        
        if not url:
            QMessageBox.warning(self, "Input Error", "Please enter a URL")
            return
        
        # Add http:// if no protocol specified
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        # Update UI to show loading state
        self.fetch_button.setEnabled(False)
        self.fetch_button.setText("Generating...")
        self.qr_label.setText("Generating QR code...")
        self.qr_label.setStyleSheet("""
            QLabel {
                border: 2px dashed #ccc;
                border-radius: 10px;
                padding: 20px;
                background-color: #f9f9f9;
                font-size: 14px;
                color: #666;
            }
        """)
        
        # Create and start QR fetcher thread
        self.qr_fetcher = QRCodeFetcher(url)
        self.qr_fetcher.qr_code_ready.connect(self.display_qr_code)
        self.qr_fetcher.error_occurred.connect(self.show_error)
        self.qr_fetcher.finished.connect(self.reset_ui)
        self.qr_fetcher.start()
    
    def display_qr_code(self, qpixmap):
        """Display the generated QR code"""
        # Scale the pixmap to fit the label while maintaining aspect ratio
        scaled_pixmap = qpixmap.scaled(
            self.qr_label.width() - 40, 
            self.qr_label.height() - 40,
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        )
        
        self.qr_label.setPixmap(scaled_pixmap)
        self.qr_label.setStyleSheet("""
            QLabel {
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 10px;
                background-color: white;
            }
        """)
    
    def show_error(self, error_message):
        """Display error message"""
        QMessageBox.critical(self, "Error", error_message)
        self.qr_label.setText("Error occurred. Please try again.")
        self.qr_label.setStyleSheet("""
            QLabel {
                border: 2px dashed #f44336;
                border-radius: 10px;
                padding: 20px;
                background-color: #ffebee;
                font-size: 14px;
                color: #d32f2f;
            }
        """)
    
    def reset_ui(self):
        """Reset UI elements after QR generation"""
        self.fetch_button.setEnabled(True)
        self.fetch_button.setText("Fetch QR Code")
    
    def resizeEvent(self, event):
        """Handle window resize to scale QR code appropriately"""
        super().resizeEvent(event)
        
        # If there's a QR code displayed, rescale it
        if hasattr(self.qr_label, 'pixmap') and self.qr_label.pixmap():
            qpixmap = self.qr_label.pixmap()
            scaled_pixmap = qpixmap.scaled(
                self.qr_label.width() - 40, 
                self.qr_label.height() - 40,
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
            self.qr_label.setPixmap(scaled_pixmap)

def main():
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create and show the main window
    window = QRDisplayApp()
    window.show()
    
    # Start the event loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
