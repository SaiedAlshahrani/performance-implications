import re
import os, sys
import datasets
import numpy as np
import pandas as pd
import getopt, torch
import logging, warnings
from datasets import load_dataset
from transformers import pipeline
from transformers import logging as hflogging
from huggingface_hub.utils import disable_progress_bars
from transformers import AutoModelForMaskedLM, AutoTokenizer

# disable_progress_bars()
logging.disable(logging.INFO)
datasets.disable_progress_bar()
# hflogging.set_verbosity_error()
logging.disable(logging.WARNING)

os.environ['TOKENIZERS_PARALLELISM'] = 'true'
# datasets.logging.set_verbosity(datasets.logging.INFO)
warnings.simplefilter(action='ignore', category=UserWarning)
warnings.simplefilter(action='ignore', category=FutureWarning)



def load_checkpoint(checkpoint):
    model = AutoModelForMaskedLM.from_pretrained(checkpoint)
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    return model, tokenizer



def remove_noise(text):
    text = text.replace('\n','')
    text = re.sub('\s+', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = re.sub("\d+", " ", text)
    text =re.sub(r'[a-zA-Z?]', '', text).strip()
    return text



def character_length(sample):
    words = sample.split()
    character_length = sum(len(word) for word in words)
    return character_length



def select_samples(dataset, min_length, max_length):
    dataframe = pd.read_csv(dataset)
    dataframe=dataframe.dropna()
    selected_examples = []

    for i in range(dataframe.shape[0]):
        if character_length(dataframe.iloc[i][0]) >= min_length and \
        character_length(dataframe.iloc[i][0]) <= max_length:
            selected_examples.append(remove_noise(dataframe.iloc[i][0]))

    new_dataframe = pd.DataFrame(selected_examples, columns=['text'])
    new_dataset = f"{dataset.split('.')[0]}_Selected_Samples.csv"
    new_dataframe.to_csv(new_dataset, encoding='utf-8', index=False)
    return new_dataset



def load_samples(new_dataset, seed, number_samples):
    dataset = load_dataset('csv', data_files=new_dataset, split='train')
    samples = dataset.shuffle(seed=seed).select(range(number_samples))
    return samples



def get_perplexity(text, model, tokenizer):
    tensor_input = tokenizer.encode(text, truncation=True, padding=True, max_length=512, return_tensors='pt')
    repeat_input = tensor_input.repeat(tensor_input.size(-1)-2, 1)
    mask = torch.ones(tensor_input.size(-1) -1).diag(1)[:-2]
    masked_input = repeat_input.masked_fill(mask == 1, tokenizer.mask_token_id)
    labels = repeat_input.masked_fill(masked_input != tokenizer.mask_token_id, -100)
    with torch.inference_mode():
        loss = model(masked_input, labels=labels).loss
    return np.exp(loss.item())



def compute_perplexity(dataset, samples, number_samples):
    dataframe = pd.DataFrame(columns=['text','length','perplexity'])

    print(f"\033[1m \n# Calculating Pseudo-Perplexity of `{dataset}` in Progress ... \033[0m")

    for i in range(0, len(samples['text'])):
        try:
            ppl = get_perplexity(text=samples['text'][i], model=model, tokenizer=tokenizer)
            new_row = {'text':samples['text'][i], 'length':len(samples['text'][i]), 'perplexity':ppl}
            dataframe = dataframe.append(new_row, ignore_index=True)

        except:
            pass

    filename = f"PPerplexity_{dataset.split('.')[0]}_{number_samples}_Samples.csv"
    dataframe.to_csv(filename, encoding='utf-8', index=False)

    ppl_mean = dataframe['perplexity'].mean()
    print(f"\033[1m  \n# Mean Pseudo-Perplexity of `{number_samples}` Randomly Selected Samples from `{dataset}` ==\033[1m", '{0:,.2f}'.format(ppl_mean))
    print(f"  > The Calculations of Pseudo-Perplexity Exported to `{filename}`.\n")



def main(argv):
    seed = ''
    dataset = ''
    nsamples = ''
    checkpoint = ''

    opts, args = getopt.getopt(argv,"hc:d:s:n:i:x:",["checkpoint=","dataset=","seed=","nsamples=", "min=", "max="])

    for opt, arg in opts:
        if opt == '-h':
            print('# Correct Usage: python pseudo_ppls.py -c <checkpoint> -d <dataset> -s <seed> -n <nsamples> -i <min_length> -x <max_length>')
            print('  > Detailed Arguments:')
            print('    -c/--checkpoint: Hugging Face Checkpoint/Model')
            print('    -d/--dataset: Local Dataset File in CSV Format')
            print('    -s/--seed: Positive Random Number Generator Value')
            print('    -n/--nsamples: Number of Randomly Selected Samples')
            print('    -i/--min: Minimum Character Length of Selected Samples')
            print('    -x/--man: Maximum Character Length of Selected Samples')
            sys.exit()
        elif opt in ("-c", "--checkpoint"):
            checkpoint = arg
        elif opt in ("-d", "--dataset"):
            dataset = arg
        elif opt in ("-s", "--seed"):
            seed = arg
        elif opt in ("-n", "--nsamples"):
            nsamples = arg
        elif opt in ("-i", "--min"):
            min = arg
        elif opt in ("-x", "--max"):
            max = arg

    return checkpoint, dataset, int(seed), int(nsamples), int(min), int(max)



if __name__ == "__main__":
    try:
        checkpoint, dataset, seed, nsamples, min, max = main(sys.argv[1:])
        model, tokenizer = load_checkpoint(checkpoint)
        new_dataset = select_samples(dataset, min, max)
        samples = load_samples(new_dataset, seed, nsamples)    
        compute_perplexity(dataset, samples, nsamples)

    except ValueError:
        print('# Correct Usage: python pseudo_ppls.py -c <checkpoint> -d <dataset> -s <seed> -n <nsamples> -i <min_length> -x <max_length>')
        print('  > Detailed Arguments:')
        print('    -c/--checkpoint: Hugging Face Checkpoint/Model')
        print('    -d/--dataset: Local Dataset File in CSV Format')
        print('    -s/--seed: Positive Random Number Generator Value')
        print('    -n/--nsamples: Number of Randomly Selected Samples')
        print('    -i/--min: Minimum Character Length of Selected Samples')
        print('    -x/--man: Maximum Character Length of Selected Samples')
        sys.exit()
