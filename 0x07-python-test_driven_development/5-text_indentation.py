#!/usr/bin/python3
def text_indentation(text):
    """text indetation by replacing characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    print("\n".join(
        [currentLine.strip() for currentLine in text.split("\n")]), end="")
