import warnings
from gensim.models import Word2Vec
warnings.simplefilter("ignore", UserWarning)
warnings.simplefilter("ignore", FutureWarning)
from gensim.models.keyedvectors import KeyedVectors


def load_model(model, model_format='word2vec'):
    if model_format=='glove':
        model = KeyedVectors.load_word2vec_format(model, binary=False, no_header=True)
        return model
    else:
        model = KeyedVectors.load(model)
        return model


def get_analogy(example, query, model, model_format='word2vec', top_k=1):
    try:
        answers = []
        word_positive = [query, example[1]]
        word_negative = [example[0]]
        
        if model_format=='glove': 
            analogies = model.most_similar(positive=word_positive, negative=word_negative, topn=top_k)
        else: 
            analogies = model.wv.most_similar(positive=word_positive, negative=word_negative, topn=top_k)
        
        for analogy in analogies:
            variants = search_variants(analogy[0])
            if variants != None:
                for variant in variants:
                    if variant not in answers:
                        answers.append(variant)
            answers.append(analogy[0])
        return answers
    
    except KeyError:
        return 'OOV'

    
def get_analogy_by_row(row, model, model_format='word2vec', top_k=1):
    example = [row['example1'], row['example2']]
    query = row['query']
    if model_format=='glove': 
        pred_answer = get_analogy(example, query, model, model_format='glove', top_k=top_k)
    else:
        pred_answer = get_analogy(example, query, model, top_k=top_k)
    return(pred_answer)


def search_variants(answer):
    variants = []
    
    teh_marbuta = ['\u0629', '\u0647']
    alef_maksura = ['\u0649', '\u064a']
    alefs = ['\u0625','\u0623','\u0671','\u0622','\u0627']
    
    if answer[-1] in teh_marbuta:
        for teh in teh_marbuta:
            variants.append(answer.replace(answer[:-1]+answer[-1], answer[:-1]+teh))
    elif answer[-1] in alef_maksura:
        for alefm in alef_maksura:
            variants.append(answer.replace(answer[:-1]+answer[-1], answer[:-1]+alefm))
    elif answer[0] in alefs:
        for alef in alefs:
            variants.append(answer.replace(answer[0]+answer[1:], alef+answer[1:]))
    else:
        return None
    
    return variants