import json
import pandas as pd
import os, logging, warnings
from transformers import pipeline
from transformers import AutoConfig
from transformers import logging as hflogging
from huggingface_hub.utils import disable_progress_bars


disable_progress_bars()
hflogging.set_verbosity_error()
logging.disable(logging.WARNING)
os.environ['TOKENIZERS_PARALLELISM'] = 'False'
warnings.simplefilter(action='ignore', category=UserWarning)
warnings.simplefilter(action='ignore', category=FutureWarning)



def get_model_config(model):

    model_config = AutoConfig.from_pretrained(model)
    
    class GetRobertaConfig:
        def __getitem__(self, configs):
            return f"{configs}"
            
    config = GetRobertaConfig()
    return json.loads(config[model_config][14:])
    


def search_variants(masked_token):
    variants = []
    
    teh_marbuta = ['\u0629', '\u0647']
    alef_maksura = ['\u0649', '\u064a']
    alefs = ['\u0625','\u0623','\u0671','\u0622','\u0627']
    
    if masked_token[-1] in teh_marbuta:
        for teh in teh_marbuta:
            variants.append(masked_token.replace(masked_token[:-1]+masked_token[-1], masked_token[:-1]+teh))
    elif masked_token[-1] in alef_maksura:
        for alefm in alef_maksura:
            variants.append(masked_token.replace(masked_token[:-1]+masked_token[-1], masked_token[:-1]+alefm))
    elif masked_token[0] in alefs:
        for alef in alefs:
            variants.append(masked_token.replace(masked_token[0]+masked_token[1:], alef+masked_token[1:]))
    else:
        return None
    


def mask_filler(prompt, model, top_k):
    results_strs = []
    fill = pipeline('fill-mask', model=model, top_k=top_k)
    results = fill(prompt)

    for result in results:
        variants = search_variants(result['token_str'])
        
        if variants != None:
            for variant in variants:
                if variant not in results_strs:
                    results_strs.append(variant)
                    
        results_strs.append(result['token_str'])

    results_strs = [result.strip(' ') for result in list(set(results_strs))]
    results_strs = [result for result in results_strs if result]
    return results_strs
