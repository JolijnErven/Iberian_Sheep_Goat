import tskit
import pyslim
import sys

ts = tskit.load(sys.argv[1])
nts = pyslim.convert_alleles(pyslim.generate_nucleotides(ts))

with open(sys.argv[2], "w") as f:
    nts.write_vcf(f, contig_id=str(1))
