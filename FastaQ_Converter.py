'''
This program help to convert DNA sequences obtained from next generation sequencing.
After conversion, the raw data are ready for analysis by tools provided on NCBI platform.

'''
from Bio import SeqIO

SeqIO.convert('input.fastq','fastq','output.fasta','fasta')
