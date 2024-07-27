import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


def download_nltk_pkg(package):
    """
    The function `download_nltk_pkg` downloads specific NLTK packages such as stopwords, punkt, and
    averaged_perceptron_tagger.
    
    :param package: The `package` parameter in the `download_nltk_pkg` function is a placeholder for the
    name of the NLTK package that you want to download. You can pass the name of the specific NLTK
    package as an argument when calling this function to download that package
    """
    # stopwords = descarga el conjunto de palabras vacías (stopwords)
    # punkt,averaged_perceptron_tagger = descarga el tokenizador de palabras y frases.
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    #nltk.download(package)

def limpio_signos_puntuacion(texto, idioma = 'en'):
    """
    The function `limpio_signos_puntuacion_es` removes punctuation marks from a given text in either
    English or Spanish.

    :param texto: The function `limpio_signos_puntuacion_es` is designed to remove punctuation marks
    from a given text based on the specified language. However, there are a couple of issues in the code
    that need to be corrected:
    :param idioma: The function `limpio_signos_puntuacion_es` takes two parameters: `texto` which is the
    input text to be processed, and `idioma` which specifies the language of the text for punctuation
    removal (default is 'en' for English), defaults to en (optional)
    :return: The function `limpio_signos_puntuacion_es` returns the input text without any punctuation
    marks based on the specified language (either English or Spanish).
    """
    # Tokenizo el texto ingresado
    palabras = word_tokenize(texto)

    if idioma == 'es':
        # defino un string con los signos de puntuacion en español, mas el salto de linea
        puntuacion_espanol = "¡!\"#$%&'()*+,-./:;<=>¿?@[\\]^_`{|}~«»\n" #"¡!\"#$%&'()*+,-./:;<=>¿?@[\\]^_`{|}~«»\n"
        palabras_sin_puntuacion_espanol = [palabra for palabra in texto if palabra not in puntuacion_espanol]
        texto_sin_puntuacion_es = ''.join(palabras_sin_puntuacion_espanol)
        texto_sin_puntuacion = texto_sin_puntuacion_es
    elif idioma == 'en':
        # importo de la libreria string la funcion punctuation, que lista los signos de puntuacion en ingles
        from string import punctuation
        palabras_sin_puntuacion_english = [palabra for palabra in texto if palabra not in punctuation]
        texto_sin_puntuacion_en = ''.join(palabras_sin_puntuacion_english)
        texto_sin_puntuacion = texto_sin_puntuacion_en

    return texto_sin_puntuacion



def delete_stopwords_nltk(texto, lang='english'):
    """
    The function `delete_stopwords` removes common Spanish stopwords from a given text.

    :param texto: The function `delete_stopwords` takes a text input and removes common stopwords in
    Spanish using NLTK library. It tokenizes the text, converts it to lowercase, and then removes any
    stopwords present in the text. The cleaned text without stopwords is then returned
    :return: The function `delete_stopwords` returns the input text with common Spanish stopwords
    removed.
    """
    # Defino que las StopWords son del idioma Español
    nltk_stopwords_es = nltk.corpus.stopwords.words(lang)
    # Elimino las palabras vacias mas comunes(stopwords)
    clean_texto_nltk = ' '.join([palabra for palabra in nltk.tokenize.word_tokenize(texto) if not palabra in nltk_stopwords_es])
    return clean_texto_nltk


def avg_palabras_resenia(frase):
    """
    This Python function calculates the average length of words in a given sentence.

    :param frase: The function `avg_palabras_resenia` calculates the average length of words in a given
    sentence or phrase. It splits the input `frase` into individual words, calculates the length of each
    word, and then computes the average length of all words in the phrase
    :return: The function `avg_palabras_resenia` returns the average length of words in the input
    sentence `frase`.
    """
    palabras = frase.split()
    avg_palabras = round(sum(len(palabra) for palabra in palabras) / len(palabras),3)
    return avg_palabras


def promedio_longitud_oraciones(texto):
    """
    This Python function calculates the average length of sentences in a given text.

    :param texto: The function `promedio_longitud_oraciones` calculates the average length of sentences
    in a given text. It first splits the text into sentences using the period ('.') as the delimiter.
    Then, it calculates the total length of words in all sentences and the total number of sentences.
    Finally, it returns
    :return: The function `promedio_longitud_oraciones` calculates and returns the average length of
    sentences in the input text.
    """
    oraciones = texto.split('.')
    longitud_total = sum(len(oracion.split()) for oracion in oraciones if oracion)
    cantidad_oraciones = len([oracion for oracion in oraciones if oracion])
    return round(longitud_total / cantidad_oraciones, 2) if cantidad_oraciones > 0 else 0