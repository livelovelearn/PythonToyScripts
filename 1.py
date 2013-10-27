'''from Bio import SeqIO;
SeqIO.convert('untrimmed.fq','fastq','trimmed.fasta','fasta')
'''
from Bio import SeqIO
records = (rec[:21] for rec in SeqIO.parse(open("untrimmed.fq"), "fastq-solexa"))
handle = open("trimmed21.fastq", "w")
count = SeqIO.write(records, handle, "fastq-solexa")
handle.close()

