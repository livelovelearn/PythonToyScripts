'''
This program help to convert and trim DNA sequences obtained from next generation sequencing.
After conversion, the raw data are ready for analysis by tools provided on NCBI platform.

'''
from Bio import SeqIO

records = (rec[:21] for rec in SeqIO.parse(open("untrimmed.fq"), "fastq-solexa"))

savedFile = open("trimmed21.fastq", "w")

count = SeqIO.write(records, savedFile, "fastq-solexa")

handle.close()

