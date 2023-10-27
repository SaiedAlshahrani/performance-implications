# Arab States Analogy Dataset (ASAD)
We share our Arab States Analogy Dataset (ASAD), which consists of *four* sets: country-capital set, country-currency set, country-nationality set, and country-continent set. Each set has **380** word analogies, and the ASAD dataset's total number of word analogies is **1520**. *Please read the paper for more details about the ASAD dataset*. 

The ASAD dataset consists of *five* text files, one for each set mentioned above and one text file for all the sets combined. You can load the ASAD dataset using `Pandas` Python library directly or load the hosted version of the ASAD dataset on the Hugging Face Hub at [SaiedAlshahrani/ASAD](https://huggingface.co/datasets/SaiedAlshahrani/ASAD).

#### To directly load the ASAD dataset using `Pandas` Python library, use the following code snippet:

```Python
import pandas as pd
asad_dataset = pd.read_csv("Arab_States_Analogy_Dataset_All.txt", sep=" ", header=None)
asad_dataset.columns = ["example1", "example2", "query", "answer"]
```

#### To load the ASAD dataset from the Hugging Face Hub, use the following code snippet:

```Python
from datasets import load_dataset
asad_dataset = load_dataset("SaiedAlshahrani/ASAD")
```