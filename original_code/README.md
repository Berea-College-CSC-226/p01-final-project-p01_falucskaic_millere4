This folder is for holding your original assignments that you are using as a reference. 
Put the code in this folder, but DO NOT modify it directly! 
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
#   Ideas borrowed from j. ben Schafer: https://www.cs.uni.edu/~schafer/
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################


def is_nucleotide(sequence):
    """
    Checks that the string sequence provided is a valid string
    consisting only of the 4 nucleotides A, C, G, and T
    Returns True if so, and False otherwise

    :param sequence: A string representing a DNA sequence
    :return: True is the sequence is valid, otherwise False
    """

    valid_nucleotides = {"A", "C", "G", "T"} # define value of the nucleotides as a set
    return all(base in valid_nucleotides for base in sequence) #returns True if all characters valid.



def complement_strand(sequence):
    """
    Returns the string which will be the second strand of the DNA sequence
    given that Ts complement As, and Cs complement Gs. If given
    a bad input, the function returns "Sequencing Error"

    :param sequence:
    :return: The complementary DNA strand as a string or sequencing error if not valid
    """

    if not is_nucleotide(sequence): #check if the input is valid sequence
        return "Sequencing Error" #returns error message if invalid

    complement_map = {"A": "T", "T": "A", "C": "G", "G": "C"} #dictionary mapping nucleotides to complements
    return "".join(complement_map[base] for base in sequence)  #replaces bases with complements


def mRNA(sequence):
    """
    Replaces each occurrence of the nucleotide T replaced with the nucleotide U.

    :param sequence: A string representing a DNA sequence
    :return: A string representing the corresponding mRNA sequence
    """

    if not is_nucleotide(sequence): #validate input sequence
        return "Sequencing Error" #return error is input invalid

    return sequence.replace("T", "U") #replace are Ts with Us


def chunk_amino_acid(sequence):
    """
    Uses output of mRNA(sequence) and divides it into substrings of length 3,
    ignoring any "extra DNA" at the far end returning the relevant substrings in a list.

    :param sequence: A string representing an mRNA sequence
    :return:  A list of codons (triplets).
    """

    return [sequence[i:i + 3] for i in range(0, len(sequence) - (len(sequence) % 3), 3)]
    # sees if there are any extra nucleotides with len and % and removes andy extra nucleotides at the end. Uses range with a step of 3 and excludes and extra nucleotides. It then extracts triplets as the list loops through the sequences using i values from the range.

def translate_amino_acid(three_char_seq):
    """
    Expects a three character string as a parameter and returns
    the corresponding single character amino acid

    :param three_char_seq: a sequence of three characters
    :return: A string representing the amino acid chunk for that sequence
    """

    # ###################################################################### #
    # #  This function is already completed correctly! No changes needed!  # #
    # ###################################################################### #

    translator = {"GCA": "A", "GCC": "A", "GCG": "A", "GCU": "A",
                  "AGA": "R", "AGG": "R", "CGA": "R", "CGC": "R", "CGG": "R", "CGU": "R",
                  "GAC": "D", "GAU": "D",
                  "AAC": "N", "AAU": "N",
                  "UGC": "C", "UGU": "C",
                  "GAA": "E", "GAG": "E",
                  "CAA": "Q", "CAG": "Q",
                  "GGA": "G", "GGC": "G", "GGU": "G", "GGG": "G",
                  "CAC": "H", "CAU": "H",
                  "AUA": "I", "AUC": "I", "AUU": "I",
                  "UUA": "L", "UUG": "L", "CUA": "L", "CUC": "L", "CUG": "L", "CUU": "L",
                  "AAA": "K", "AAG": "K",
                  "AUG": "M",
                  "UUC": "F", "UUU": "F",
                  "CCA": "P", "CCC": "P", "CCG": "P", "CCU": "P",
                  "AGC": "S", "AGU": "S", "UCA": "S", "UCC": "S", "UCG": "S", "UCU": "S",
                  "ACA": "T", "ACC": "T", "ACG": "T", "ACU": "T",
                  "UGG": "W",
                  "UAC": "Y", "UAU": "Y",
                  "GUA": "V", "GUC": "V", "GUG": "V", "GUU": "V",
                  "UAA": "*", "UAG": "*", "UGA": "*"
                 }

    if three_char_seq in translator.keys():
        return translator[three_char_seq]  # Given any 3 letter sequence, this returns the amino acid for that sequence
    else:
        return "?"                          # Returns a question mark if the input is invalid


