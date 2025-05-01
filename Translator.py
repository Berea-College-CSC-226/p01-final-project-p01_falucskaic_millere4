#################################################################################
# Author: Constance Falucskai & Liz Miller
# Username: falucskaic & millere4
#
# Assignment: PO1-Final Project
# Purpose: Create a Translator class that references the codon chart to return an mRNA>amino acic (aa) transtlation -or-
#          semi- tranlate protein seq > aa (returns a list of possible aa codons for each aa)
# Google Doc Link:
#
#################################################################################
# Acknowledgements:
#   Geeks for Geeks :
#       https://www.geeksforgeeks.org/creating-dictionary-of-sets-in-python/
#       https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
#       https://www.geeksforgeeks.org/python-len-function/
#       https://www.geeksforgeeks.org/python-program-to-concatenate-all-elements-of-a-list-into-a-string/
#       https://www.geeksforgeeks.org/python-dict-function/ **
#   PythonGuides
#       https://pythonguides.com/python-dictionary-find-a-key-by-value/
#       https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
#       https://docs.python.org/3/library/functions.html#print
#   StacksOverFlow
#       https://stackoverflow.com/questions/43982938/split-string-into-groups-of-3-characters **
#       https://stackoverflow.com/questions/24805709/python-combine-all-items-in-a-list-into-a-string
#       https://stackoverflow.com/posts/35982511/revisions
#   W3schools
#       https://www.w3schools.com/python/ref_func_len.asp
#       https://www.w3schools.com/python/python_ref_dictionary.asp **
#   datagy
#       https://datagy.io/append-to-lists-python/
#
#        **-->(not used... yet, maybe translator?, working on understanding the actual code before trying to implement)
#################################################################################

from mRNA_codon_chart import condon_table

class translator(mRNA,aa) :
    def __init__(self):
        
        print(self)
        def sequence_reader(self):
            seq=self
            print(seq)
#         # sequ=['UUA','UUC','AAC']                          #series of codons assign as variable "sequ"
#         amino_acid_chain=[]                                 #empty list used to store translated aa seq'''
#
# for seq in sequ:                                    #creates variable seq and starts loop through each codon in "sequ"
#     for key,value in condon_table.items():          #tells code to look in the codon table for keys&val assc.
#
#         if seq in value:                          #'''searches codon_table for the codon stored in the variable seq'''
#             print(key)                            #''' step check to confirm key is referenced correctly by code'''
#             amino_acid_chain.extend([key])       #'''updates the key, or single letter aa, in aa list variable named
#                                                  #      amino_acid_chain'''
#
# aa=' '.join(amino_acid_chain)                     #'''concatenates amino_acid_chain and removes commas'''
# print (amino_acid_chain)                          #'''print check to confirm order is maintained'''
# print(aa)                                         #'''confirms order and comma removal--how to remove space?'''

a="'UUAUUCAAC'"
translator(a,)

'''It does WORK, AYAYAYAAYYAY!!!'''