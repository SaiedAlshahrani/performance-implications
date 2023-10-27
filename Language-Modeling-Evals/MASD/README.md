# Masked Arab States Dataset (MASD)

We share our Masked Arab States Dataset (MASD), which consists of *four* categories: country-capital
prompts, country-currency prompts, country-nationality prompts, and country-continent prompts. Each prompts category has **40** masked prompts, and the total number of masked prompts in the MASD dataset is **160**. *Please read the paper for more details about the MASD dataset*. 

The MASD dataset consists of *five* CSV files, one for each category mentioned above and one CSV file for all the categories combined. You can load the MASD dataset using `Pandas` Python library directly or load the hosted version of the MASD dataset on the Hugging Face Hub at [SaiedAlshahrani/MASD](https://huggingface.co/datasets/SaiedAlshahrani/MASD).

#### To directly load the MASD dataset using `Pandas` Python library, use the following code snippet:

```Python
import pandas as pd
masd_dataset = pd.read_csv("Masked_Arab_States_Dataset_All.csv")

```

#### To load the MASD dataset from the Hugging Face Hub, use the following code snippet:

```Python
from datasets import load_dataset
masd_dataset = load_dataset("SaiedAlshahrani/MASD")
```