import tkinter as tk
from gui_app import PerkalianApp

def main():
    """Fungsi utama untuk menjalankan aplikasi GUI"""
    print("🚀 Memulai Program Perkalian Super...")
    print("📱 Mode: GUI")
    print("⏳ Membuat interface...")
    
    try:
        # Buat root window
        root = tk.Tk()
        
        # Inisialisasi aplikasi
        app = PerkalianApp(root)
        
        print("✅ GUI berhasil dimuat!")
        print("🎯 Petunjuk:")
        print("   - Masukkan bilangan di kolom input")
        print("   - Tekan Enter atau klik 'Tampilkan Perkalian'")
        print("   - Gunakan menu untuk melihat history")
        
        # Jalankan main loop
        root.mainloop()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Pastikan Tkinter terinstall dengan benar")
        input("Tekan Enter untuk keluar...")

if __name__ == "__main__":
    main()