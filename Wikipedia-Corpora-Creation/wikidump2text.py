"""
Creates a corpus from Wikipedia dump file.
Inspired by:
https://github.com/panyang/Wikipedia_Word2vec/blob/master/v1/process_wiki.py
"""

import sys , warnings
warnings.filterwarnings("ignore")
from gensim.corpora import WikiCorpus



def make_corpus(input_file, output_file):
	"""Convert Wikipedia xml dump file to text corpus"""
	outputs = open(output_file, 'w')

	i = 0

	for text in WikiCorpus(input_file).get_texts():
		outputs.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')
		i = i + 1
		if (i % 5000 == 0):
			print(f'  +Processed {i:,} articles')

	outputs.close()
	print(f'# Processing {i:,} articles complete!')


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Usage: python wikidump2text.py <wikipedia_xml_dump_bz2_file> <processed_corpus_text_file>')
		sys.exit(1)

	input_file = sys.argv[1]
	output_file = sys.argv[2]
	print(f'# Processing [{sys.argv[1].split("/")[-1]}]:')
	make_corpus(input_file, output_file)
