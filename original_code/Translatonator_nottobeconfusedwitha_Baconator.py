######################################################################
# Author(s): Liz Miller
# Username(s): millere4
#
# Assignment: P01:Final Project
#
# Purpose: Window set up for final project
######################################################################
#
# Acknowledgements:
#https://www.youtube.com/watch?v=YXPyB4XeYLA
#codon tables- https://docs.python.org/3/tutorial/datastructures.html#dictionaries
#fasta handling- read/write files- https://realpython.com/read-write-files-python/
#sequence processing- https://docs.python.org/3/library/stdtypes.html#string-methods
#Tkinter Scrolled Text- https://www.pythontutorial.net/tkinter/tkinter-scrolledtext/
#Tkinter dialogs- https://docs.python.org/3/library/dialog.html
#Tkinter MessageBox- https://www.tutorialspoint.com/python/tk_messagebox
####################################################################################
#
#---Notes---#
#ScrolledText widget used to allow fasta input without changing text. Scroll bars added vertically and horizontally to
#   accommodate fasta files. Handles long sequences
#
#LabeledFrame widget to draw border and display label for group. Helps visually separate sections of the window
#
#OptionsMenu Widget used to incorporate drop down menus and save space
#
#Radiobutton widget used for frame selection
#
#Button widget for regular clickable buttons
#
#Used grid_columnconfigure/grid_rowconfigure utilized with Weights. This helps control how the window responds when
#   resized. The weights designate which areas grow with the screen and which do not/differentiate rates. Buttons stay
#   fixed, but input and output boxes grow
#
#Used Sticky to properly align window elements, "nsew" makes widgets fill the spaces allocated to them. Prevents awkward
#   layouts when resizing
########################################################################################################################
########################################################################################################################

import tkinter as tk
from tkinter import scrolledtext, messagebox

########################################################################################################################

# --- Codon Table for mRNA → Protein ---
mrna_codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}
########################################################################################################################

# --- Reverse Table: Protein → Codons ---
reverse_mrna_table = {}
for codon, aa in mrna_codon_table.items():
    reverse_mrna_table.setdefault(aa, []).append(codon)
########################################################################################################################

