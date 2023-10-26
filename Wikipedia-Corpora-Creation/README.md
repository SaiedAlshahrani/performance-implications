# Wikipedia Corpora Creation

To create a corpus (extract articles) for a Wikipedia edition/language, you should follow these steps:

1- Download a Wikipedia XML Dump file for your desired language from here: [Wikimedia Downloads](https://dumps.wikimedia.org/backup-index.html). You can download the Wikipedia Dump file using `wget` Unix/Linux utility. For example, to download the **Arabic** Wikipedia XML Dump file for the latest backup, use this command in your terminal:

```bash
wget https://dumps.wikimedia.org/arwiki/latest/arwiki-latest-pages-articles.xml.bz2
```

2- Once you download the Wikipedia XML Dump file for your desired language, you can process it using `Gensim` Python library. We share the Python script we used to create a corpus from Wikipedia XML Dump file ([wikidump2text.py](https://github.com/SaiedAlshahrani/performance-implications/blob/main/Wikipedia-Corpora-Creation/wikidump2text.py)). To run this script, use this command in your terminal and provide it with the Wikipedia XML Dump file and your desired name for the extracted corpus:

```bash
python wikidump2text.py <wikipedia_xml_dump_bz2_file> <processed_corpus_text_file> 
```

3- Once the corpus is extracted, you can use our preprocessing Shell script to preprocess the extracted corpus lightly. The script removes the optional diacritical marks and Latin letters and numbers; it does not do any stemming, lemmatization, or text normalization. The script utilizes the command-line tools of `CAMeL Tools` and `tr` Unix/Linux utility. To run this script, use this command in your terminal and provide it with the name for the extracted corpus file and the desired name for the preprocessed corpus:

```bash
bash preprocess.sh <processed_corpus_text_file> <preprocessed_corpus_text_file>
```