def sequence_gene(sequence):
    """
    The sequence_gene() function takes a sequence of nucleotides and returns
    the corresponding amino acid sequence.

    :param sequence: a string representing a sequence of nucleotides
    :return: a string representing the amino acid sequence
    """

    # ###################################################################### #
    # #  This function is already completed correctly! No changes needed!  # #
    # ###################################################################### #

    aaseq=""                                                # Amino acid sequence
    if is_nucleotide(sequence):                             # Checks for a valid sequence
        comp_strand = complement_strand(sequence)           # Finds the complement sequence
        mrna = mRNA(comp_strand)                            # Finds the mRNA of the complement
        amino_acid_list = chunk_amino_acid(mrna)            # Chunks the mRNA sequence

        for amino_acid in amino_acid_list:                  # Loops through each chunk
            aaseq = aaseq + translate_amino_acid(amino_acid)   # Creates the final amino acid sequence
    return aaseq                                            # Returns an empty string for any illegal input


def main():
    """
    The main() function runs the sequence_gene code, which calls all other parts of this code

    :return: None
    """

    # ###################################################################### #
    # #  This function is already completed correctly! No changes needed!  # #
    # ###################################################################### #
    print("The original sequence {0} returns {1}".format("CACGT", sequence_gene("CACGT")))


if __name__ == "__main__":
    main()          # call to main() function


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
# T12: Events and GUIs
#
# Purpose: Show interactive DNA strand copying using the turtle library.
#  This program also uses both mouse click and keypress event handling.
#  The mouse click causes the complementary nucleotides to appear under
#  the base that the user clicks on in the DNA strand.
# ######################################################################
# Acknowledgements:
#
# Original code written by Dr. Mario Nakazawa
# Previously modified by Scott Heggen and Brian Schack
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle, random

# Global variables which will be used throughout the program.
global nucleotides
nucleotides = {"A": "pink", "T": "green", "C": "magenta", "G": "yellow"}

global complement
complement = {"T": "A", "A": "T", "G": "C", "C": "G"}

global max_bases                # We'll be using this variable inside an event handler, so it needs global scope
max_bases = 4


def draw_scaffold():
    """
    Create the top and bottom scaffold for the nucleotides
    to be added afterwards.

    :return: None
    """

    dna_protein = turtle.Turtle()
    dna_protein.hideturtle()
    dna_protein.shape("square")
    dna_protein.penup()
    dna_protein.setpos(-260,230)
    dna_protein.pendown()
    dna_protein.pensize(20)
    dna_protein.forward(500)

    dna_protein.penup()
    dna_protein.setpos(-260,-42)
    dna_protein.pendown()
    dna_protein.pensize(20)
    dna_protein.forward(500)

    dna_protein.penup()
    dna_protein.setpos(0,-170)
    dna_protein.write("Click on the black square for each nucleotide \nin the DNA strand created at the top\nto get the complement in the strand at the bottom!\n\nPress 'q' to quit.", move=False,align='center',font=("Arial",15,("bold","normal")))


def draw_random_DNA(current_base_turtle, base_index, letter):
    """
    Draw a random sequence to be used later to create the complementary base pair.

    :param current_base_turtle: a turtle object
    :param base_index: an index, to help position the turtle
    :param letter: the letter being drawn
    :return: None
    """
    current_base_turtle.penup()
    current_base_turtle.right(90)
    current_base_turtle.setpos(-250 + 95*base_index, 230)       # Moves the turtle right the appropriate amount
    current_base_turtle.pendown()
    current_base_turtle.shape("square")
    current_base_turtle.pensize(10)
    current_base_turtle.forward(50)
    current_base_turtle.color(nucleotides[letter])
    current_base_turtle.pensize(30)
    current_base_turtle.forward(70)
    current_base_turtle.backward(40)
    current_base_turtle.color("black")

    # draw out the letters for the base_turtles and return back to the center.
    (xpos, ypos) = current_base_turtle.pos()
    letter_turtle.setpos(xpos, ypos+5 )
    letter_turtle.write(letter,move=False,align='center',font=("Arial",25,("bold","normal")))
    letter_turtle.setpos(0,0)