#---User interface---#
class Translator:
    def __init__(self):
        self.root = tk.Tk() #initializaes main application window
        self.root.title("mRNA ↔ Protein Translator")
        self.root.minsize(800, 600)

        # Configure grid weights for resizing
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)

        # ---Variables---#
        self.input_seq = tk.StringVar() #for storing input
        self.output_seq = tk.StringVar() #for sotring output
        self.color_mode = tk.StringVar(value="Light Mode") #set default color mode
        self.translation_mode = tk.StringVar(value="mRNA → Protein") #set default translation direction
        self.frame_var = tk.IntVar(value=1)  # set default reading frame

        #UI Components#
        self.setup_instructions() #adds instr. at top
        self.setup_mode_selector() #adds color mode dropdown
        self.setup_input_section() #adds input text box and upload button
        self.setup_output_section() #adds output text box and translate button
        self.setup_direction_toggle() #adds reading frame selection
        self.setup_frame_selector() #adds action buttons
        self.setup_buttons() #adds status bar

    def setup_instructions(self):
        """Add clear usage instructions at the top"""
        instructions = """INSTRUCTIONS:
1. Select translation direction (mRNA→Protein or Protein→mRNA)
2. For mRNA→Protein: Select reading frame (1, 2, or 3)
3. Paste sequence or upload FASTA file
4. Click 'Translate' button
5. Use 'Reset' to clear all fields, 'Download' to save results"""

        # Create instruction label with:
        # - Left-aligned text
        # - Helvetica font, size 10
        # - Wrapped to 650px width
        tk.Label(self.root, text=instructions, justify=tk.LEFT, anchor="w", font=('Helvetica', 10),
                wraplength=650).grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky="w")

    def setup_mode_selector(self):
        """Set up color mode selector"""
        modes = ["Light Mode", "Dark Mode", "Colorblind Mode"] #list of available color modes
        label = tk.Label(self.root, text="Color Mode:") #dropdown label
        label.grid(row=1, column=0, padx=10, pady=5, sticky="w") #place drop down label
        dropdown = tk.OptionMenu(self.root, self.color_mode, *modes, command=self.apply_mode) #create dropdown menu
        dropdown.grid(row=1, column=1, padx=10, pady=5, sticky="w") #place drop down menu

        #uses sticky parameters to help control widget expansion

    def apply_mode(self, mode):
        """Apply selected color scheme"""
        colors = {
            "Light Mode": {"bg": "white", "fg": "black"},
            "Dark Mode": {"bg": "#1e1e1e", "fg": "white"},
            "Colorblind Mode": {"bg": "#fdf6e3", "fg": "black"}
        }
        selected = colors.get(mode, colors["Light Mode"])
        self.root.configure(bg=selected["bg"])
        for widget in self.root.winfo_children():
            try:
                widget.configure(bg=selected["bg"], fg=selected["fg"])
            except:
                pass

    def setup_input_section(self):
        """Set up input sequence section"""
        frame = tk.LabelFrame(self.root, text="Input Sequence", padx=5, pady=5) #Create labeled frame
        frame.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky="nsew") #place labeled frame
        frame.grid_columnconfigure(0, weight=1) #text box expandable

        self.input_box = scrolledtext.ScrolledText(frame, height=10, width=80) #scrollable text box for inout
        self.input_box.grid(row=0, column=0, columnspan=2, sticky="nsew") #place input text box

    def setup_output_section(self):
        """Set up output section"""
        frame = tk.LabelFrame(self.root, text="Translation Results", padx=5, pady=5) #labeled frame container for output
        frame.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky="nsew") #place it
        frame.grid_columnconfigure(0, weight=1) #make text box expandable

        self.output_box = scrolledtext.ScrolledText(frame, height=10, width=80, state='disabled') #creates text box for results. scroll disabled.
        self.output_box.grid(row=0, column=0, columnspan=2, sticky="nsew") #place it

    def setup_direction_toggle(self):
        """Set up translation direction selector"""
        frame = tk.Frame(self.root) #create container frame for translation toggle
        frame.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky="w") #place it

        tk.Label(frame, text="Direction:").grid(row=0, column=0, padx=5) #adding label
        tk.OptionMenu(frame, self.translation_mode, "mRNA → Protein", "Protein → mRNA").grid(row=0, column=1) #add dropdown menu

    def setup_frame_selector(self):
        """Set up reading frame selector (only for mRNA→Protein)"""
        frame = tk.Frame(self.root) #create container frame
        frame.grid(row=4, column=1, padx=10, pady=5, sticky="e") #place it

        tk.Label(frame, text="Reading Frame:").grid(row=0, column=0, padx=5) #add label
        for i in range(1, 4): #add buttons for frames
            tk.Radiobutton(frame, text=str(i), variable=self.frame_var, value=i).grid(row=0, column=i)

    def setup_buttons(self):
        """Set up action buttons at bottom of window"""
        button_frame = tk.Frame(self.root) #create frame for buttons
        button_frame.grid(row=5, column=0, columnspan=3, pady=10) #place it

        #create buttons at bottom of the screen with respective commands
        tk.Button(button_frame, text="Upload FASTA", command=self.upload_fasta).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Translate", command=self.translate).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Reset", command=self.reset).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Download Output", command=self.download_output).grid(row=0, column=3, padx=5)

    def upload_fasta(selfself):
        messagebox.showinfo("FASTA Upload", "Need to configure")

    def translate(selfself):
        messagebox.showinfo("Translate", "Need to configure translation logic")

    def download_output(selfself):
        messagebox.showinfo("Download", "Download functionality coming soon")

    def reset(self):
        """Reset all fields"""
        self.input_box.delete("1.0", tk.END)
        self.output_box.configure(state='normal')
        self.output_box.delete("1.0", tk.END)
        self.output_box.configure(state='disabled')
        self.output_seq.set("")
        self.frame_var.set(1)
        self.translation_mode.set("mRNA → Protein")

def main():
    app = Translator()
    app.root.mainloop()


if __name__ == "__main__":
    main()
