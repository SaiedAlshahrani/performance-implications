#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
import time, logging
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

alpha=0.03
min_count=1
window_size=2
train_epoch=20
vector_size=300
min_alpha=0.0007
negative_size=20
sampling_threshold=6e-5
worker_count=multiprocessing.cpu_count()

if __name__ == '__main__':

    if len(sys.argv) < 5:
        print('Usage: python word2vec_train.py <wikipedia_dump_text_file> <word2vec_algorithm:0->cbow,1->skip-gram> <save_bin_model> <save_model_vectors>')
        sys.exit(1)

    wiki_corpus, w2v_algorithm, save_bin_model, save_model_vectors = sys.argv[1:5]

    logging.basicConfig(filename=f'{save_bin_model}.log',filemode='a',format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    print(f"# Training Word2Vec on '{wiki_corpus.split('/')[1]}' in progress!")
    os.system(f"echo 'python {sys.argv[0]} {sys.argv[1]} {sys.argv[2]} {sys.argv[3]} {sys.argv[4]}' >> {save_bin_model}.log")

    print(f"  >> Logging information is sent/saved to '{save_bin_model}.log' ...")

    start_time = time.time()

    model = Word2Vec(LineSentence(wiki_corpus), vector_size=vector_size, window=window_size, min_count=min_count, sample=sampling_threshold, hs=0,
            alpha=alpha, min_alpha=min_alpha, workers=worker_count, sg=w2v_algorithm, negative=negative_size, cbow_mean=1, epochs=train_epoch)

    model.save(save_bin_model)
    model.wv.save_word2vec_format(save_model_vectors, binary=False)

    end_time = time.time() - start_time

    print(f"# Total Training Execution Time: {round((end_time), 2)} Seconds.")
    os.system(f"echo '# Total Training Execution Time: {round((end_time), 2)} Seconds.' >> {save_bin_model}.log")
