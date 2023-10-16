import tkinter
import tkinter.messagebox
import customtkinter
from pdf_compressor import compress


customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("PDF Compression Tool")
        self.geometry(f"{720}x{448}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=0) # column 0 is resizable
        self.grid_columnconfigure((1, 2), weight=1) # column 1 is not resizable
        self.grid_rowconfigure((0, 1, 2, 3), weight=1) # rows 0, 1 and 2 are resizable

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="PDF compression", font=customtkinter.CTkFont(size=20, weight="bold"))
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

    # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, columnspan=2, padx=20, pady=20, sticky="nsew")

    # create main entry and button
        self.file_path_text = customtkinter.CTkEntry(self, placeholder_text="Enter a valid file path")
        self.file_path_text.grid(row=1, column=1, columnspan=2, padx=20, pady=20, sticky="nsew")

        self.upload_button = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Upload", command=self.upload_file_event)
        self.upload_button.grid(row=2, column=1, rowspan=2,  padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.compress_button = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Compress", command=self.compress_file)
        self.compress_button.grid(row=2, column=2, rowspan=2,  padx=(20, 20), pady=(20, 20), sticky="nsew")


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
            print(file_path)
            status = compress(file_path, file_path.replace(".pdf", "_compressed.pdf"), power=4)
            self.update_textbox(status)

if __name__ == "__main__":
    app = App()
    app.mainloop()

# installer cmd: pyinstaller --name PDFCompressor --onefile --windowed --noconsole --icon=icon.ico compressionapp.py
# installer cmd: pyinstaller --name PDFCompressor --onefile --windowed --icon=opensource.ico compressionapp.py