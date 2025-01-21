import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import json
import os
from ui.main_window import MainWindow
from utils.config import Config
from utils.logger import Logger
from protocols.obdlink import OBDLinkSX

class KeyProgrammerApp:
    def __init__(self):
        self.config = Config()
        self.logger = Logger()
        
        # Setup main window
        self.root = ctk.CTk()
        self.root.title("Vehicle Programming Commands by M Khanfar")
        self.root.geometry("1024x850")
        
        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Initialize OBDLink connection
        self.device = None
        
        # Load vehicle database
        self.load_vehicle_database()
        
        # Create main window interface
        self.main_window = MainWindow(self.root, self)
        
    def load_vehicle_database(self):
        """Load vehicle definitions from JSON database"""
        try:
            # Load main database file
            db_path = os.path.join("src", "database", "vehicles.json")
            with open(db_path, 'r') as f:
                db = json.load(f)
            
            # Initialize vehicles dictionary
            self.vehicles = {}
            
            # Load each manufacturer file
            for mfr, file_path in db["manufacturer_files"].items():
                try:
                    full_path = os.path.join("src", "database", file_path)
                    with open(full_path, 'r') as f:
                        self.vehicles[mfr.title()] = json.load(f)
                except Exception as e:
                    self.logger.error(f"Failed to load manufacturer file {file_path}: {e}")
                    
        except Exception as e:
            self.logger.error(f"Failed to load vehicle database: {e}")
            self.vehicles = {}
            
    def connect_device(self):
        """Connect to OBDLink SX device"""
        try:
            port = self.config.get("device_port", "COM3")
            self.device = OBDLinkSX(port)
            if self.device.connect():
                messagebox.showinfo("Success", "Connected to OBDLink SX")
                return True
            else:
                messagebox.showerror("Error", "Failed to connect to OBDLink SX")
                return False
        except Exception as e:
            messagebox.showerror("Error", f"Connection error: {e}")
            return False
            
    def disconnect_device(self):
        """Disconnect from OBDLink SX device"""
        if self.device:
            self.device.disconnect()
            self.device = None
            messagebox.showinfo("Success", "Disconnected from OBDLink SX")
            
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = KeyProgrammerApp()
    app.run()
