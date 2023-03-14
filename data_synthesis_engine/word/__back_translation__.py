# from translate import Translator
from deep_translator import GoogleTranslator

# def back_translate(text, target_language, source_language='en'):
#     """
#     Translates the given text from the target language to the source language and back to the target language, resulting in
#     a 'back translated' version of the original text.
#     :param text: The text to back translate.
#     :param target_language: The target language for the back translation.
#     :param source_language: The source language for the back translation. Default is 'en' (English).
#     :return: The 'back translated' version of the original text.
#     """



def back_translater(sentence):


    en_hi = GoogleTranslator(source='en', target='hi').translate(sentence)  # output -> Weiter so, du bist großartig
    hi_en = GoogleTranslator(source='hi', target='en').translate(en_hi)  # output -> Weiter so, du bist großartig
    
    en_de = GoogleTranslator(source='en', target='de').translate(sentence)  # output -> Weiter so, du bist großartig
    de_en = GoogleTranslator(source='de', target='en').translate(en_de)  # output -> Weiter so, du bist großartig
    
    en_ja = GoogleTranslator(source='en', target='ja').translate(sentence)  # output -> Weiter so, du bist großartig
    ja_en = GoogleTranslator(source='ja', target='en').translate(en_ja)  # output -> Weiter so, du bist großartig
    
    en_fr = GoogleTranslator(source='en', target='fr').translate(sentence)  # output -> Weiter so, du bist großartig
    fr_en = GoogleTranslator(source='fr', target='en').translate(en_fr)  # output -> Weiter so, du bist großartig
    
    return hi_en, de_en, ja_en, fr_en