def draw_complement(letter, x, y):
        """
        Draws the complement strand for a given letter at the correct location.

        :param letter: the base letter
        :param x: the mouse x-coordinate
        :param y: the mouse y-coordinate
        :return: None
        """
        pair_turtle = turtle.Turtle()
        pair_turtle.hideturtle()
        pair_turtle.penup()
        pair_turtle.goto(x, y)
        pair_turtle.right(90)
        pair_turtle.forward(190)
        pair_turtle.pendown()
        pair_turtle.color("black")
        pair_turtle.pensize(10)
        pair_turtle.back(50)
        pair_turtle.color(nucleotides[complement[letter]])          # sets the color to the complement's color
        pair_turtle.pensize(30)

        (x_pos, y_pos) = pair_turtle.pos()

        pair_turtle.back(70)
        pair_turtle.penup()

        # draw the letter for that base
        letter_turtle.setpos(x_pos, y_pos - 10)
        letter_turtle.write(complement[letter], move=False, align='center', font=("Arial", 25, ("bold", "normal")))
        letter_turtle.setpos(0, 0)

        # Resets stuff
        pair_turtle.back(70)
        pair_turtle.showturtle()
        pair_turtle.color("black")


def base_handler(x, y):
    """
    Event handler for clicks on turtles.
    Draws the complement strand.
    Each turtle reuses this handler.

    :param x: x-coordinate of the mouse
    :param y: y-coordinate of the mouse
    :return: None
    """
    global current_letter
    global current_base

    draw_complement(current_letter, x, y)           # Draw the complement strand
    current_base += 1
    if current_base <= max_bases:
        # Repeat the program up to four times. Creates a new letter, new turtle, and reuses the click handler base_handler
        current_letter = random.choice(list(nucleotides.keys()))
        base_turtle = turtle.Turtle()
        draw_random_DNA(base_turtle, current_base, current_letter)
        base_turtle.onclick(base_handler)


def main():
    """
    Interactive DNA sequence drawing program.

    :return: None
    """
    global letter_turtle            # We'll be using this variable inside an event handler, so it needs global scope
    global current_base             # We'll be using this variable inside an event handler, so it needs global scope
    global current_letter           # We'll be using this variable inside an event handler, so it needs global scope

    letter_turtle = turtle.Turtle()
    letter_turtle.hideturtle()
    letter_turtle.penup()

    draw_scaffold()

    current_base = 1
    current_letter = random.choice(list(nucleotides.keys()))        # Picks a random letter from the dictionary keys
    base_turtle = turtle.Turtle()

    draw_random_DNA(base_turtle, current_base, current_letter)      # Draws a random DNA

    base_turtle.onclick(base_handler)       # Binds the first turtle to the base_handler event handler

    # It's not common, but sometimes useful to define functions within other functions.
    def quit_program():
        """
        Event handler for quitting the program

        :return: None
        """
        wn.bye()

    wn = turtle.Screen()
    wn.onkey(quit_program, "q")     # Binds to the quit_program event handler above
    wn.listen()                     # Needed to capture events
    wn.mainloop()                   # Keeps the program running


main()

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

# T12: Events and GUIs
#
# Purpose: Show interactive DNA strand copying using the turtle library.
#  This program also uses both mouse click and keypress event handling.
#  The mouse click causes the complementary nucleotides to appear under
#  the base that the user clicks on in the DNA strand.
# ######################################################################
# Acknowledgements:
#
# Original code written by Dr. Mario Nakazawa
# Previously modified by Scott Heggen and Brian Schack
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle
import random


