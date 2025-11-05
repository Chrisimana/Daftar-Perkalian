import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import json
from datetime import datetime
from database import DatabaseManager
from styles import GUIStyles, GUIColors

class PerkalianApp:
    def __init__(self, root):
        self.root = root
        self.db_manager = DatabaseManager()
        self.setup_gui()
    
    def setup_gui(self):
        """Setup antarmuka GUI"""
        self.root.title("✨ Daftar Perkalian ✨")
        self.root.geometry("700x600")
        self.root.configure(bg=GUIColors.BACKGROUND)
        self.root.resizable(True, True)
        
        # Center window on screen
        self.center_window()
        
        # Header Frame
        header_frame = tk.Frame(self.root, bg=GUIColors.PRIMARY, height=80)
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="✨ DAFTAR PERKALIAN ✨",
            font=GUIStyles.TITLE_FONT,
            bg=GUIColors.PRIMARY,
            fg=GUIColors.WHITE,
            pady=20
        )
        title_label.pack(expand=True)
        
        # Main Content Frame
        main_frame = tk.Frame(self.root, bg=GUIColors.BACKGROUND)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Input Section
        input_frame = tk.LabelFrame(
            main_frame,
            text="🎯 Input Bilangan",
            font=GUIStyles.HEADER_FONT,
            bg=GUIColors.BACKGROUND,
            fg=GUIColors.PRIMARY,
            padx=15,
            pady=15
        )
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(
            input_frame,
            text="Masukkan Bilangan:",
            font=GUIStyles.NORMAL_FONT,
            bg=GUIColors.BACKGROUND,
            fg=GUIColors.TEXT_DARK
        ).pack(side=tk.LEFT)
        
        self.bilangan_entry = tk.Entry(
            input_frame,
            font=GUIStyles.NORMAL_FONT,
            width=15,
            justify='center',
            relief='solid',
            borderwidth=1,
            bg=GUIColors.WHITE
        )
        self.bilangan_entry.pack(side=tk.LEFT, padx=10)
        self.bilangan_entry.bind('<Return>', lambda e: self.tampilkan_perkalian())
        self.bilangan_entry.focus()
        
        # Button Section
        button_frame = tk.Frame(main_frame, bg=GUIColors.BACKGROUND)
        button_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Tombol-tombol utama
        self.btn_tampilkan = tk.Button(
            button_frame,
            text="🧮 Tampilkan Perkalian",
            command=self.tampilkan_perkalian,
            **GUIStyles.primary_button()
        )
        self.btn_tampilkan.pack(side=tk.LEFT, padx=5)
        
        self.btn_history = tk.Button(
            button_frame,
            text="📊 Lihat History",
            command=self.tampilkan_history,
            **GUIStyles.secondary_button()
        )
        self.btn_history.pack(side=tk.LEFT, padx=5)
        
        self.btn_clear = tk.Button(
            button_frame,
            text="🗑️ Bersihkan History",
            command=self.bersihkan_history,
            **GUIStyles.danger_button()
        )
        self.btn_clear.pack(side=tk.LEFT, padx=5)
        
        # Result Area
        result_frame = tk.LabelFrame(
            main_frame,
            text="📊 Hasil Perkalian",
            font=GUIStyles.HEADER_FONT,
            bg=GUIColors.BACKGROUND,
            fg=GUIColors.PRIMARY,
            padx=15,
            pady=15
        )
        result_frame.pack(fill=tk.BOTH, expand=True)
        
        # Text area dengan scrollbar
        self.result_text = scrolledtext.ScrolledText(
            result_frame,
            wrap=tk.WORD,
            font=GUIStyles.MONOSPACE_FONT,
            bg=GUIColors.WHITE,
            fg=GUIColors.TEXT_DARK,
            relief='solid',
            borderwidth=1,
            padx=10,
            pady=10
        )
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        # Status Bar
        self.status_bar = tk.Label(
            self.root,
            text="👋 Selamat datang! Masukkan bilangan dan klik 'Tampilkan Perkalian'",
            bg=GUIColors.DARK,
            fg=GUIColors.WHITE,
            font=('Arial', 9),
            anchor=tk.W,
            padx=10
        )
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)
        
        # Tampilkan welcome message
        self.tampilkan_pesan_welcome()
    
    def center_window(self):
        """Center window di layar"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def tampilkan_pesan_welcome(self):
        """Menampilkan pesan welcome"""
        welcome_text = """✨ PROGRAM PERKALIAN SUPER ✨

Fitur yang tersedia:
• 🧮 Tampilkan tabel perkalian 1-10
• 📊 Simpan history secara otomatis
• 📝 Lihat riwayat perkalian sebelumnya
• 🗑️  Bersihkan history

