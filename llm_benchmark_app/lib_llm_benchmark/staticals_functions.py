from types import SimpleNamespace
import re
import pandas as pd
import textstat
import langdetect
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob

def stopwords_count(text):
    """
    The function `stopwords_count` calculates the number of stopwords in a given text in Spanish.
    
    :param text: The function `stopwords_count` takes a text input and counts the number of stopwords
    (common words that are often filtered out before or after processing of text) in the text
    :return: The function `stopwords_count` returns the number of stopwords present in the input text.
    """

    nltk.download('stopwords', quiet=True)
    stopwords_es = set(stopwords.words('spanish'))
    words = text.lower().split()
    num_stopwords = sum(1 for word in words if word in stopwords_es)
    return num_stopwords


def calc_lexical_diversity(text):
    """
    The function `calc_lexical_diversity` calculates the lexical richness and diversity of a given text
    by removing punctuation marks, splitting the text into words, and then computing the ratio of unique
    words to total words.
    
    :param text: It looks like you have provided a code snippet for calculating the lexical diversity of
    a given text. However, you have not provided the actual text input for which you want to calculate
    the lexical diversity
    :return: A SimpleNamespace object containing the calculated lexical richness and lexical diversity
    values.
    """

    punctuation_pattern = r"[,.;:!()?\-–…“”‘’]+"
    text_whitout_puntuacion = re.sub(punctuation_pattern, "", text.lower())
    words = text_whitout_puntuacion.split()
    vocabulary = set(words)
    lexical_richness = len(vocabulary) / len(words)
    lexical_diversity = (len(vocabulary) / len(words)) * 100
    dict = {
            "lexical_richness": lexical_richness,
            "lexical_diversity": lexical_diversity
            }
    ns = SimpleNamespace(**dict)
    return ns


def analyze_sentiment(text):
    """
    The `analyze_sentiment` function uses TextBlob to analyze the sentiment of a given text and returns
    whether it is positive, neutral, or negative.
    
    :param text: The code you provided is a simple sentiment analysis function using TextBlob library in
    Python. It analyzes the sentiment of the input text and returns 'Positive' if the sentiment polarity
    is greater than 0, 'Neutral' if it is 0, and 'Negative' if it is less than 0
    :return: The function `analyze_sentiment(text)` returns a sentiment analysis result based on the
    polarity of the text. It returns 'Positive' if the polarity is greater than 0, 'Neutral' if the
    polarity is 0, and 'Negative' if the polarity is less than 0.
    """
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'
    

def get_df_linguistics_statistics_values(df_prompts, name_tbl):
    """
    The function `get_df_linguistics_statistics_values` processes a DataFrame of prompts, extracting
    linguistic statistics and sentiment analysis for each answer.
    
    :param df_prompts: The function `get_df_linguistics_statistics_values` takes two parameters:
    :param name_tbl: The `name_tbl` parameter is a string that represents the name of a table or model.
    In the provided code snippet, it is used to extract the name of the LLM model by splitting the
    string at underscores and taking the first part
    :return: The function `get_df_linguistics_statistics_values` returns the DataFrame `df_prompts`
    after adding several columns with linguistic statistics values calculated from the text in the
    'answers' column.
    """
 
    # llm_model name
    df_prompts['llm_model'] = name_tbl.split('_')[0] 
    # detect lang
    df_prompts['lang'] = df_prompts['answers'].apply(lambda x: langdetect.detect(x)) 
    #  reading time
    df_prompts['reading_time'] = df_prompts['answers'].apply(lambda x: textstat.reading_time(x))
    # Aggregates and Averages
    #Sentence Count: Returns the number of sentences present in the given text.
    df_prompts['sentence_count']=df_prompts['answers'].apply(lambda x: textstat.sentence_count(x))
    #Character Count: Returns the number of characters present in the given text. la puntuacion incluida
    df_prompts['char_count']=df_prompts['answers'].apply(lambda x: textstat.char_count(x))
    #Letter Count: Returns the number of characters present in the given text without punctuation.
    df_prompts['letter_count']=df_prompts['answers'].apply(lambda x: textstat.letter_count(x))
    #Syllable Count: Returns the number of syllables present in the given text
    df_prompts['lexicon_count']=df_prompts['answers'].apply(lambda x: textstat.lexicon_count(x))
    #avg_sentence_length: Returns the average lenght of sentence in the given text
    df_prompts['avg_sentence_length']=df_prompts['answers'].apply(lambda x: textstat.avg_sentence_length(x))
    #avg_letter_per_word:  Returns the average numeber o letters per word in the given text
    df_prompts['avg_letter_per_word']=df_prompts['answers'].apply(lambda x: textstat.avg_letter_per_word(x))
    # stop words function
    df_prompts['qtty_stopwords']=df_prompts['answers'].apply(stopwords_count)
    #qtty_words
    df_prompts['qtty_words']=df_prompts['answers'].apply(lambda x: len(x.split()))
    #lexical_density
    df_prompts['lexical_density']=df_prompts['answers'].apply(lambda x: calc_lexical_diversity(x).lexical_diversity)
    #lexical_richness
    df_prompts['lexical_richness']=df_prompts['answers'].apply(lambda x: calc_lexical_diversity(x).lexical_richness)
    #analyze_sentiment
    df_prompts['analyze_sentiment']=df_prompts['answers'].apply(analyze_sentiment)

    return df_prompts