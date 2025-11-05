import json
from datetime import datetime

class HistoryManager:
    def __init__(self, db_manager):
        self.db = db_manager
    
    def tampilkan_history(self):
        """Menampilkan history perkalian"""
        history = self.db.ambil_history()
        
        if not history:
            return "📝 Belum ada history perkalian"
        
        result = "📊 HISTORY PERKALIAN TERAKHIR:\n"
        result += "=" * 50 + "\n"
        
        for item in history:
            id_history, bilangan, hasil_json, timestamp = item
            hasil_perkalian = json.loads(hasil_json)
            
            # Format timestamp
            waktu = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
            format_waktu = waktu.strftime('%d/%m/%Y %H:%M')
            
            result += f"🆔: {id_history} | Bilangan: {bilangan} | {format_waktu}\n"
            result += "Hasil:\n"
            
            for i in range(1, min(6, len(hasil_perkalian) + 1)):
                result += f"   {bilangan} × {i} = {hasil_perkalian[i-1]}\n"
            
            if len(hasil_perkalian) > 5:
                result += f"   ... dan {len(hasil_perkalian) - 5} hasil lainnya\n"
            
            result += "-" * 50 + "\n"
        
        return result
    
    def simpan_perkalian(self, bilangan, hasil):
        """Menyimpan hasil perkalian"""
        self.db.simpan_history(bilangan, hasil)
    
    def bersihkan_history(self):
        """Membersihkan semua history"""
        self.db.hapus_history()
        return "✅ History berhasil dibersihkan!"