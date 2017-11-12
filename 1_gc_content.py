# Ex 1
# Pgm that reads DNA sequence and returns GC content

#opening file
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

# counting the number of G and C
count = 0
for i in seq_list:
    if i == 'G' or i == 'C':
        count += 1

# calculating the GC content of the sequence
gc_content = (float(count) / len(seq_list)) * 100

# nicely printing the GC content of the sequence
gc = ("{0:.2f}".format(gc_content))
print 'GC content = %s %%' % (gc)
