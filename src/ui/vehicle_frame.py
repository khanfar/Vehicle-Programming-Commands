import customtkinter as ctk
from tkinter import ttk

class VehicleFrame(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        
        # Create header
        self.create_header()
        
        # Create vehicle selection
        self.create_vehicle_selection()
        
    def create_header(self):
        """Create frame header"""
        header = ctk.CTkLabel(
            self,
            text="Vehicle Selection",
            font=("Helvetica", 16, "bold")
        )
        header.pack(padx=5, pady=5)
        
    def create_vehicle_selection(self):
        """Create vehicle selection controls"""
        # Manufacturer selection
        mfr_frame = ctk.CTkFrame(self)
        mfr_frame.pack(fill="x", padx=5, pady=5)
        
        mfr_label = ctk.CTkLabel(mfr_frame, text="Manufacturer:")
        mfr_label.pack(padx=5, pady=2)
        
        self.mfr_var = ctk.StringVar()
        self.mfr_combo = ctk.CTkComboBox(
            mfr_frame,
            values=sorted(list(self.app.vehicles.keys())),
            variable=self.mfr_var,
            command=self.on_manufacturer_change
        )
        self.mfr_combo.pack(padx=5, pady=2)
        
        # Model selection
        model_frame = ctk.CTkFrame(self)
        model_frame.pack(fill="x", padx=5, pady=5)
        
        model_label = ctk.CTkLabel(model_frame, text="Model:")
        model_label.pack(padx=5, pady=2)
        
        self.model_var = ctk.StringVar()
        self.model_combo = ctk.CTkComboBox(
            model_frame,
            values=[],
            variable=self.model_var,
            command=self.on_model_change
        )
        self.model_combo.pack(padx=5, pady=2)
        
        # Year selection
        year_frame = ctk.CTkFrame(self)
        year_frame.pack(fill="x", padx=5, pady=5)
        
        year_label = ctk.CTkLabel(year_frame, text="Year:")
        year_label.pack(padx=5, pady=2)
        
        self.year_var = ctk.StringVar()
        self.year_combo = ctk.CTkComboBox(
            year_frame,
            values=[],
            variable=self.year_var,
            command=self.on_year_change
        )
        self.year_combo.pack(padx=5, pady=2)
        
    def on_manufacturer_change(self, choice):
        """Handle manufacturer selection change"""
        # Clear subsequent selections
        self.model_var.set("")
        self.year_var.set("")
        
        # Update model list based on manufacturer
        if choice in self.app.vehicles:
            models = sorted(list(self.app.vehicles[choice].keys()))
            self.model_combo.configure(values=models)
        else:
            self.model_combo.configure(values=[])
            
    def on_model_change(self, choice):
        """Handle model selection change"""
        # Clear year selection
        self.year_var.set("")
        
        # Update year list based on model
        mfr = self.mfr_var.get()
        if mfr in self.app.vehicles and choice in self.app.vehicles[mfr]:
            years = sorted(list(self.app.vehicles[mfr][choice].keys()))
            self.year_combo.configure(values=years)
        else:
            self.year_combo.configure(values=[])
            
    def on_year_change(self, choice):
        """Handle year selection change"""
        # Get selected vehicle data
        mfr = self.mfr_var.get()
        model = self.model_var.get()
        if mfr in self.app.vehicles and model in self.app.vehicles[mfr] and choice in self.app.vehicles[mfr][model]:
            vehicle_data = self.app.vehicles[mfr][model][choice]
            self.app.main_window.command_frame.update_commands(vehicle_data)
            
    def get_selected_vehicle(self):
        """Get the currently selected vehicle info"""
        return {
            "manufacturer": self.mfr_var.get(),
            "model": self.model_var.get(),
            "year": self.year_var.get()
        }
