'''
This library takes as input a 3' UTR annotation file derived from GENCODE annotation using the script
annotate_3utr.R

Input: ref_file
'''

import argparse
import pandas as pd

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('ref_file', help='3\' UTR annotation file generated by annotate_3utr.R')

	args = parser.parse_args()

	# ref file must be tab separated with six columns and first line as header.
	ref = pd.read_table(args.ref_file, sep='\t')


