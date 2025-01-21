import serial
import time

class OBDLinkSX:
    def __init__(self, port, baudrate=115200, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.connection = None
        
    def connect(self):
        """Connect to OBDLink SX device"""
        try:
            self.connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            
            # Reset device
            self.send_command("ATZ")
            time.sleep(1)
            
            # Disable echo
            self.send_command("ATE0")
            
            # Set protocol to ISO 15765-4 CAN (11 bit ID, 500 kbaud)
            self.send_command("ATSP6")
            
            # Set headers on
            self.send_command("ATH1")
            
            # Set spaces on
            self.send_command("ATS1")
            
            return True
            
        except Exception as e:
            print(f"Connection error: {e}")
            return False
            
    def disconnect(self):
        """Disconnect from device"""
        if self.connection and self.connection.is_open:
            self.connection.close()
            
    def send_command(self, command, timeout=5):
        """Send command to device and get response"""
        if not self.connection or not self.connection.is_open:
            raise Exception("Device not connected")
            
        # Clear input buffer
        self.connection.flushInput()
        
        # Send command
        self.connection.write(f"{command}\r".encode())
        
        # Read response
        response = ""
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            if self.connection.in_waiting:
                char = self.connection.read().decode()
                if char == '>':  # End of response
                    break
                response += char
                
        return response.strip()
        
    def send_can_command(self, id, data):
        """Send CAN command with specific ID and data"""
        command = f"{id:03X}#{data}"
        return self.send_command(command)
        
    def enter_diagnostic_session(self, session_type):
        """Enter diagnostic session"""
        return self.send_command(f"1003{session_type:02X}")
        
    def security_access(self, level):
        """Request security access"""
        # Request seed
        response = self.send_command(f"2701{level:02X}")
        if not response.startswith("6701"):
            raise Exception("Failed to get security seed")
            
        # Calculate key (implementation depends on manufacturer)
        seed = int(response[4:], 16)
        key = self.calculate_security_key(seed)
        
        # Send key
        response = self.send_command(f"2702{key:08X}")
        if not response.startswith("6702"):
            raise Exception("Security access denied")
            
        return True
        
    def calculate_security_key(self, seed):
        """Calculate security key from seed (example implementation)"""
        # This should be implemented according to manufacturer specifications
        return seed ^ 0xFFFFFFFF
