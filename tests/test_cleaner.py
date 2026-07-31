from parsers.text_cleaner import TextCleaner

sample = """
SKILLS


Python      Java

Machine Learning



EDUCATION
"""

print(TextCleaner.clean(sample))