# Ex 2
# Pgm that reads DNA sequence and returns the reverse complement

# opening file
with open ('seq1.txt', 'r') as seq:
    seq = seq.read()

# turning sequence into a list of nucleotides
seq_list = list(seq)

# filtering if there is any non-nucleotide character
new_seq = []
for i in seq_list:
    if i == 'G' or i == 'C' or i == 'T' or i == 'A':
        new_seq.append (i)

seq_list = new_seq

# generating the reverse complement list
reverse = []
for i in seq_list:
    if i == 'G':
        reverse.append ('C')
    if i == 'C':
        reverse.append ('G')
    if i == 'T':
        reverse.append ('A')
    if i == 'A':
        reverse.append ('T')

# nicely printing the reverse complement
oriseq_str = "".join (seq_list)
reverse_str = "".join (reverse)
print 'Original sequence: %s' % (oriseq_str)
print 'Reverse complement: %s' % (reverse_str)
