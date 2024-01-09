#====================================
#Pemilu Simulator by Utonion Group
#====================================

# Logical stuff

import time
import random

vote_anies_0 = random.randint(1, 1000)
vote_prabowo_0 = random.randint(1, 1000)
vote_ganjar_0 = random.randint(1, 1000)

vote_anies_1 = random.randint(1, 1000)
vote_prabowo_1 = random.randint(1, 1000)
vote_ganjar_1 = random.randint(1, 1000)

vote_anies_2 = random.randint(1, 1220)
vote_prabowo_2 = random.randint(1, 1220)
vote_ganjar_2 = random.randint(1, 1220)

vote_anies_3 = random.randint(1, 1000)
vote_prabowo_3 = random.randint(1, 1000)
vote_ganjar_3 = random.randint(1, 1000)

vote_anies_4 = random.randint(1, 1000)
vote_prabowo_4 = random.randint(1, 1000)
vote_ganjar_4 = random.randint(1, 1000)

vote_anies_5 = random.randint(1, 1000)
vote_prabowo_5 = random.randint(1, 1000)
vote_ganjar_5 = random.randint(1, 1000)

pilihan_anies_bulan_1 = vote_anies_0 + vote_anies_1
pilihan_anies_bulan_2 = pilihan_anies_bulan_1 + vote_anies_2
pilihan_anies_bulan_3 = pilihan_anies_bulan_2 + vote_anies_3
pilihan_anies_bulan_4 = pilihan_anies_bulan_3 + vote_anies_4
pilihan_anies_bulan_5 = pilihan_anies_bulan_4 + vote_anies_5

pilihan_prabowo_bulan_1 = vote_prabowo_0 + vote_prabowo_1
pilihan_prabowo_bulan_2 = pilihan_prabowo_bulan_1 + vote_prabowo_2
pilihan_prabowo_bulan_3 = pilihan_prabowo_bulan_2 + vote_prabowo_3
pilihan_prabowo_bulan_4 = pilihan_prabowo_bulan_3 + vote_prabowo_4
pilihan_prabowo_bulan_5 = pilihan_prabowo_bulan_4 + vote_prabowo_5

pilihan_ganjar_bulan_1 = vote_ganjar_0 + vote_ganjar_1
pilihan_ganjar_bulan_2 = pilihan_ganjar_bulan_1 + vote_ganjar_2
pilihan_ganjar_bulan_3 = pilihan_ganjar_bulan_2 + vote_ganjar_3
pilihan_ganjar_bulan_4 = pilihan_ganjar_bulan_3 + vote_ganjar_4
pilihan_ganjar_bulan_5 = pilihan_ganjar_bulan_4 + vote_ganjar_5