class DNADraw:
    # Class variables which will be used throughout the program.
    nucleotides = {"A": "pink", "T": "green", "C": "magenta", "G": "yellow"}
    complement = {"T": "A", "A": "T", "G": "C", "C": "G"}
    max_bases = 4
    
    def __init__(self):
        self.letter_turtle = turtle.Turtle()
        self.letter_turtle.hideturtle()
        self.letter_turtle.penup()
    
        self.draw_scaffold()
    
        self.current_base = 1
        self.current_letter = random.choice(list(self.nucleotides.keys()))        # Picks a random letter from the dictionary keys
        self.base_turtle = turtle.Turtle()
    
        self.draw_random_DNA()      # Draws a random DNA
    
        self.base_turtle.onclick(self.base_handler)       # Binds the first turtle to the base_handler event handler

        self.wn = turtle.Screen()
        self.wn.onkey(self.quit_program, "q")     # Binds to the quit_program event handler above
        self.wn.listen()                          # Needed to capture events
        self.wn.mainloop()                        # Keeps the program running

    def quit_program(self):
            """
            Event handler for quitting the program.

            :return: None
            """
            self.wn.bye()

    def draw_scaffold(self):
        """
        Create the top and bottom scaffold for the nucleotides
        to be added afterwards.
    
        :return: None
        """

        dna_protein = turtle.Turtle()
        dna_protein.hideturtle()
        dna_protein.shape("square")
        dna_protein.penup()
        dna_protein.setpos(-260,230)
        dna_protein.pendown()
        dna_protein.pensize(20)
        dna_protein.forward(500)
    
        dna_protein.penup()
        dna_protein.setpos(-260,-42)
        dna_protein.pendown()
        dna_protein.pensize(20)
        dna_protein.forward(500)
    
        dna_protein.penup()
        dna_protein.setpos(0,-170)
        dna_protein.write("Click on the black square for each nucleotide \nin the DNA strand created at the top\nto get the complement in the strand at the bottom!\n\nPress 'q' to quit.", move=False,align='center',font=("Arial",15,("bold","normal")))

    def draw_random_DNA(self):
        """
        Draw a random sequence to be used later to create he complementary base pair

        :return: None
        """
        self.base_turtle.penup()
        self.base_turtle.right(90)
        self.base_turtle.setpos(-250 + 95 * self.current_base, 230)
        self.base_turtle.pendown()
        self.base_turtle.shape("square")
        self.base_turtle.pensize(10)
        self.base_turtle.forward(50)
        self.base_turtle.color(self.nucleotides[self.current_letter])
        self.base_turtle.pensize(30)
        self.base_turtle.forward(70)
        self.base_turtle.backward(40)
        self.base_turtle.color("black")
    
        # draw out the letters for the base_turtles and return back to the center.
        (xpos, ypos) = self.base_turtle.pos()
        self.letter_turtle.setpos(xpos, ypos+5)
        self.letter_turtle.write(self.current_letter, move=False, align='center',
                                 font=("Arial", 25, ("bold", "normal")))
        self.letter_turtle.setpos(0,0)

    def draw_complement(self, x, y):
        """
        Draws the complement strand for a given letter at the correct location

        :param x: the mouse x-coordinate
        :param y: the mouse y-coordinate
        :return: None
        """
        pair_turtle = turtle.Turtle()
        pair_turtle.hideturtle()
        pair_turtle.penup()
        pair_turtle.goto(x, y)
        pair_turtle.right(90)
        pair_turtle.forward(190)
        pair_turtle.pendown()
        pair_turtle.color("black")
        pair_turtle.pensize(10)
        pair_turtle.back(50)
        # sets the color to the complement's color
        pair_turtle.color(self.nucleotides[self.complement[self.current_letter]])
        pair_turtle.pensize(30)

        (x_pos, y_pos) = pair_turtle.pos()

        pair_turtle.back(70)
        pair_turtle.penup()

        # draw the letter for that base
        self.letter_turtle.setpos(x_pos, y_pos - 10)
        self.letter_turtle.write(self.complement[self.current_letter], move=False, align='center',
                                 font=("Arial", 25, ("bold", "normal")))
        self.letter_turtle.setpos(0, 0)

        # Resets stuff
        pair_turtle.back(70)
        pair_turtle.showturtle()
        pair_turtle.color("black")

    def base_handler(self, x, y):
        """
        Event handler for clicks on turtles.
        Draws the complement strand.
        Each turtle reuses this handler.
    
        :param x: x-coordinate of the mouse
        :param y: y-coordinate of the mouse
        :return: None
        """

        self.draw_complement(x, y)           # Draw the complement strand
        self.current_base += 1
        if self.current_base <= self.max_bases:
            # Repeat the program up to 4x. Creates a new letter, new turtle, and reuses the click handler base_handler
            self.current_letter = random.choice(list(self.nucleotides.keys()))
            self.base_turtle = turtle.Turtle()
            # A better solution here uses a collaboration with a Nucleotide object and spawns new ones,
            # eliminating the issue from the Google Doc with every nucleotide being clickable.
            self.draw_random_DNA()
            self.base_turtle.onclick(self.base_handler)


def main():
    """
    Interactive DNA sequence drawing program.

    :return: None
    """

    dna = DNADraw()     # Yup. that's it!
    # DNADraw()           # Technically, this would work also. Why?


main()
