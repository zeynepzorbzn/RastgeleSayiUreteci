import time

# --- ALGORİTMA SINIFI (Nebula-RNG) ---
class NebulaRNG:
    def __init__(self, seed=None):
        """
        Başlangıç fonksiyonu.
        Seed verilmezse o anki zamanı kullanır.
        """
        if seed is None:
            self.state = int(time.time() * 1000)
        else:
            self.state = seed
        
        # 0 yutan eleman olduğu için state 0 olmamalı
        if self.state == 0:
            self.state = 123456789

    def next_int(self):
        """
        Bir sonraki rastgele tamsayıyı üretir.
        """
        # 1. Aşama: Xorshift Algoritması (Karıştırma)
        x = self.state
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17) & 0xFFFFFFFF
        x ^= (x << 5)  & 0xFFFFFFFF
        
        # Durumu güncelle
        self.state = x
        
        # 2. Aşama: Çarpımsal Karıştırma
        return (x * 2654435761) & 0xFFFFFFFF

    def range(self, min_val, max_val):
        """
        Belirli bir aralıkta sayı üretir.
        """
        return min_val + (self.next_int() % (max_val - min_val))

# --- KODUN ÇIKTI VERMESİ İÇİN GEREKLİ TEST KISMI ---
if __name__ == "__main__":
    print("=== NEBULA-RNG ALGORİTMASI TESTİ ===\n")

    # TEST 1: Sabit Seed (Her çalıştırışta aynı sonucu vermeli)
    rng1 = NebulaRNG(seed=42)
    print("--- Test 1: Sabit Seed (42) ---")
    print(f"Sayı 1: {rng1.next_int()}")
    print(f"Sayı 2: {rng1.next_int()}")
    print(f"Sayı 3: {rng1.next_int()}")

    # TEST 2: Farklı Seed (Farklı sonuçlar vermeli)
    rng2 = NebulaRNG(seed=999)
    print("\n--- Test 2: Farklı Seed (999) ---")
    print(f"Sayı 1: {rng2.next_int()}")

    # TEST 3: Aralık Testi (0 ile 100 arası)
    print("\n--- Test 3: 0-100 Arası 5 Rastgele Sayı ---")
    liste = []
    for _ in range(5):
        liste.append(rng1.range(0, 100))
    print(f"Sonuçlar: {liste}")