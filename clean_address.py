import re
import unicodedata
import pandas as pd

class CleanAddress:
    COMMON_ABBREVIATIONS = {
        r"\bst\b": "street",
        r"\brd\b": "road",
        r"\bave\b": "avenue",
        r"\bav\b": "avenue",
        r"\bblvd\b": "boulevard",
        r"\bdr\b": "drive",
        r"\bln\b": "lane",
        r"\bhwy\b": "highway",
        r"\bapt\b": "apartment",
        r"\bfl\b": "floor",
        r"\bno\b": "number",
    }
    address = ""
    def __init__(self, address):
        self.address = address
        pass

    def clean_address(self) -> str:
        if pd.isna(self.address):
            return ""
        # Unicode normalization
        self.address = unicodedata.normalize('NFKD', self.address).encode('ascii', 'ignore').decode()
        # Lowercase
        self.address = self.address.lower()
        # Expand abbreviations
        for pattern, replacement in self.COMMON_ABBREVIATIONS.items():
            self.address = re.sub(pattern, replacement, self.address)
        # Remove all non-alphanumeric and non-space characters
        self.address = re.sub(r"[^a-z0-9\s]", " ", self.address)
        # Collapse multiple spaces
        self.address = re.sub(r"\s+", " ", self.address).strip()
        return self.address

# print(CleanAddress("S/O SHIVAMURATAYYA A/P CHIKBAGEWADI TQ BAILHONGAL BELGAUM BELGAUM KARNATAKA").clean_address())  # Example usage