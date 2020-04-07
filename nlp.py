import pandas as pd
news= pd.read_csv('data/abcnews-date-text.csv',nrows=10000)
def plot_character_length_histogram(text):
    text.str.len().\
        hist()
plot_character_length_histogram(news['headline_text'])
