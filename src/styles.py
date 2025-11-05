class GUIColors:
    # Warna untuk GUI
    PRIMARY = "#2E86AB"
    SECONDARY = "#A23B72"
    SUCCESS = "#28A745"
    DANGER = "#DC3545"
    WARNING = "#FFC107"
    INFO = "#17A2B8"
    LIGHT = "#F8F9FA"
    DARK = "#343A40"
    BACKGROUND = "#F0F8FF"
    WHITE = "#FFFFFF"
    
    # Text colors
    TEXT_DARK = "#212529"
    TEXT_LIGHT = "#6C757D"

class GUIStyles:
    # Font styles
    TITLE_FONT = ("Arial", 18, "bold")
    HEADER_FONT = ("Arial", 12, "bold")
    NORMAL_FONT = ("Arial", 10)
    MONOSPACE_FONT = ("Courier New", 10)
    
    # Button styles
    @staticmethod
    def primary_button():
        return {
            'font': ('Arial', 10, 'bold'),
            'bg': GUIColors.PRIMARY,
            'fg': 'white',
            'activebackground': '#1B5E7A',
            'activeforeground': 'white',
            'relief': 'raised',
            'borderwidth': 2,
            'padx': 15,
            'pady': 8,
            'cursor': 'hand2'
        }
    
    @staticmethod
    def secondary_button():
        return {
            'font': ('Arial', 10),
            'bg': GUIColors.SECONDARY,
            'fg': 'white',
            'activebackground': '#7A2B58',
            'activeforeground': 'white',
            'relief': 'raised',
            'borderwidth': 2,
            'padx': 10,
            'pady': 5,
            'cursor': 'hand2'
        }
    
    @staticmethod
    def danger_button():
        return {
            'font': ('Arial', 10),
            'bg': GUIColors.DANGER,
            'fg': 'white',
            'activebackground': '#BD2130',
            'activeforeground': 'white',
            'relief': 'raised',
            'borderwidth': 2,
            'padx': 10,
            'pady': 5,
            'cursor': 'hand2'
        }