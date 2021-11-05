def alphabetical(sentence: str) -> str:
    words = sentence.split()
    words.sort() 
    return " ".join(words)
