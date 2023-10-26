# Wikipedia Corpora Creation

To create a corpus (extract articles) for a Wikipedia edition/language, you should follow these steps:

1- Download a Wikipedia XML Dump file for your desired language from here: [Wikimedia Downloads](https://dumps.wikimedia.org/backup-index.html). You can download the Wikipedia Dump file using `wget` Unix/Linux utility. For example, to download the **Modern Standard Arabic** Wikipedia XML Dump file for the latest backup, use this command in your terminal:

```bash
wget https://dumps.wikimedia.org/arwiki/latest/arwiki-latest-pages-articles.xml.bz2
```

2- Once you download the Wikipedia XML Dump file for your desired language, you can process it using `Gensim` Python library. We share the Python script we used to create a corpus from Wikipedia XML Dump file ([wikidump2text.py](https://github.com/SaiedAlshahrani/performance-implications/blob/main/Wikipedia-Corpora-Creation/wikidump2text.py)). To run this script, use this command in your terminal and provide it with the Wikipedia XML Dump file and your desired name for the extracted corpus:

```bash
python wikidump2text.py <wikipedia_xml_dump_bz2_file> <processed_corpus_text_file> 
```

3- Once the corpus is extracted, you can use our preprocessing Shell script ([preprocess.sh](https://github.com/SaiedAlshahrani/performance-implications/blob/main/Wikipedia-Corpora-Creation/preprocess.sh))to preprocess the extracted corpus lightly. The script removes the optional diacritical marks and Latin letters and numbers; it does not do any stemming, lemmatization, or text normalization. The script utilizes the command-line tools of `CAMeL Tools` and `tr` Unix/Linux utility. To run this script, use this command in your terminal and provide it with the name for the extracted corpus file and the desired name for the preprocessed corpus:

```bash
bash preprocess.sh <processed_corpus_text_file> <preprocessed_corpus_text_file>
```

### Bot-generated Articles Exclusion: 
_*You should use a Python virtual environment for this experiment._

We exclude all the bot-generated articles from the Modern Standard Arabic and Arabic Moroccan Wikipedia editions. We use Wikimedia [XTools](https://www.mediawiki.org/wiki/XTools) API to identify Wikipedia articles’ authors and use Wikipedia’s “[List Users](https://ar.wikipedia.org/wiki/خاص:عرض_المستخدمين)” service to retrieve the full list of bots in the targeted Wikipedia edition (*Do not forget to change the Wikipedia code accordingly; it is `ar` for the Modern Standard Arabic Wikipedia in the link above*) to disclose and remove the articles whose authors are in the bots list. 

We automate and integrate all these API calls into the `Gensim` Python library, specifically in its [corpora.wikicorpus](https://radimrehurek.com/gensim/corpora/wikicorpus.html) module. You only need to copy (and replace) our modified version of [wikicorpus.py](https://github.com/SaiedAlshahrani/performance-implications/blob/main/Wikipedia-Corpora-Creation/wikicorpus.py) to the `Gensim`'s local directory; it is usually part of this path (`///python*.**/site-packages/gensim/corpora/wikicorpus.py`).


> **Once the copy and replace is done, you can follow the above steps (1, 2, and 3) to download, extract, process, and preprocess a Wikipedia XML Dump file to create a corpus _without_ bot-generated articles.** 


# Arabic Wikipedia Editions' Corpora
We host our already extracted, processed, and preprocessed Arabic Wikipedia editions' corpora on the Hugging Face Hub. See the Table below for the details.
