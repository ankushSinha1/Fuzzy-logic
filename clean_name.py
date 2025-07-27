import re
import unicodedata
import pandas as pd

class CleanName:
    COMMON_TITLES = {
        "mr", "mrs", "ms", "dr", "prof", "shri", "smt", "miss", "sir", "madam"
    }
    
    name = ""
    
    def __init__(self, name):
        self.name = name

    def clean_name(self) -> str:
        if pd.isna(self.name):
            return ""
        # Unicode normalization
        self.name = unicodedata.normalize('NFKD', self.name).encode('ascii', 'ignore').decode()
        # Lowercase
        self.name = self.name.lower()
        # Remove punctuation and special characters
        self.name = re.sub(r"[^a-z0-9\s]", "", self.name)
        # Tokenize
        tokens = self.name.split()
        tokens = [tok for tok in tokens if tok not in self.COMMON_TITLES]
        # Collapse multiple spaces and join
        cleaned_name = " ".join(tokens)
        return cleaned_name.strip()

# print(CleanName("Neetu Singh Wo Suresh Chandra").clean_name())  # Example usage