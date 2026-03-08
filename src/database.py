import json
import os

class DBHandler:
    def __init__(self, lang="laravel-react"):
        self.base_path = f"data/{lang}"
        self.stats_path = "storage/user_stats.json"

    def get_all_master_data(self):
        all_snippets = []
        if not os.path.exists(self.base_path):
            return []

        for root, dirs, files in os.walk(self.base_path):
            if "data_kode.json" in files:
                # Ambil nama folder terakhir sebagai kategori
                category_name = os.path.basename(root) 
                
                path = os.path.join(root, "data_kode.json")
                with open(path, 'r') as f:
                    snippets = json.load(f)
                    
                    # Suntikkan nama folder ke dalam data
                    for s in snippets:
                        s['category'] = category_name # Menambahkan field 'category'
                    
                    all_snippets.extend(snippets)
        return all_snippets

    def get_stats(self):
        if not os.path.exists(self.stats_path):
            return {}
        with open(self.stats_path, 'r') as f:
            return json.load(f)

    def save_stats(self, stats):
        os.makedirs("storage", exist_ok=True)
        with open(self.stats_path, 'w') as f:
            json.dump(stats, f, indent=4)