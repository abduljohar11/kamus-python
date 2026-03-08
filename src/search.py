class SearchEngine:
    @staticmethod
    def search(query, all_master, stats):
        # 1. Pecah query menjadi tokens (kata-kata terpisah)
        # Contoh: "migration delete" -> ["migration", "delete"]
        keywords = query.lower().strip().split()
        if not keywords:
            return []
            
        matched = []
        
        for item in all_master:
            s_id = item['id']
            # Ambil data personal dari storage
            meta = stats.get(s_id, {"hits": 0, "is_favorite": False, "custom_tags": []})
            
            # --- Persiapkan Data untuk Dicek ---
            title = item.get('title', '').lower()
            desc = item.get('description', '').lower()
            code = item.get('code', '').lower()
            folder_cat = item.get('category', '').lower()
            inner_cats = [c.lower() for c in item.get('categories', [])]
            user_tags = [t.lower() for t in meta.get('custom_tags', [])]
            
            # Gabungkan semua teks relevan menjadi satu string untuk pencarian tokens
            # Kita sertakan juga field 'link' jika ingin link bisa dicari
            link = item.get('link', '').lower()
            
            searchable_pool = [
                title, 
                desc, 
                code, 
                folder_cat, 
                link,
                *inner_cats, 
                *user_tags
            ]
            
            # --- Logika Pencarian AND ---
            # Pastikan SETIAP kata kunci (keyword) ada di salah satu field di atas
            is_match = True
            for kw in keywords:
                # Cek apakah keyword ini ada di salah satu isi searchable_pool
                if not any(kw in target for target in searchable_pool):
                    is_match = False
                    break
            
            if is_match:
                # Gabungkan data master dengan meta (statistik)
                # Field 'link' otomatis ikut karena ada di dalam {**item}
                matched.append({**item, **meta})
        
        # Urutkan berdasarkan Favorit lalu Hits terbanyak
        matched.sort(key=lambda x: (x.get('is_favorite', False), x.get('hits', 0)), reverse=True)
        
        return matched