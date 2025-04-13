#################################################################################
# Author: Constance Falucskai & Liz Miller
# Username: falucskaic & millere4
#
# Assignment: PO1-Final Project
# Purpose: To make a codon chart referencable by mRNA to amino acid translator.
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

"""lists codon chart in a dictionary for reference
    codon: three nucleotides coding for a particular amino acid"""

""" F=Phe=Phenylalanine, L=Leu=Leucine, S=Ser=Serine, Y=Tyr=Tyrosine, C=Cys=Cysteine, W=Trp=Tryptophan P=Pro=Proline, H=His=Histidine, 
Q=Gin=Glutamate, R=Arg=Arginine, I=Ile=Isoleucine, M=Met=Methionine(START), T=Thr=Threonine, N=Asn=Asparagine, 
K=Lys=Lysine, V=Val=Valine, A=Ala=Alanine, D=Asp=Aspartic acid, E=Glu=Glutamic acid, G=Gly=Glycine"""

condon_table = dict( F={'UUU', 'UUC'}, L={'UUA', 'UUG', 'CUU','CUC','CUA', 'CUG'},S={'UCU','UCC','UCA','UCG','AGU','AGC'},
                     Y={'UAU','UAC'},C={'UGU','UGC'},W={'UGG'},P={'CCU','CCC','CCA','CCG'}, H={'CAU','CAC'},
                     Q={'CAA','CAG'},R={'CGU','CGC','CGA','CGG','AGA','AGG'}, I={'AUU','AUC','AUA'},M={'AUG'},
                     T={'ACU','ACC','ACA','ACG'}, N={'AUU','AAC'},K={'AAA','AAG'}, V={'GUU','GUC','GUA','GUG'},
                     A={'GCU','GCC','GCA','GCG'}, D={'GAU','GAC'},E={'GAA','GAG'},G={'GGU','GGC','GGA','GGG'},
                     STOP={'UAA','UAG','UGA'} )


'''testing for dictionary function as compiled sets'''
# sequ=['UUA','UUC','AAC']                          #series of codons assign as variable "sequ"
# amino_acid_chain=[]                                 #empty list used to store translated aa seq'''
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

'''It does WORK, AYAYAYAAYYAY!!!'''