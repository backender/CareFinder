#%% Building corpus
import pandas as pd
import wikipedia
import re
import nltk
from nltk.tokenize import word_tokenize


meta = pd.read_excel("meta.xlsx")
for spec in meta.Specialization:
    print (spec)
    page = wikipedia.page(spec)
    file = open(spec+'.txt','w') 
    file.write(re.sub("[^a-zA-Z]", " ", page.title)) 
    file.write(re.sub("[^a-zA-Z]", " ", page.content)) 
    file = open(spec+'_links.txt','w')
    file = open(spec+'_furtherLinks.txt','w')
    for link in page.links:
        try:
            file = open(spec+'_links.txt','a')
            linkPage=wikipedia.page(link)
            file.write(re.sub("[^a-zA-Z]", " ", linkPage.title))
            file.write(re.sub("[^a-zA-Z]", " ", linkPage.summary)) 
            file = open(spec+'_furtherLinks.txt','a')
            for linkFurther in linkPage.links:
                file.write(re.sub("[^a-zA-Z]", " ", linkFurther))
        except wikipedia.PageError:
            continue
        except wikipedia.DisambiguationError:
            continue
    