def pemilu():
    print("Terima kasih telah memilih! Simulasi ini akan menjalankan anda selama 5 bulan musim pemilu! Jika presiden yang kamu pilih menang maka kamu menang taruhan! Jika presiden yang kamu pilih kalah maka kamu juga kalah!")
    time.sleep(2)
    print(f"Bulan 0:\n1. Anies Baswedan: {vote_anies_0}\n2. Prabowo Subianto: {vote_prabowo_0}\n3. Ganjar Pranowo: {vote_ganjar_0}")
    time.sleep(6)
    print(f"Bulan 1:\n1. Anies Baswedan: {vote_anies_1} | Total: {pilihan_anies_bulan_1}\n2. Prabowo Subianto: {vote_prabowo_1} | Total: {pilihan_prabowo_bulan_1}\n3. Ganjar Pranowo: {vote_ganjar_1} | Total: {pilihan_ganjar_bulan_1}")
    time.sleep(6)
    print(f"Bulan 2:\n1. Anies Baswedan: {vote_anies_2} | Total: {pilihan_anies_bulan_2}\n2. Prabowo Subianto: {vote_prabowo_2} | Total: {pilihan_prabowo_bulan_2}\n3. Ganjar Pranowo: {vote_ganjar_2} | Total: {pilihan_ganjar_bulan_2}")
    time.sleep(6)
    print(f"Bulan 3:\n1. Anies Baswedan: {vote_anies_3} | Total: {pilihan_anies_bulan_3}\n2. Prabowo Subianto: {vote_prabowo_3} | Total: {pilihan_prabowo_bulan_3}\n3. Ganjar Pranowo: {vote_ganjar_3} | Total: {pilihan_ganjar_bulan_3}")
    time.sleep(6)
    print(f"Bulan 4:\n1. Anies Baswedan: {vote_anies_4} | Total: {pilihan_anies_bulan_4}\n2. Prabowo Subianto: {vote_prabowo_4} | Total: {pilihan_prabowo_bulan_4}\n3. Ganjar Pranowo: {vote_ganjar_4} | Total: {pilihan_ganjar_bulan_4}")
    time.sleep(6)
    print(f"Bulan 5(Bulan Terakhir):\n1. Anies Baswedan: {vote_anies_5} | Total: {pilihan_anies_bulan_5}\n2. Prabowo Subianto: {vote_prabowo_5} | Total: {pilihan_prabowo_bulan_5}\n3. Ganjar Pranowo: {vote_ganjar_5} | Total: {pilihan_ganjar_bulan_5}")
    
    jumlah_anies = (vote_anies_0 + vote_anies_1 + vote_anies_2 + vote_anies_3 + vote_anies_4 + vote_anies_5)
    jumlah_prabowo = (vote_prabowo_0 + vote_prabowo_1 + vote_prabowo_2 + vote_prabowo_3 + vote_prabowo_4 + vote_prabowo_5)
    jumlah_ganjar = (vote_ganjar_0 + vote_ganjar_1 + vote_ganjar_2 + vote_ganjar_3 + vote_ganjar_4 + vote_ganjar_5)
    
    if choice == "1" and jumlah_anies > jumlah_prabowo and jumlah_anies > jumlah_ganjar:
        print("Kamu menang! Kamu mendapatkan uang Rp. 20.000")
        print("Kamu mendapatkan achievement: 'Menang dengan pilihan Anies!'")
    elif choice == "2" and jumlah_prabowo > jumlah_anies and jumlah_prabowo > jumlah_ganjar:
        print("Kamu menang! Kamu mendapatkan uang Rp. 20.000")
        print("Kamu mendapatkan achievement: 'Menang dengan pilihan Prabowo!'")
    elif choice == "3" and jumlah_ganjar > jumlah_prabowo and jumlah_ganjar > jumlah_anies:
        print("Kamu menang! Kamu mendapatkan uang Rp. 20.000")
        print("Kamu mendapatkan achievement: 'Menang dengan pilihan Ganjar!'")
    else:
        print("Kamu kalah! Kamu dipaksa untuk membayar temanmu Rp. 20.000")
        print("Kamu mendapatkan achievement: 'Kalah!'")

# Game Start
print("Rabu, 14 Februari 2024")
time.sleep(2)
print("Kamu dan temanmu sedang berada dalam momen kebosanan, hal itu mendorong keputusan untuk terlibat dalam sebuah taruhan. Taruhannya berpusat pada hasil pemilu 2024. Syaratnya sederhana: pihak yang kalah harus membayar Rp. 20.000 kepada peserta yang menang.")
time.sleep(3)
print("Hakmu sebagai masyarakat Indonesia adalah untuk berpartisipasi dalam pemilu setiap 4 tahun. Pada pemilu tahun ini terdapat 3 kandidat, yakni:\nAnies Baswedan (capres nomor urut 1),\nPrabowo Subianto (capres nomor urut 2), dan\nGanjar Pranowo (capres nomor urut 3)")
time.sleep(3)
print("Pemilu ini berjalan selama 5 bulan. Pilihlah presiden idamanmu sekarang!")
time.sleep(2)
while True:
    print("""
        1. Anies Baswedan
        2. Prabowo Subianto
        3. Ganjar Pranowo
        """)
    choice = input("Presiden yang akan anda pilih: ")
    try:
        if choice == "1" or choice == "2" or choice == "3":
            pemilu()
            quit()
        elif choice > 1 or choice > 2 or choice > 3:
            raise ValueError("Masukkan angka antara 1-3!")
    except ValueError as e:
        print(f"Error: {e}")
