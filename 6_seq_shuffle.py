#Exo 6
# Write a program that reads a DNA sequence and shuffles the sequence.

# Opening sequence file
with open ('seq1.txt', 'r') as seq:
    seq = seq.read()

# Sequence > list of nucleotides
seq_list = list(seq)

# Filter if any non-nucleotide character
new_seq = []
for i in seq_list:
    if i == 'G' or i == 'C' or i == 'T' or i == 'A':
        new_seq.append (i)
seq_list = new_seq

# Putting the sequence back in the str
seq = ''.join (seq_list)

###################################################################
# Shuffle the sequence

import random
seq_list_shuffled = (random.sample (seq, len(seq)))
seq = ''.join (seq_list_shuffled)
print seq
