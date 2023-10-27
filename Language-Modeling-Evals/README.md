# Language Modeling Evaluations

We evaluate the **performance** of the Masked Language Models (MLMs) using the Fill-Mask evaluation task and our [Masked Arab States Dataset (MASD)](https://github.com/SaiedAlshahrani/performance-implications/tree/main/Language-Modeling-Evals/MASD) dataset. To measure the **impact of template-based translation**, we compare the performance of MLMs trained on the Egyptian Arabic Wikipedia edition’s corpora, which are dominated by template-based translation, to the performance of MLMs trained on Modern Standard Arabic and Moroccan Arabic Wikipedia editions’ corpora, which are not. On the other hand, to measure the **impact of bot-based generation**, we compare the performance of MLMs trained on Arabic and Moroccan Arabic corpora (with and without bot-generated articles) using the Fill-Mask task and our [MASD](https://github.com/SaiedAlshahrani/performance-implications/tree/main/Language-Modeling-Evals/MASD) dataset. *Please read the paper for more details about the evaluation process.*


### Masked Language Models (MLMs):
We have trained **5 RoBERTa** MLMs for this experiment, and due to the huge size of these models, we could **not** share them with the community. However, we have hosted them on the Hugging Face Hub. See the Table below for the details. We also evaluate these MLMs using the *Pseudo-Perplexity* metric and share the evaluation process and results here at [Pseudo-Perplexity-Evals](https://github.com/SaiedAlshahrani/performance-implications/tree/main/Language-Modeling-Evals/Pseudo-Perplexity-Evals).

| Wikipedia Edition     | Dump File Date | Hugging Face Link |
| :----: | :----: |:----: |
| Modern Standard Arabic Wikipedia (AR)| 01-01-2023 | [SaiedAlshahrani/Arabic\_Wikipedia\_20230101\_bots](https://huggingface.co/datasets/SaiedAlshahrani/Arabic_Wikipedia_20230101_bots)|
| Modern Standard Arabic Wikipedia (AR)| 01-01-2023 | [SaiedAlshahrani/Arabic\_Wikipedia\_20230101\_nobots](https://huggingface.co/datasets/SaiedAlshahrani/Arabic_Wikipedia_20230101_nobots)|
| Egyptian Arabic Wikipedia (ARZ)| 01-01-2023 | [SaiedAlshahrani/Egyptian\_Arabic\_Wikipedia\_20230101](https://huggingface.co/datasets/SaiedAlshahrani/Egyptian_Arabic_Wikipedia_20230101)|
| Moroccan Arabic Wikipedia (ARY)| 01-01-2023 | [SaiedAlshahrani/Moroccan\_Arabic\_Wikipedia\_20230101\_bots](https://huggingface.co/datasets/SaiedAlshahrani/Moroccan_Arabic_Wikipedia_20230101_bots)|
| Moroccan Arabic Wikipedia (ARY)| 01-01-2023 | [SaiedAlshahrani/Moroccan\_Arabic\_Wikipedia\_20230101\_nobots](https://huggingface.co/datasets/SaiedAlshahrani/Moroccan_Arabic_Wikipedia_20230101_nobots)|

 
### Evaluation Pipeline:
We share our **evaluation pipeline** of the Language Modeling upstream task, including the implementation of the Fill-Mask evaluation task process and the generic search algorithm that takes any Arabic word and then searches for all its possible Arabic variants (*only* Alefs, Alef Maksura, and Teh Marbuta variants). All are available at [mlm_utils.py](https://github.com/SaiedAlshahrani/performance-implications/blob/main/Language-Modeling-Evals/mlm_utils.py). We also share the Word Representation evaluations of our WEMs here at [Language-Modeling-Task.ipynb](https://github.com/SaiedAlshahrani/performance-implications/blob/main/Language-Modeling-Evals/Language-Modeling-Task.ipynb).