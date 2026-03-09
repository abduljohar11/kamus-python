class SearchEngine:
    @staticmethod
    def search(query, all_master, stats):
        keywords = query.lower().strip().split()
        if not keywords:
            return []
            
        matched = []
        
        # Cek apakah ada request spesifik cari di kode saja (prefix c:)
        force_code_search = any(kw.startswith('c:') for kw in keywords)
        
        # Bersihkan keywords dari prefix jika ada
        clean_keywords = [kw.replace('c:', '') if kw.startswith('c:') else kw for kw in keywords]

        for item in all_master:
            s_id = item['id']
            meta = stats.get(s_id, {"hits": 0, "is_favorite": False, "custom_tags": []})
            
            # --- Persiapan Data ---
            title = item.get('title', '').lower()
            desc = item.get('description', '').lower()
            code = item.get('code', '').lower()
            folder_name = item.get('category', '').lower()
            inner_cats = [c.lower() for c in item.get('categories', [])]
            user_tags = [t.lower() for t in meta.get('custom_tags', [])]
            
            # Pool Utama (Metadata)
            metadata_pool = [title, desc, folder_name, *inner_cats, *user_tags]
            
            # --- Logika Matching ---
            is_match = True
            for kw in clean_keywords:
                # 1. Cek di metadata dulu (Prioritas Utama)
                found_in_metadata = any(kw in target for target in metadata_pool)
                
                # 2. Cek di kode (Hanya jika force_code_search AKTIF atau keyword tidak ketemu di metadata)
                found_in_code = kw in code
                
                if force_code_search:
                    # Jika pakai c:, maka HARUS ada di kode
                    if not found_in_code:
                        is_match = False
                        break
                else:
                    # Jika pencarian normal, match jika ada di metadata ATAU kode
                    if not (found_in_metadata or found_in_code):
                        is_match = False
                        break
            
            if is_match:
                matched.append({**item, **meta})
        
        # --- LOGIKA SORTING (Prioritas) ---
        def sorting_priority(x):
            is_fav = x.get('is_favorite', False)
            hits = x.get('hits', 0)
            
            # Boost score jika keyword ada di judul (lebih relevan daripada di dalam kode)
            title_boost = 1 if any(kw in x.get('title', '').lower() for kw in clean_keywords) else 0
            
            # Boost score jika query cocok dengan nama folder
            folder_match = 1 if any(kw in x.get('category', '').lower() for kw in clean_keywords) else 0
            
            return (is_fav, folder_match, title_boost, hits)

        matched.sort(key=sorting_priority, reverse=True)
        
        return matched