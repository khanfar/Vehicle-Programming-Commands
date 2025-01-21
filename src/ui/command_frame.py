import customtkinter as ctk
from tkinter import ttk, messagebox
import threading
import time

class CommandFrame(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.vehicle_data = None
        self.is_connected = False
        
        self.create_header()
        self.create_command_area()
        self.create_log_area()
        
    def create_header(self):
        """Create frame header"""
        # Title
        title = ctk.CTkLabel(
            self,
            text="Vehicle Programming Commands by M Khanfar",
            font=("Helvetica", 18, "bold")
        )
        title.pack(padx=5, pady=(10,5))
        
        # Section header
        header = ctk.CTkLabel(
            self,
            text="Commands",
            font=("Helvetica", 14)
        )
        header.pack(padx=5, pady=(0,5))
        
    def create_command_area(self):
        """Create command buttons area"""
        self.cmd_area = ctk.CTkFrame(self)
        self.cmd_area.pack(fill="x", padx=5, pady=5)
        
        # Default commands (will be updated based on vehicle)
        self.create_default_commands()
        
    def create_default_commands(self):
        """Create default command buttons"""
        # OBD-II Diagnostics Section
        diag_label = ctk.CTkLabel(
            self.cmd_area,
            text="OBD-II Diagnostics",
            font=("Helvetica", 14, "bold")
        )
        diag_label.pack(padx=5, pady=(5,2))
        
        # Read DTCs
        self.read_dtc_btn = ctk.CTkButton(
            self.cmd_area,
            text="Read Trouble Codes",
            command=self.read_dtc,
            state="disabled"
        )
        self.read_dtc_btn.pack(padx=5, pady=2, fill="x")
        
        # Clear DTCs
        self.clear_dtc_btn = ctk.CTkButton(
            self.cmd_area,
            text="Clear Trouble Codes",
            command=self.clear_dtc,
            state="disabled"
        )
        self.clear_dtc_btn.pack(padx=5, pady=2, fill="x")
        
        # Real-time Data
        self.live_data_btn = ctk.CTkButton(
            self.cmd_area,
            text="View Live Data",
            command=self.view_live_data,
            state="disabled"
        )
        self.live_data_btn.pack(padx=5, pady=2, fill="x")
        
        # Emissions Data
        self.emissions_btn = ctk.CTkButton(
            self.cmd_area,
            text="Emissions Status",
            command=self.check_emissions,
            state="disabled"
        )
        self.emissions_btn.pack(padx=5, pady=2, fill="x")
        
        # Vehicle Parameters
        self.params_btn = ctk.CTkButton(
            self.cmd_area,
            text="Vehicle Parameters",
            command=self.monitor_parameters,
            state="disabled"
        )
        self.params_btn.pack(padx=5, pady=2, fill="x")
        
        # Separator
        separator = ttk.Separator(self.cmd_area, orient="horizontal")
        separator.pack(fill="x", padx=5, pady=10)
        
        # Security Features Section (kept for future development)
        security_label = ctk.CTkLabel(
            self.cmd_area,
            text="Security Features (Development)",
            font=("Helvetica", 14, "bold")
        )
        security_label.pack(padx=5, pady=(5,2))
        
        # Add New Key
        self.add_key_btn = ctk.CTkButton(
            self.cmd_area,
            text="Add New Key",
            command=self.add_new_key,
            state="disabled"
        )
        self.add_key_btn.pack(padx=5, pady=2, fill="x")
        
        # Read PIN Code
        self.read_pin_btn = ctk.CTkButton(
            self.cmd_area,
            text="Read PIN Code",
            command=self.read_pin_code,
            state="disabled"
        )
        self.read_pin_btn.pack(padx=5, pady=2, fill="x")
        
        # Immobilizer Bypass
        self.bypass_btn = ctk.CTkButton(
            self.cmd_area,
            text="Immobilizer Bypass",
            command=self.immobilizer_bypass,
            state="disabled"
        )
        self.bypass_btn.pack(padx=5, pady=2, fill="x")
        
        # Read Key Count
        self.read_count_btn = ctk.CTkButton(
            self.cmd_area,
            text="Read Key Count",
            command=self.read_key_count,
            state="disabled"
        )
        self.read_count_btn.pack(padx=5, pady=2, fill="x")
        
        # Clear All Keys
        self.clear_keys_btn = ctk.CTkButton(
            self.cmd_area,
            text="Clear All Keys",
            command=self.clear_all_keys,
            state="disabled"
        )
        self.clear_keys_btn.pack(padx=5, pady=2, fill="x")
        
    def create_log_area(self):
        """Create log display area"""
        log_frame = ctk.CTkFrame(self)
        log_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        log_label = ctk.CTkLabel(log_frame, text="Command Log:")
        log_label.pack(padx=5, pady=2)
        
        self.log_text = ctk.CTkTextbox(log_frame, height=200)
        self.log_text.pack(fill="both", expand=True, padx=5, pady=2)
        
    def update_commands(self, vehicle_data):
        """Update available commands based on vehicle and connection state"""
        self.vehicle_data = vehicle_data
        self.update_button_states()
        
    def update_connection_state(self, is_connected):
        """Update connection state and refresh button states"""
        self.is_connected = is_connected
        self.update_button_states()
        
    def update_button_states(self):
        """Update all button states based on both vehicle support and connection state"""
        # If not connected, all buttons should be disabled
        if not self.is_connected:
            self.add_key_btn.configure(state="disabled")
            self.read_pin_btn.configure(state="disabled")
            self.bypass_btn.configure(state="disabled")
            self.read_count_btn.configure(state="disabled")
            self.clear_keys_btn.configure(state="disabled")
            self.read_dtc_btn.configure(state="disabled")
            self.clear_dtc_btn.configure(state="disabled")
            self.live_data_btn.configure(state="disabled")
            self.emissions_btn.configure(state="disabled")
            self.params_btn.configure(state="disabled")
            return
            
        # If connected but no vehicle selected, enable only OBD-II features
        if not self.vehicle_data:
            self.add_key_btn.configure(state="disabled")
            self.read_pin_btn.configure(state="disabled")
            self.bypass_btn.configure(state="disabled")
            self.read_count_btn.configure(state="disabled")
            self.clear_keys_btn.configure(state="disabled")
            # Enable standard OBD-II features
            self.read_dtc_btn.configure(state="normal")
            self.clear_dtc_btn.configure(state="normal")
            self.live_data_btn.configure(state="normal")
            self.emissions_btn.configure(state="normal")
            self.params_btn.configure(state="normal")
            return
            
        # If connected and vehicle selected, enable based on vehicle support
        self.add_key_btn.configure(
            state="normal" if self.vehicle_data.get("supports_key_add") else "disabled"
        )
        self.read_pin_btn.configure(
            state="normal" if self.vehicle_data.get("supports_pin_read") else "disabled"
        )
        self.bypass_btn.configure(
            state="normal" if self.vehicle_data.get("supports_bypass") else "disabled"
        )
        self.read_count_btn.configure(
            state="normal" if self.vehicle_data.get("supports_key_count") else "disabled"
        )
        self.clear_keys_btn.configure(
            state="normal" if self.vehicle_data.get("supports_key_clear") else "disabled"
        )
        # Always enable OBD-II features when connected
        self.read_dtc_btn.configure(state="normal")
        self.clear_dtc_btn.configure(state="normal")
        self.live_data_btn.configure(state="normal")
        self.emissions_btn.configure(state="normal")
        self.params_btn.configure(state="normal")
        
    def log_message(self, message):
        """Add message to log area"""
        self.log_text.insert("end", f"{message}\n")
        self.log_text.see("end")
        
    def execute_command(self, command_func):
        """Execute command in separate thread"""
        if not self.app.device:
            messagebox.showerror("Error", "Device not connected")
            return
            
        vehicle = self.app.main_window.vehicle_frame.get_selected_vehicle()
        if not all(vehicle.values()):
            messagebox.showerror("Error", "Please select a vehicle first")
            return
            
        # Run command in thread
        thread = threading.Thread(target=command_func, args=(vehicle,))
        thread.daemon = True
        thread.start()
        
    def add_new_key(self):
        """Add new key to vehicle"""
        def command(vehicle):
            try:
                self.log_message(f"Adding new key for {vehicle['manufacturer']} {vehicle['model']} {vehicle['year']}...")
                
                # Get commands for vehicle
                commands = self.app.vehicles[vehicle['manufacturer']][vehicle['model']][vehicle['year']]['key_add_sequence']
                
                # Execute each command
                for cmd in commands:
                    self.log_message(f"Sending: {cmd['description']}")
                    response = self.app.device.send_command(cmd['command'])
                    self.log_message(f"Response: {response}")
                    
                    if not cmd.get('expected_response') in response:
                        raise Exception(f"Unexpected response: {response}")
                        
                    if cmd.get('delay'):
                        time.sleep(cmd['delay'])
                        
                self.log_message("Key successfully added!")
                messagebox.showinfo("Success", "New key has been successfully programmed")
                
            except Exception as e:
                self.log_message(f"Error: {e}")
                messagebox.showerror("Error", str(e))
                
        self.execute_command(command)
        
    def immobilizer_bypass(self):
        """Bypass immobilizer"""
        def command(vehicle):
            try:
                self.log_message(f"Bypassing immobilizer for {vehicle['manufacturer']} {vehicle['model']} {vehicle['year']}...")
                
                # Get bypass commands
                commands = self.app.vehicles[vehicle['manufacturer']][vehicle['model']][vehicle['year']]['bypass_sequence']
                
                # Execute commands
                for cmd in commands:
                    self.log_message(f"Sending: {cmd['description']}")
                    response = self.app.device.send_command(cmd['command'])
                    self.log_message(f"Response: {response}")
                    
                    if not cmd.get('expected_response') in response:
                        raise Exception(f"Unexpected response: {response}")
                        
                    if cmd.get('delay'):
                        time.sleep(cmd['delay'])
                        
                self.log_message("Immobilizer successfully bypassed!")
                messagebox.showinfo("Success", "Immobilizer has been bypassed")
                
            except Exception as e:
                self.log_message(f"Error: {e}")
                messagebox.showerror("Error", str(e))
                
        self.execute_command(command)
        
    def read_key_count(self):
        """Read number of programmed keys"""
        def command(vehicle):
            try:
                self.log_message(f"Reading key count for {vehicle['manufacturer']} {vehicle['model']} {vehicle['year']}...")
                
                # Get command sequence
                commands = self.app.vehicles[vehicle['manufacturer']][vehicle['model']][vehicle['year']]['key_count_sequence']
                
                # Execute commands
                for cmd in commands:
                    self.log_message(f"Sending: {cmd['description']}")
                    response = self.app.device.send_command(cmd['command'])
                    self.log_message(f"Response: {response}")
                    
                    if cmd.get('parse_count'):
                        count = cmd['parse_count'](response)
                        self.log_message(f"Number of programmed keys: {count}")
                        messagebox.showinfo("Key Count", f"Number of programmed keys: {count}")
                        
            except Exception as e:
                self.log_message(f"Error: {e}")
                messagebox.showerror("Error", str(e))
                
        self.execute_command(command)
        
    def read_pin_code(self):
        """Read vehicle PIN code"""
        def command(vehicle):
            try:
                self.log_message(f"Reading PIN code for {vehicle['manufacturer']} {vehicle['model']} {vehicle['year']}...")
                
                # Get PIN read commands
                commands = self.app.vehicles[vehicle['manufacturer']][vehicle['model']][vehicle['year']]['pin_read_sequence']
                
                # Execute commands
                for cmd in commands:
                    self.log_message(f"Sending: {cmd['description']}")
                    response = self.app.device.send_command(cmd['command'])
                    self.log_message(f"Response: {response}")
                    
                    if cmd.get('parse_pin'):
                        pin = cmd['parse_pin'](response)
                        self.log_message(f"PIN Code: {pin}")
                        messagebox.showinfo("PIN Code", f"Vehicle PIN Code: {pin}")
                        
            except Exception as e:
                self.log_message(f"Error: {e}")
                messagebox.showerror("Error", str(e))
                
        self.execute_command(command)

    def clear_all_keys(self):
        """Clear all programmed keys"""
        if not messagebox.askyesno("Warning", "This will erase ALL programmed keys. Continue?"):
            return
            
        def command(vehicle):
            try:
                self.log_message(f"Clearing all keys for {vehicle['manufacturer']} {vehicle['model']} {vehicle['year']}...")
                
                # Get clear commands
                commands = self.app.vehicles[vehicle['manufacturer']][vehicle['model']][vehicle['year']]['key_clear_sequence']
                
                # Execute commands
                for cmd in commands:
                    self.log_message(f"Sending: {cmd['description']}")
                    response = self.app.device.send_command(cmd['command'])
                    self.log_message(f"Response: {response}")
                    
                    if not cmd.get('expected_response') in response:
                        raise Exception(f"Unexpected response: {response}")
                        
                    if cmd.get('delay'):
                        time.sleep(cmd['delay'])
                        
                self.log_message("All keys cleared successfully!")
                messagebox.showinfo("Success", "All keys have been cleared")
                
            except Exception as e:
                self.log_message(f"Error: {e}")
                messagebox.showerror("Error", str(e))
                
        self.execute_command(command)

    def read_dtc(self):
        """Read trouble codes"""
        def command(vehicle):
            try:
                self.log_message(f"Reading trouble codes for {vehicle['manufacturer']} {vehicle['model']} {vehicle['year']}...")
                
                # Get command sequence
                commands = self.app.vehicles[vehicle['manufacturer']][vehicle['model']][vehicle['year']]['obd_dtc_sequence']
                
                # Execute commands
                for cmd in commands:
                    self.log_message(f"Sending: {cmd['description']}")
                    response = self.app.device.send_command(cmd['command'])
                    self.log_message(f"Response: {response}")
                    
                    if cmd.get('parse_dtc'):
                        dtc = cmd['parse_dtc'](response)
                        self.log_message(f"DTC: {dtc}")
                        messagebox.showinfo("DTC", f"DTC: {dtc}")
                        
            except Exception as e:
                self.log_message(f"Error: {e}")
                messagebox.showerror("Error", str(e))
                
        self.execute_command(command)

    def clear_dtc(self):
        """Clear trouble codes"""
        def command(vehicle):
            try:
                # Ask for confirmation
                if not messagebox.askyesno("Confirm", "Are you sure you want to clear all trouble codes? This will reset the Check Engine light and clear all diagnostic data."):
                    return
                    
                self.log_message("Clearing trouble codes...")
                
                # Clear DTCs command (Mode 04)
                clear_cmd = {
                    "description": "Clear DTCs",
                    "command": "04",
                    "expected_response": "44",
                    "delay": 0.5
                }
                
                # Send the command
                self.log_message(f"Sending: {clear_cmd['description']}")
                response = self.app.device.send_command(clear_cmd['command'])
                self.log_message(f"Response: {response}")
                
                if response and response.startswith(clear_cmd['expected_response']):
                    self.log_message("Successfully cleared all trouble codes")
                    messagebox.showinfo("Success", "All trouble codes have been cleared successfully")
                else:
                    raise Exception("Failed to clear trouble codes")
                    
                # Wait a moment then read codes again to confirm
                time.sleep(1)
                self.read_dtc()
                
            except Exception as e:
                self.log_message(f"Error: {e}")
                messagebox.showerror("Error", str(e))
                
        self.execute_command(command)

    def view_live_data(self):
        """View live data"""
        def command(vehicle):
            try:
                self.log_message(f"Viewing live data for {vehicle['manufacturer']} {vehicle['model']} {vehicle['year']}...")
                
                # Get command sequence
                commands = self.app.vehicles[vehicle['manufacturer']][vehicle['model']][vehicle['year']]['obd_live_data_sequence']
                
                # Execute commands
                for cmd in commands:
                    self.log_message(f"Sending: {cmd['description']}")
                    response = self.app.device.send_command(cmd['command'])
                    self.log_message(f"Response: {response}")
                    
                    if cmd.get('parse_live_data'):
                        live_data = cmd['parse_live_data'](response)
                        self.log_message(f"Live Data: {live_data}")
                        messagebox.showinfo("Live Data", f"Live Data: {live_data}")
                        
            except Exception as e:
                self.log_message(f"Error: {e}")
                messagebox.showerror("Error", str(e))
                
        self.execute_command(command)

    def check_emissions(self):
        """Check emissions status"""
        def command(vehicle):
            try:
                self.log_message(f"Checking emissions status for {vehicle['manufacturer']} {vehicle['model']} {vehicle['year']}...")
                
                # Get command sequence
                commands = self.app.vehicles[vehicle['manufacturer']][vehicle['model']][vehicle['year']]['obd_emissions_sequence']
                
                # Execute commands
                for cmd in commands:
                    self.log_message(f"Sending: {cmd['description']}")
                    response = self.app.device.send_command(cmd['command'])
                    self.log_message(f"Response: {response}")
                    
                    if cmd.get('parse_emissions'):
                        emissions = cmd['parse_emissions'](response)
                        self.log_message(f"Emissions Status: {emissions}")
                        messagebox.showinfo("Emissions Status", f"Emissions Status: {emissions}")
                        
            except Exception as e:
                self.log_message(f"Error: {e}")
                messagebox.showerror("Error", str(e))
                
        self.execute_command(command)

    def monitor_parameters(self):
        """Monitor vehicle parameters"""
        def command(vehicle):
            try:
                self.log_message(f"Monitoring vehicle parameters for {vehicle['manufacturer']} {vehicle['model']} {vehicle['year']}...")
                
                # Get command sequence
                commands = self.app.vehicles[vehicle['manufacturer']][vehicle['model']][vehicle['year']]['obd_params_sequence']
                
                # Execute commands
                for cmd in commands:
                    self.log_message(f"Sending: {cmd['description']}")
                    response = self.app.device.send_command(cmd['command'])
                    self.log_message(f"Response: {response}")
                    
                    if cmd.get('parse_params'):
                        params = cmd['parse_params'](response)
                        self.log_message(f"Vehicle Parameters: {params}")
                        messagebox.showinfo("Vehicle Parameters", f"Vehicle Parameters: {params}")
                        
            except Exception as e:
                self.log_message(f"Error: {e}")
                messagebox.showerror("Error", str(e))
                
        self.execute_command(command)
