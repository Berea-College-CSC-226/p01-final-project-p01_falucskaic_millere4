######################################################################
# Author: Liz Miller and Constance Falucskai
# Username: millere4 and falucskaic
#
# P01- Final Project
#######################################################################
# Acknowledgements:
# Codon Table source: https://www.genscript.com/tools/codon-table
#
####################################################################################
# DNA to Protein

codon_table = {
    'TTT': 'F', 'TTC': 'F',                                                  # Phenylalanine
    'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',  # Leucine
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I',                                      # Isoleucine
    'ATG': 'M',                                                              # Methionine (START)
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',                          # Valine
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT': 'S', 'AGC': 'S',  # Serine
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',                          # Proline
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',                          # Threonine
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',                          # Alanine
    'TAT': 'Y', 'TAC': 'Y',                                                  # Tyrosine
    'TAA': '*', 'TAG': '*', 'TGA': '*',                                      # STOP codons
    'CAT': 'H', 'CAC': 'H',                                                  # Histidine
    'CAA': 'Q', 'CAG': 'Q',                                                  # Glutamine
    'AAT': 'N', 'AAC': 'N',                                                  # Asparagine
    'AAA': 'K', 'AAG': 'K',                                                  # Lysine
    'GAT': 'D', 'GAC': 'D',                                                  # Aspartic Acid
    'GAA': 'E', 'GAG': 'E',                                                  # Glutamic Acid
    'TGT': 'C', 'TGC': 'C',                                                  # Cysteine
    'TGG': 'W',                                                              # Tryptophan
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',  # Arginine
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'                           # Glycine
}

