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
#Tkinter-mainloop- https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop
#Gui/tkinter- https://www.geeksforgeeks.org/python-gui-tkinter/
#https://realpython.com/python-gui-tkinter/
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
import tkinter as tk #GUI framework
from tkinter import scrolledtext, messagebox, filedialog #for widgets and dialog
import re #regex module for sequence cleaning

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

dna_codon_table = {codon.replace('U', 'T'): aa for codon, aa in mrna_codon_table.items()}

#dictionary of all 64 codons to their respective amino acids (1-letter codes) and stop codons are represented by '*'

########################################################################################################################

# --- Reverse Table: Protein → Codons ---
reverse_mrna_table = {}     #creates and empty list with no keys
for codon, aa in mrna_codon_table.items():
    reverse_mrna_table.setdefault(aa, []).append(codon) #looks up the hash table to see if there is an entry called "fruits." If it fins no entry for "fruits"
    """setdefault() is a built in python dictionary method, It's neat. worked well here to take---
        reverse_table = {}
        for codon, aa in codon_table.items():
            if aa not in reverse_table:
                reverse_table[aa] = []
            reverse_table[aa].append(codon)
    ---from 4 lines to 2 and it helps avoid keyError because it also adds fruits with a default 
    empty list"""
########################################################################################################################

#---Translator class---# User interface
class Translator:     #GUI application class
    def __init__(self):
        """Initialize the main application window"""
        self.root = tk.Tk() #initializaes main application window
        self.root.title("mRNA ↔ Protein Translator") #set window title
        self.root.minsize(800, 600) #set minimum window size

        # Configure grid weights for responsive resizing. Grid weights determine how extra space in a window is utilized
        self.root.grid_columnconfigure(1, weight=1) # Make column 1 expand horizontally when window is resized
        self.root.grid_rowconfigure(1, weight=1) # Make rows 1 and 2 expand vertically when window is resized
        self.root.grid_rowconfigure(2, weight=1) # ""
        """
        These grid configurations make sure our interface elements
        expand properly when the window is resized.
        """

        # ---Variables---#
        #self.input_seq = tk.StringVar() #for storing input
        #self.output_seq = tk.StringVar() #for sorting output

        self.color_mode = tk.StringVar(value="Light Mode") #Tracks color mode, sets default option Light Mode
        self.translation_mode = tk.StringVar(value="mRNA → Protein") #translation direction, sets default option to Protein
        self.frame_var = tk.IntVar(value=1)  #reading frame selection (1,2, or 3), set default reading frame to 1

        #builds interface
        self.setup_instructions() #adds instr. at top
        self.setup_mode_selector() #adds color mode dropdown
        self.setup_input_section() #adds input text box and upload button
        self.setup_output_section() #adds output text box and translate button
        self.setup_direction_toggle() #adds reading frame selection
        self.setup_frame_selector() #adds action buttons
        self.setup_buttons() #adds status bar

    def setup_instructions(self):
        """Add clear usage instructions at the top"""
        instructions = (
            "INSTRUCTIONS:\n"
            "1. Select translation direction (mRNA→Protein or Protein→mRNA)\n"
            "2. For mRNA→Protein: Select reading frame (1, 2, or 3)\n"
            "3. Paste sequence or upload FASTA file.\n *Manually remove FASTA title line. Include base pairs only*\n"
            "4. Click 'Translate' button\n"
            "5. Use 'Reset' to clear all fields, 'Download' to save results"
        )
        # Create instruction label with:
        # - Left-aligned text
        # - Helvetica font, size 10
        # - Wrapped to 650px width
        tk.Label(self.root, text=instructions, justify=tk.LEFT, anchor="w",
                font=('Helvetica', 10), wraplength=650).grid(
                row=0, column=0, columnspan=3, padx=10, pady=5, sticky="w")

    def setup_mode_selector(self):
        """Dropdown menu to select color theme."""
        modes = ["Light Mode", "Dark Mode", "Colorblind Mode"]
        tk.Label(self.root, text="Color Mode:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.OptionMenu(self.root, self.color_mode, *modes, command=self.apply_mode).grid(
            row=1, column=1, padx=10, pady=5, sticky="w") #uses sticky parameters to help control widget expansion

    def apply_mode(self, mode):
        """Apply selected color scheme"""
        colors = {
            "Light Mode": {"bg": "white", "fg": "black"},
            "Dark Mode": {"bg": "#1e1e1e", "fg": "white"},
            "Colorblind Mode": {"bg": "#fdf6e3", "fg": "black"}
        }
        selected = colors.get(mode, colors["Light Mode"]) #get colors form selected mode. Light mode is default.
        self.root.configure(bg=selected["bg"]) #apply to root window
        for widget in self.root.winfo_children(): #apply to all child widgets
            try:
                widget.configure(bg=selected["bg"], fg=selected["fg"])
            except:
                #skip widgets that don't support color config
                pass

    def setup_input_section(self):
        """Set up input sequence section"""
        #create labeled frame container:
        input_frame = tk.LabelFrame(self.root, text="Input Sequence", padx=5, pady=5) #create labeled frame
        input_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky="nsew") #place labeled frame- nsew= widget stuck to all four sides(N,S,E,W)
        input_frame.grid_columnconfigure(0, weight=1) #text box expandable

        self.input_box = scrolledtext.ScrolledText(input_frame, height=10, width=80) #scrollable text box for input
        self.input_box.grid(row=0, column=0, columnspan=2, sticky="nsew") #place input text box and fills entire frame

    def setup_output_section(self):
        """Set up output section"""
        output_frame = tk.LabelFrame(self.root, text="Translation Results", padx=5, pady=5) #labeled frame container for output
        output_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky="nsew") #place it
        output_frame.grid_columnconfigure(0, weight=1) #make first column expandable

        self.output_box = scrolledtext.ScrolledText(output_frame, height=10, width=80, state='disabled') #creates text box for results. scroll disabled.
        self.output_box.grid(row=0, column=0, columnspan=2, sticky="nsew") #place it

    def setup_direction_toggle(self):
        """Set up translation direction selector"""
        direction_frame = tk.Frame(self.root) #create container frame for translation toggle
        direction_frame.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky="w") #place it, left align

        tk.Label(direction_frame, text="Direction:").grid(row=0, column=0, padx=5) #adding label
        tk.OptionMenu(direction_frame, self.translation_mode, "mRNA → Protein", "Protein → mRNA", "DNA → Protein").grid(row=0, column=1) #add dropdown menu

    def setup_frame_selector(self):
        """Set up reading frame selector (only for mRNA→Protein)"""
        frame_frame = tk.Frame(self.root) #create container frame
        frame_frame.grid(row=4, column=1, padx=10, pady=5, sticky="e") #place it, right align

        tk.Label(frame_frame, text="Reading Frame:").grid(row=0, column=0, padx=5) #add label
        for i in range(1, 4): #add buttons for frames
            tk.Radiobutton(frame_frame, text=str(i), variable=self.frame_var, value=i).grid(row=0, column=i) #button label, group variable, and value when selected.

    def setup_buttons(self):
            """Upload, Translate, Reset, and Download buttons."""
            button_frame = tk.Frame(self.root)
            button_frame.grid(row=5, column=0, columnspan=3, pady=10)

            self.upload_btn = tk.Button(button_frame, text="Upload FASTA", command=self.upload_fasta)
            self.translate_btn = tk.Button(button_frame, text="Translate", command=self.translate)
            self.reset_btn = tk.Button(button_frame, text="Reset", command=self.reset)
            self.download_btn = tk.Button(button_frame, text="Download Output", command=self.download_output)

            # Place buttons in grid
            self.upload_btn.grid(row=0, column=0, padx=5)
            self.translate_btn.grid(row=0, column=1, padx=5)
            self.reset_btn.grid(row=0, column=2, padx=5)
            self.download_btn.grid(row=0, column=3, padx=5)

            #can now modify any button later
            #self.translate_btn.config(state='normal')  # Enable/disable as needed

    def clean_sequence(self, sequence):
        """Remove non-alphabetic characters and normalize case"""
        # Remove anything that's not a letter, then uppercase:
        return re.sub(r'[^a-zA-Z]', '', sequence).upper()

    def validate_mrna(self, sequence):
        """Check mRNA contains only valid bases (A,U,G,C)"""

        valid_bases = {'A', 'U', 'G', 'C', 'U'}  # Allowed nucleotides
        found=set(sequence)
        if found - valid_bases:
            messagebox.showerror("Invalid Input", f"Invalid characters: {', '.join(found - valid_bases)}")
            return False
        return True

    def validate_protein(self, sequence):
        """Ensure valid amino acid symbols."""
        valid = set(mrna_codon_table.values())
        found = set(sequence)
        if found - valid:
            messagebox.showerror("Invalid Input", f"Invalid amino acids: {', '.join(found - valid)}")
            return False
        return True

    def validate_dna(self, sequence):
        """Ensure DNA sequence only contains A, T, G, C."""
        valid = {'A', 'T', 'G', 'C'}
        found = set(sequence)
        if found - valid:
            messagebox.showerror("Invalid Input", f"Invalid DNA bases: {', '.join(found - valid)}")
            return False
        return True

    def translate(self):
        """translation with error handling"""
        try:
            raw_seq = self.clean_sequence(self.input_box.get("1.0", tk.END)) #gets input sequence from text box, strips whitespace
            if not raw_seq:
                messagebox.showwarning("Warning", "No input provided.")
                return

        ###### Clear previous output ######
            self.output_box.configure(state='normal')
            self.output_box.delete("1.0", tk.END)

            mode = self.translation_mode.get()

            if mode == "mRNA → Protein":
                if not self.validate_mrna(raw_seq): return
                frame = self.frame_var.get() - 1
                seq = raw_seq[frame:]
                remainder = len(seq) % 3
                if remainder:
                    messagebox.showwarning("Incomplete Codon", f"Trimming {remainder} base(s) off end.")
                    seq = seq[:-(remainder)]
                protein = "".join([mrna_codon_table.get(seq[i:i + 3], '?') for i in range(0, len(seq), 3)])
                self.output_box.insert(tk.END, protein)

            elif mode == "DNA → Protein":
                if not self.validate_dna(raw_seq): return
                frame = self.frame_var.get() - 1
                seq = raw_seq[frame:]
                remainder = len(seq) % 3
                if remainder:
                    messagebox.showwarning("Incomplete Codon", f"Trimming {remainder} base(s) off end.")
                    seq = seq[:-(remainder)]
                protein = "".join([dna_codon_table.get(seq[i:i + 3], '?') for i in range(0, len(seq), 3)])
                self.output_box.insert(tk.END, protein)

            elif mode == "Protein → mRNA":
                if not self.validate_protein(raw_seq): return
                results = [f"{aa}: {', '.join(reverse_mrna_table.get(aa, ['???']))}" for aa in raw_seq]
                self.output_box.insert(tk.END, "\n".join(results))
            else:
                if not self.validate_protein(raw_seq): return
                results = [f"{aa}: {', '.join(reverse_mrna_table.get(aa, ['???']))}" for aa in raw_seq]
                self.output_box.insert(tk.END, "\n".join(results))

        except Exception as e:
            messagebox.showerror("Error", str(e))

        finally:
            self.output_box.configure(state='disabled')

    def upload_fasta(self):
        """Open FASTA file and insert sequence into input box."""
        path = filedialog.askopenfilename(filetypes=[("FASTA files", "*.fasta *.fa *.txt")])
        if path:
            try:
                with open(path, 'r') as f:
                    seq = ''.join(line.strip().upper() for line in f if not line.startswith('>'))
                    self.input_box.delete("1.0", tk.END)
                    self.input_box.insert(tk.END, seq)
            except Exception as e:
                messagebox.showerror("Error", f"Could not read file: {e}")

    def download_output(self):  # No parameter needed
        """Save translation results to file"""
        output = self.output_box.get("1.0", tk.END)
        if not output.strip():
            messagebox.showwarning("Warning", "No output to download")
            return

        #Open save file dialog
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if path: #if user selected location
            try:
                with open(path, 'w') as f:
                    f.write(output)
                messagebox.showinfo("Success", "File saved successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")


    def reset(self):
        """Reset all fields to defaults"""
        self.input_box.delete("1.0", tk.END) #delete from the first character of the first line
        self.output_box.configure(state='normal') #temporarily removed ready only restrictions so the program can change the output box contents
        self.output_box.delete("1.0", tk.END) #delete all they way to the end of the box
        self.output_box.configure(state='disabled') #reengages normal read only output state for output box
        self.frame_var.set(1) #resets frame radio button back to frame 1 default
        self.translation_mode.set("mRNA → Protein") #resets translation mode back to MRNA to Protein default

def main():
    app = Translator() #create instance, builds the GUI
    app.root.mainloop() #starts event loop for the apps main window. It continuously listens for events like button clicks, window resizing etc. This is what makes the GUI actually appear and stay open

if __name__ == "__main__":
    main()
