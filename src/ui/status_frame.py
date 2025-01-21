import customtkinter as ctk

class StatusFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # Create status label
        self.status_label = ctk.CTkLabel(
            self,
            text="Not Connected",
            font=("Helvetica", 12)
        )
        self.status_label.pack(side="left", padx=5)
        
    def set_status(self, message):
        """Update status message"""
        self.status_label.configure(text=message)
