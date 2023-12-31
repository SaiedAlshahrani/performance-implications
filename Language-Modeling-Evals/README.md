# Language Modeling Evaluations

We evaluate the **performance** of the Masked Language Models (MLMs) using the Fill-Mask evaluation task and our [Masked Arab States Dataset (MASD)](https://github.com/SaiedAlshahrani/performance-implications/tree/main/Language-Modeling-Evals/MASD) dataset. To measure the **impact of template-based translation**, we compare the performance of MLMs trained on the Egyptian Arabic Wikipedia edition’s corpora, which are dominated by template-based translation, to the performance of MLMs trained on Modern Standard Arabic and Moroccan Arabic Wikipedia editions’ corpora, which are not. On the other hand, to measure the **impact of bot-based generation**, we compare the performance of MLMs trained on Modern Standard Arabic and Moroccan Arabic Wikipedia editions’ corpora (with and without bot-generated articles) using the Fill-Mask task and our [MASD](https://github.com/SaiedAlshahrani/performance-implications/tree/main/Language-Modeling-Evals/MASD) dataset. *Please read the paper for more details about the evaluation process.*


### Masked Language Models (MLMs):
We have trained **5 RoBERTa<sub>BASE</sub>** MLMs for this experiment, and due to the huge size of these models, we could **not** share them with the community. However, we share our training scripts here at [MLMs-Training-Scripts](https://github.com/SaiedAlshahrani/performance-implications/tree/main/Language-Modeling-Evals/MLMs-Training-Scripts) for these models and provide detailed documentation on the creation of Wikipedia corpora that can be found here at [Wikipedia-Corpora-Creation](https://github.com/SaiedAlshahrani/performance-implications/tree/main/Wikipedia-Corpora-Creation).

We have hosted them on the Hugging Face Hub (see the Table below for the details). We also evaluate these MLMs using the *Pseudo-Perplexity* metric and share the evaluation process and results here at [Pseudo-Perplexity-Evals](https://github.com/SaiedAlshahrani/performance-implications/tree/main/Language-Modeling-Evals/Pseudo-Perplexity-Evals).

| Wikipedia Edition     | Model Name | Hugging Face Link |
| :----: | :----: |:----: |
| Modern Standard Arabic Wikipedia (AR)| arRoBERTa<sub>BASE</sub> | [SaiedAlshahrani/arwiki\_20230101\_roberta\_mlm\_bots](https://huggingface.co/SaiedAlshahrani/arwiki_20230101_roberta_mlm_bots)|
| Modern Standard Arabic Wikipedia (AR)| arRoBERTa<sub>BASE</sub> | [SaiedAlshahrani/arwiki\_20230101\_roberta\_mlm\_nobots](https://huggingface.co/SaiedAlshahrani/arwiki_20230101_roberta_mlm_nobots)|
| Egyptian Arabic Wikipedia (ARZ)| arzRoBERTa<sub>BASE</sub> | [SaiedAlshahrani/arzwiki\_20230101\_roberta\_mlm](https://huggingface.co/SaiedAlshahrani/arzwiki_20230101_roberta_mlm)|
| Moroccan Arabic Wikipedia (ARY)| aryRoBERTa<sub>BASE</sub> | [SaiedAlshahrani/arywiki\_20230101\_roberta\_mlm\_bots](https://huggingface.co/SaiedAlshahrani/arywiki_20230101_roberta_mlm_bots)|
| Moroccan Arabic Wikipedia (ARY)| aryRoBERTa<sub>BASE</sub> | [SaiedAlshahrani/arywiki\_20230101\_roberta\_mlm\_nobots](https://huggingface.co/SaiedAlshahrani/arywiki_20230101_roberta_mlm_nobots)|

 
### Evaluation Pipeline:
We share our **evaluation pipeline** of the Language Modeling upstream task, including the implementation of the Fill-Mask evaluation task process and the generic search algorithm that takes any Arabic word and then searches for all its possible Arabic variants (*only* Alefs, Alef Maksura, and Teh Marbuta variants). All are available at [mlm_utils.py](https://github.com/SaiedAlshahrani/performance-implications/blob/main/Language-Modeling-Evals/mlm_utils.py). We also share the Language Modeling evaluations of our MLMs here at [Language-Modeling-Task.ipynb](https://github.com/SaiedAlshahrani/performance-implications/blob/main/Language-Modeling-Evals/Language-Modeling-Task.ipynb).