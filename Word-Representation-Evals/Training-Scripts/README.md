# Training Scripts
We share our Python training scripts of three context-independent word embedding algorithms and their variants. We have trained five models for each Arabic Wikipedia edition (Modern Standard Arabic, Egyptian Arabic, and Moroccan Arabic). You can follow these steps to replicate the training of the word embedding models. 

> We set these unified parameters of the three algorithms to these values: 
> {*vector-size*=300, *epochs*=20, *window-size*=2, *min-count*=1, *alpha*=0.03}.

1- **Word2Vec (continuous bag of words (cbow) and skip-gram)**: 

You can train these two variants of the Word2Vec algorithm using `Gensim` Python library or you can use our training script ([word2vec_train.py](https://github.com/SaiedAlshahrani/performance-implications/blob/main/Word-Representation-Evals/Training-Scripts/Word2Vec/word2vec_train.py)). To run this script, use this command in your terminal and provide it with the preprocessed Wikipedia corpus text file, the selected variant of Word2Vec (0 ---> cbow and 1 ---> skip-gram), the desired name for the model file, and the desired name for the vectors file.

```bash
python word2vec_train.py <wikipedia_dump_text_file> <word2vec_algorithm:0->cbow,1->skip-gram> <save_bin_model> <save_model_vectors>
```


2- **fastText (continuous bag of words (cbow) and skip-gram)**: 

You can train these two variants of the Word2Vec algorithm using `Gensim` Python library, or you can use our training script ([fasttext_train.py](https://github.com/SaiedAlshahrani/performance-implications/blob/main/Word-Representation-Evals/Training-Scripts/fastText/fasttext_train.py)). To run this script, use this command in your terminal and provide it with the preprocessed Wikipedia corpus text file, the selected variant of Word2Vec (0 ---> cbow and 1 ---> skip-gram), the desired name for the model file, and the desired name for the vectors file.

```bash
python fasttext_train.py <wikipedia_dump_text_file> <word2vec_algorithm:0->cbow,1->skip-gram> <save_bin_model> <save_model_vectors>
```