Cara menggunakan:
1. Masukkan bilangan di kolom input
2. Klik 'Tampilkan Perkalian' atau tekan Enter
3. Lihat hasilnya di area bawah

Contoh: Masukkan '5' untuk melihat perkalian 5"""
        
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(1.0, welcome_text)
        self.update_status("Siap menerima input...")
    
    def update_status(self, message):
        """Update status bar"""
        self.status_bar.config(text=f"📢 {message}")
    
    def tampilkan_perkalian(self):
        """Menampilkan hasil perkalian"""
        try:
            bilangan_text = self.bilangan_entry.get().strip()
            if not bilangan_text:
                messagebox.showwarning("Peringatan", "Silakan masukkan bilangan terlebih dahulu!")
                self.bilangan_entry.focus()
                return
                
            bilangan = int(bilangan_text)
            
            # Hitung hasil perkalian
            hasil = self.hitung_perkalian(bilangan)
            
            # Tampilkan hasil
            self.tampilkan_hasil_di_text(bilangan, hasil)
            
            # Simpan ke history
            success = self.db_manager.simpan_history(bilangan, hasil)
            if success:
                self.update_status(f"Perkalian {bilangan} berhasil ditampilkan dan disimpan!")
            else:
                self.update_status(f"Perkalian {bilangan} ditampilkan (gagal menyimpan)")
            
        except ValueError:
            messagebox.showerror("Error", "Masukkan bilangan yang valid!\nContoh: 5, -3, 10")
            self.update_status("Error: Input harus berupa bilangan bulat")
            self.bilangan_entry.focus()
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
            self.update_status("Error: Terjadi kesalahan sistem")
    
    def hitung_perkalian(self, bilangan):
        """Menghitung perkalian 1-10"""
        return [bilangan * i for i in range(1, 11)]
    
    def tampilkan_hasil_di_text(self, bilangan, hasil):
        """Menampilkan hasil di text area"""
        result_text = f"📊 TABEL PERKALIAN {bilangan}\n"
        result_text += "=" * 40 + "\n\n"
        
        for i, hsl in enumerate(hasil, 1):
            result_text += f"  {bilangan:2d} × {i:2d} = {hsl:3d}\n"
        
        result_text += f"\n{'=' * 40}\n"
        result_text += f"✨ Total: {sum(hasil):,}\n"
        result_text += f"📈 Rata-rata: {sum(hasil)/len(hasil):.1f}\n"
        
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(1.0, result_text)
    
    def tampilkan_history(self):
        """Menampilkan history perkalian"""
        try:
            history_data = self.db_manager.ambil_history()
            
            if not history_data:
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(1.0, "📝 Belum ada history perkalian")
                self.update_status("Tidak ada history yang tersimpan")
                return
            
            history_text = "📊 HISTORY PERKALIAN TERAKHIR:\n"
            history_text += "=" * 50 + "\n\n"
            
            for item in history_data:
                id_history, bilangan, hasil_json, timestamp = item
                hasil_perkalian = json.loads(hasil_json)
                
                # Format timestamp
                try:
                    waktu = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                    format_waktu = waktu.strftime('%d/%m/%Y %H:%M')
                except:
                    format_waktu = timestamp
                
                history_text += f"🆔: {id_history} | Bilangan: {bilangan} | {format_waktu}\n"
                history_text += "Hasil:\n"
                
                # Tampilkan 5 hasil pertama
                for i in range(1, min(6, len(hasil_perkalian) + 1)):
                    history_text += f"   {bilangan} × {i} = {hasil_perkalian[i-1]}\n"
                
                if len(hasil_perkalian) > 5:
                    history_text += f"   ... dan {len(hasil_perkalian) - 5} hasil lainnya\n"
                
                history_text += "-" * 50 + "\n\n"
            
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(1.0, history_text)
            self.update_status(f"Menampilkan {len(history_data)} data history")
            
        except Exception as e:
            messagebox.showerror("Error", f"Gagal memuat history: {str(e)}")
            self.update_status("Error: Gagal memuat history")
    
    def bersihkan_history(self):
        """Membersihkan history"""
        if messagebox.askyesno(
            "Konfirmasi", 
            "Apakah Anda yakin ingin menghapus SEMUA history perkalian?\nTindakan ini tidak dapat dibatalkan!"
        ):
            success = self.db_manager.hapus_history()
            if success:
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(1.0, "✅ History berhasil dibersihkan!\n\nSemua data history telah dihapus.")
                self.update_status("History berhasil dibersihkan")
                messagebox.showinfo("Sukses", "History berhasil dibersihkan!")
            else:
                messagebox.showerror("Error", "Gagal membersihkan history!")
                self.update_status("Error: Gagal membersihkan history")