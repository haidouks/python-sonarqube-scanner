import re
import os

class search():
    """
    docstring
    HELPER FOR SEARCH OPERATOPNS
    """
    @staticmethod
    def search_content( file_filter_regex, keyword_regex, folder_path="./"):
        exists = False
        matching_files = []
        # Klasör içinde dolaş
        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                # Dosya adı regex deseni ile eşleşiyorsa
                if re.match(file_filter_regex, file_name):
                    file_path = os.path.join(root, file_name)
                    # Dosya içinde dolaş
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                        for line_number, line in enumerate(file, start=1):
                            # Anahtar kelimeyi içeren satırı bul
                            if re.match(keyword_regex, line):
                                matching_files.append({
                                    'file_name': file_name,
                                    'matched_line': line.strip()
                                })
                                exists = True
        return {"exists": exists, "results": matching_files}
