# Performance Implications of Using Unrepresentative Corpora in Arabic Natural Language Processing

We, in this repository, share with the community our evaluation scripts for ([Word Representation Task](https://github.com/SaiedAlshahrani/performance-implications/tree/main/Word-Representation-Evals) and [Language Modeling Task](https://github.com/SaiedAlshahrani/performance-implications/tree/main/Language-Modeling-Evals)), created datasets ([Arab States Analogy Dataset (ASAD)](https://github.com/SaiedAlshahrani/performance-implications/tree/main/Word-Representation-Evals/ASAD) and [Masked Arab States Dataset (MASD)](https://github.com/SaiedAlshahrani/performance-implications/tree/main/Language-Modeling-Evals/MASD)), extracted corpora ([Wikipedia Corpora Creation](https://github.com/SaiedAlshahrani/performance-implications/tree/main/Wikipedia-Corpora-Creation)), and trained models ([Training Scripts](https://github.com/SaiedAlshahrani/performance-implications/tree/main/Word-Representation-Evals/Training-Scripts)) for our accepted paper, **[Performance Implications of Using Unrepresentative Corpora in Arabic Natural Language Processing](https://webspace.clarkson.edu/~alshahsf/unrepresentative_corpora.pdf)**, at *[The First Arabic Natural Language Processing Conference (ArabicNLP 2023)](https://sites.google.com/view/wanlp2023)*, co-located with [EMNLP 2023](https://2023.emnlp.org/) in Singapore (hybrid conference), December 7, 2023. 

```bash
@inproceedings{alshahrani-etal-2022-learning,
    title = "Learning From {A}rabic Corpora But Not Always From {A}rabic Speakers: A Case Study of the {A}rabic {W}ikipedia Editions",
    author = "Alshahrani, Saied  and
      Wali, Esma  and
      Matthews, Jeanna",
    booktitle = "Proceedings of the The Seventh Arabic Natural Language Processing Workshop (WANLP)",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates (Hybrid)",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.wanlp-1.34",
    doi = "10.18653/v1/2022.wanlp-1.34",
    pages = "361--371",
    abstract = "Wikipedia is a common source of training data for Natural Language Processing (NLP) research, especially as a source for corpora in languages other than English. However, for many downstream NLP tasks, it is important to understand the degree to which these corpora reflect representative contributions of native speakers. In particular, many entries in a given language may be translated from other languages or produced through other automated mechanisms. Language models built using corpora like Wikipedia can embed history, culture, bias, stereotypes, politics, and more, but it is important to understand whose views are actually being represented. In this paper, we present a case study focusing specifically on differences among the Arabic Wikipedia editions (Modern Standard Arabic, Egyptian, and Moroccan). In particular, we document issues in the Egyptian Arabic Wikipedia with automatic creation/generation and translation of content pages from English without human supervision. These issues could substantially affect the performance and accuracy of Large Language Models (LLMs) trained from these corpora, producing models that lack the cultural richness and meaningful representation of native speakers. Fortunately, the metadata maintained by Wikipedia provides visibility into these issues, but unfortunately, this is not the case for all corpora used to train LLMs.",
}
```