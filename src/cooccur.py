import pandas as pd

def get_TF(lst: pd.Series):
    bag = list(map(lambda x: str(x).split(), lst))
    
    TF = pd.Series(bag).apply(lambda x: pd.Series(x).value_counts())
    
    TF_ordered = TF.sort_index(axis=1)
    
    return TF_ordered
    

def get_cooccur(lst: pd.Series):
    TF = get_TF(lst)
    TF = TF.fillna(0)
    cooccurr = TF.transpose().dot(TF)
    
    return cooccurr