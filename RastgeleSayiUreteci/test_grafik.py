import time
import matplotlib.pyplot as plt # Çizim kütüphanesi

# --- BİZİM ALGORİTMA (Nebula-RNG) ---
class NebulaRNG:
    def __init__(self, seed=None):
        if seed is None:
            self.state = int(time.time() * 1000)
        else:
            self.state = seed
        if self.state == 0: self.state = 123456789

    def next_int(self):
        # Xorshift mantığı
        x = self.state
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17) & 0xFFFFFFFF
        x ^= (x << 5)  & 0xFFFFFFFF
        self.state = x
        return (x * 2654435761) & 0xFFFFFFFF

    def next_float(self):
        # 0.0 ile 1.0 arası sayı üret
        return self.next_int() / 0xFFFFFFFF

# --- GÖRSEL ANALİZ KISMI ---
def grafik_ciz():
    rng = NebulaRNG(seed=42)
    
    x_degerleri = []
    y_degerleri = []
    
    print("Noktalar üretiliyor, lütfen bekleyin...")
    
    # 1000 adet (x, y) koordinatı üretelim
    for _ in range(1000):
        x_degerleri.append(rng.next_float())
        y_degerleri.append(rng.next_float())

    # Grafiği oluştur
    plt.figure(figsize=(8, 8))
    plt.title("Nebula-RNG Dağılım Testi (1000 Nokta)")
    
    # Noktaları çiz (Scatter Plot)
    plt.scatter(x_degerleri, y_degerleri, s=10, c='blue', alpha=0.5)
    
    plt.xlabel("X Ekseni (Rastgele)")
    plt.ylabel("Y Ekseni (Rastgele)")
    plt.grid(True, linestyle='--', alpha=0.3)
    
    print("Grafik ekrana getiriliyor...")
    plt.show()

# Kodu çalıştır
if __name__ == "__main__":
    grafik_ciz()