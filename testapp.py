import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Custom PDF Tool")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Custom PDF Tool", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=400)
        self.tabview.grid(row=0, column=1, padx=(20, 10), pady=20, sticky="nsew")
        self.tabview.add("PDF Compress")
        self.tabview.add("PDF Split")
        self.tabview.add("PDF Merge")
        self.tabview.tab("PDF Compress").grid_columnconfigure([0], weight=1) 
        # self.tabview.tab("PDF Split").grid_columnconfigure(0, weight=1)

        # create compress tab
        self.compress_file_path = customtkinter.CTkEntry(self.tabview.tab("PDF Compress"), placeholder_text="Enter the file path")
        self.compress_file_path.grid(row=0, column=0, padx=20, pady=20, sticky="ew")  # Adjust the sticky parameter to "ew" to make it full width


        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=2, padx=(10, 20), pady=20, sticky="nsew")


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    
    def upload_file_event(self):
        # Open a file dialog and allow the user to select a file to upload
        self.file_path_text.delete(0, 'end')
        file_path = customtkinter.filedialog.askopenfilename()

        # Do something with the selected file
        self.file_path_text.insert(0, file_path)
        # compress(file_path, file_path.replace(".pdf", "_compressed.pdf"), power=4)
        # print(file_path)
    
    def update_textbox(self, text: str):
        self.textbox.delete('0.0', 'end')
        self.textbox.insert('0.0', text)
        self.file_path_text.delete(0, 'end')

    def compress_file(self):
        file_path = self.file_path_text.get()
        if file_path == self.file_path_text._placeholder_text or file_path == "":
            tkinter.messagebox.showerror("Error", "Please enter a valid file path")
            return
        else:
            power_value = int(self.power_optionemenu.get())  # Retrieve the selected power value
            # print(f"Selected power value: {power_value}")  # Print the selected power value (for testing)
            # status = compress(file_path, file_path.replace(".pdf", "_compressed.pdf"), power=power_value)
            # self.update_textbox(status)



if __name__ == "__main__":
    app = App()
    app.mainloop()