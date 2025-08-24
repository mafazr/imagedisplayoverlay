"""
Configuration file for the QR Code Display Application.
Modify these settings to customize the application behavior.
"""

# Window settings
WINDOW_TITLE = "QR Code Display"
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500
WINDOW_X = 100
WINDOW_Y = 100

# QR Code settings
QR_VERSION = 1
QR_ERROR_CORRECTION = 'L'  # L, M, Q, H (Low, Medium, Quarter, High)
QR_BOX_SIZE = 10
QR_BORDER = 4
QR_FILL_COLOR = "black"
QR_BACK_COLOR = "white"

# Network settings
REQUEST_TIMEOUT = 10  # seconds

# UI settings
DEFAULT_PLACEHOLDER_TEXT = "Enter URL here..."
STATUS_FETCHING = "Fetching QR code..."
STATUS_SUCCESS = "QR code displayed successfully"
STATUS_ERROR_PREFIX = "Error: "

# Style settings
MAIN_BACKGROUND_COLOR = "#f0f0f0"
INPUT_BORDER_COLOR = "#ddd"
INPUT_FOCUS_COLOR = "#0078d4"
BUTTON_BACKGROUND_COLOR = "#0078d4"
BUTTON_HOVER_COLOR = "#106ebe"
BUTTON_PRESSED_COLOR = "#005a9e"
BUTTON_TEXT_COLOR = "white"
LABEL_BORDER_COLOR = "#ccc"
LABEL_BACKGROUND_COLOR = "#f9f9f9"
LABEL_TEXT_COLOR = "#666"
STATUS_TEXT_COLOR = "#666"

# Messages
ERROR_NO_URL = "Please enter a URL"
ERROR_FETCH_FAILED = "Failed to fetch URL: {}"
ERROR_QR_GENERATION = "Error generating QR code: {}"
