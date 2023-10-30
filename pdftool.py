import tkinter
import tkinter.messagebox
import tkinter.filedialog as filedialog
import customtkinter
from pdf_compressor import compress
from pdf_split import split_pdf
from pdf_merge import merge_pdfs

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
        self.tabview.tab("PDF Split").grid_columnconfigure([0, 1, 2, 3], weight=1)
        self.tabview.tab("PDF Merge").grid_columnconfigure([0], weight=1)

        # create compress tab
        self.compress_file_path = customtkinter.CTkEntry(self.tabview.tab("PDF Compress"), placeholder_text="Enter the file path")
        self.compress_file_path.grid(row=0, column=0, columnspan=4, padx=20, pady=(20, 10), sticky="ew")  # Adjust the sticky parameter to "ew" to make it full width
        self.upload_compress_button = customtkinter.CTkButton(self.tabview.tab("PDF Compress"), text="Upload", command=lambda: self.upload_file_event("compress"))
        self.upload_compress_button.grid(row=1, column=0, columnspan=3, padx=20, pady=10, sticky="ew")
        self.power_dropdown = customtkinter.CTkOptionMenu(self.tabview.tab("PDF Compress"), values=["0", "1", "2", "3", "4"], dynamic_resizing=False)
        self.power_dropdown.grid(row=1, column=3, padx=20, pady=10)
        self.power_dropdown.set("Power")
        self.compress_button = customtkinter.CTkButton(self.tabview.tab("PDF Compress"), text="Compress", command=self.compress_file)
        self.compress_button.grid(row=2, column=0, columnspan=4, padx=20, pady=20, sticky="nsew", ipadx=20, ipady=5)  # Adjust the ipadx and ipady parameters to increase the size of the button
        self.compress_button.configure(width=20)  # Adjust the width to increase the button's width

        # create split tab
        self.split_file_path = customtkinter.CTkEntry(self.tabview.tab("PDF Split"), placeholder_text="Enter the file path")
        self.split_file_path.grid(row=0, column=0, columnspan=3, padx=(20, 10), pady=(20, 10), sticky="ew")  # Adjust the sticky parameter to "ew" to make it full width
        self.upload_split_button = customtkinter.CTkButton(self.tabview.tab("PDF Split"), text="Upload", command=lambda: self.upload_file_event("split"))
        self.upload_split_button.grid(row=0, column=3, padx=(10, 20), pady=(20, 10))

        self.radiobutton_frame = customtkinter.CTkFrame(self.tabview.tab("PDF Split"), corner_radius=0)
        self.radiobutton_frame.grid(row=1, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Split method :")
        self.label_radio_group.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=0, column=2, pady=10, padx=10, sticky="n")
        self.radio_button_1.configure(text="Custom")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=0, column=3, pady=10, padx=10, sticky="n")
        self.radio_button_2.configure(text="Fixed")

        self.custom_range_label_start = customtkinter.CTkLabel(self.tabview.tab("PDF Split"), text="Custom Range Start:")
        self.custom_range_label_start.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="w")
        self.custom_range_entry_start = customtkinter.CTkEntry(self.tabview.tab("PDF Split"), placeholder_text="Start")
        self.custom_range_entry_start.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.custom_range_entry_start.configure(width=50)

        self.custom_range_label_end = customtkinter.CTkLabel(self.tabview.tab("PDF Split"), text="Custom Range End:")
        self.custom_range_label_end.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.custom_range_entry_end = customtkinter.CTkEntry(self.tabview.tab("PDF Split"), placeholder_text="End")
        self.custom_range_entry_end.grid(row=2, column=3, padx=(10, 20), pady=10, sticky="w")
        self.custom_range_entry_end.configure(width=50)

        self.fixed_range_label = customtkinter.CTkLabel(self.tabview.tab("PDF Split"), text="Fixed Range :")
        self.fixed_range_label.grid(row=3, column=0, padx=(20, 10), pady=10, sticky="w")
        self.fixed_range_entry = customtkinter.CTkEntry(self.tabview.tab("PDF Split"), placeholder_text="Fixed")
        self.fixed_range_entry.grid(row=3, column=1, padx=(10, 20), pady=10, sticky="ew")
        self.fixed_range_entry.configure(width=50)

        self.split_button = customtkinter.CTkButton(self.tabview.tab("PDF Split"), text="Split", command=self.split_file)
        self.split_button.grid(row=4, column=0, columnspan=4, padx=20, pady=20, sticky="nsew", ipadx=20, ipady=5)  # Adjust the ipadx and ipady parameters to increase the size of the button
        self.split_button.configure(width=20)  # Adjust the width to increase the button's width


        # create merge tab
        self.merge_file_paths = []  # List to hold the paths of the files to be merged
        self.upload_merge_button = customtkinter.CTkButton(self.tabview.tab("PDF Merge"), text="Upload", command=self.upload_merge_event)
        self.upload_merge_button.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 10))

        self.merge_listbox = tkinter.Listbox(self.tabview.tab("PDF Merge"), width=50)  # Using tkinter Listbox here
        self.merge_listbox.grid(row=1, column=0, columnspan=3, padx=20, pady=10, sticky="nsew")
        self.merge_listbox.config(xscrollcommand=True)

        self.up_button = customtkinter.CTkButton(self.tabview.tab("PDF Merge"), text="Move Up", command=self.move_up_event)
        self.up_button.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")
        self.down_button = customtkinter.CTkButton(self.tabview.tab("PDF Merge"), text="Move Down", command=self.move_down_event)
        self.down_button.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.remove_button = customtkinter.CTkButton(self.tabview.tab("PDF Merge"), text="Remove", command=self.remove_file_event)
        self.remove_button.grid(row=2, column=2, padx=(10, 20), pady=10, sticky="nsew")

        self.merge_button = customtkinter.CTkButton(self.tabview.tab("PDF Merge"), text="Merge", command=lambda: self.merge_files_event(self.merge_file_paths))
        self.merge_button.grid(row=5, column=0, columnspan=3, padx=20, pady=20, sticky="nsew", ipadx=20, ipady=5)
        self.merge_button.configure(width=20)

        
        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=2, padx=(10, 20), pady=20, sticky="nsew")

        # set default settings


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    
    def upload_file_event(self, task: str):
        if task == "compress":
            self.handle_upload(self.compress_file_path)
        elif task == "split":
            self.handle_upload(self.split_file_path)

    def handle_upload(self, file_path_entry):
        # Open a file dialog and allow the user to select a file to upload
        file_path_entry.delete(0, 'end')
        file_path = customtkinter.filedialog.askopenfilename()

        # Do something with the selected file
        file_path_entry.insert(0, file_path)
    
    def update_textbox(self, text: str):
        self.textbox.delete('0.0', 'end')
        self.textbox.insert('0.0', text)

    def compress_file(self):
        file_path = self.compress_file_path.get()
        if file_path == self.compress_file_path._placeholder_text or file_path == "":
            tkinter.messagebox.showerror("Error", "Please enter a valid file path")
            return
        else:
            if self.power_dropdown.get() == "Power":
                tkinter.messagebox.showerror("Error", "Please select a power value")
                return
            power_value = int(self.power_dropdown.get())  # Retrieve the selected power value
            status = compress(file_path, file_path.replace(".pdf", "_compressed.pdf"), power=power_value)
            self.update_textbox(status)

    def split_file(self):
        file_path = self.split_file_path.get()
        if file_path == self.split_file_path._placeholder_text or file_path == "":
            tkinter.messagebox.showerror("Error", "Please enter a valid file path")
            return
        else:
            option = self.radio_var.get()
            if option == 0:
                if self.custom_range_entry_start.get() == "" or self.custom_range_entry_end.get() == "":
                    tkinter.messagebox.showerror("Error", "Please enter a valid custom range")
                    return
                start = int(self.custom_range_entry_start.get())
                end = int(self.custom_range_entry_end.get())
                if start > end:
                    tkinter.messagebox.showerror("Error", "Please enter a valid custom range")
                    return
                msg = split_pdf(file_path, custom_start=start, custom_end=end, fixed_value=None)
                self.update_textbox(msg)
            else:
                if self.fixed_range_entry.get() == "":
                    tkinter.messagebox.showerror("Error", "Please enter a valid fixed range")
                    return
                fixed = int(self.fixed_range_entry.get())
                msg = split_pdf(file_path, fixed_value=fixed, custom_start=None, custom_end=None)
                self.update_textbox(msg)
        # clear input fields
        self.split_file_path.delete(0, 'end')
        self.custom_range_entry_start.delete(0, 'end')
        self.custom_range_entry_end.delete(0, 'end')
        self.fixed_range_entry.delete(0, 'end')
    
    def upload_merge_event(self):
        # Open a file dialog and allow the user to select files to upload
        file_paths = customtkinter.filedialog.askopenfilenames()

        for path in file_paths:
            self.merge_listbox.insert("end", path)
            self.merge_file_paths.append(path)

    def move_up_event(self):
        selected_index = self.merge_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            if selected_index > 0:
                self.merge_listbox.insert(selected_index - 1, self.merge_listbox.get(selected_index))
                self.merge_listbox.delete(selected_index + 1)
                self.merge_file_paths.insert(selected_index - 1, self.merge_file_paths.pop(selected_index))
    
    def move_down_event(self):
        selected_index = self.merge_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            if selected_index < len(self.merge_file_paths) - 1:
                self.merge_listbox.insert(selected_index + 2, self.merge_listbox.get(selected_index))
                self.merge_listbox.delete(selected_index)
                self.merge_file_paths.insert(selected_index + 1, self.merge_file_paths.pop(selected_index))

    def remove_file_event(self):
        selected_index = self.merge_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            self.merge_listbox.delete(selected_index)
            self.merge_file_paths.pop(selected_index)

    def merge_files_event(self, file_paths):
        if len(file_paths) < 2:
            tkinter.messagebox.showerror("Error", "Please select at least 2 files to merge.")
        else:
            output_path = filedialog.asksaveasfilename(defaultextension=".pdf")
            if output_path:
                merge_pdfs(file_paths, output_path)
                self.update_textbox(f"PDF files have been merged into {output_path}.")
                self.merge_file_paths.clear()
                self.merge_listbox.delete(0, "end")




if __name__ == "__main__":
    app = App()
    app.mainloop()


# create an executible file
# pyinstaller --name PDFTool --onefile --windowed --noconsole --icon=icon.ico pdftool.py