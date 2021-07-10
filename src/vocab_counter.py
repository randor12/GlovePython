import numpy as np
import pandas as pd

def get_vocab_counts(lst: pd.Series):
    
    wrd_counts = {}
    # loop through all the phrases
    for i in lst:
        phrase = str(i)
        
        for j in phrase.split():
            # loop through each word in the phrase
            
            # get the value counts 
            if j in wrd_counts.keys():
                wrd_counts[j] += 1
            else:
                wrd_counts[j] = 1
                
    return wrd_counts