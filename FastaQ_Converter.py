'''
This program help to convert and trim DNA sequences obtained from next generation sequencing.
After conversion, the raw data are ready for analysis by tools provided on NCBI platform.

'''
from Bio import SeqIO

SeqIO.convert('6427_6418_N_in_R1.fastq','fastq','trimmed_in.fasta','fasta')
