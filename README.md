# UAS ROBOTIKA DAN SISTEM OTONOM
## NOMOR 1:
Sebuah robot bergerak dua roda (differential drive robot) harus bergerak dari Titik Start (S) menuju Titik Goal (G) pada lingkungan 2D yang memiliki beberapa rintangan statis. Lingkungan direpresentasikan dalam bentuk peta grid (occupancy grid), di mana sel tertentu tidak dapat dilewati oleh robot. 

Pada tahap awal, robot hanya bergerak berdasarkan arah langsung ke tujuan (go-to-goal) tanpa perencanaan jalur, sehingga sering 
- menabrak rintangan,
- terjebak pada jalur buntu,
- atau mengambil lintasan yang terlalu panjang. 

Untuk mengatasi masalah tersebut, tim Anda diminta untuk mengimplementasikan algoritma path planning pada simulasi robot mobile menggunakan salah satu atau lebih metode berikut: 
- Dijkstra,
- A*, atau
- Rapidly-exploring Random Tree (RRT). 
 
Simulasi dilakukan menggunakan Python, dan hasil perencanaan jalur akan digunakan sebagai lintasan referensi bagi robot. 
 
Pertanyaan:  
Bagaimana proses implementasi algoritma path planning yang Anda pilih (Dijkstra, A*, atau RRT) dalam simulasi robot mobile sehingga robot dapat menemukan jalur dari Start (S) ke Goal (G) secara aman dan efisien? 

Jelaskan secara rinci:
1. Pemodelan lingkungan simulasi, termasuk representasi peta (grid atau ruang kontinu), penentuan node/vertex, dan definisi sel rintangan.
2. Langkah-langkah implementasi algoritma path planning yang dipilih, mulai dari inisialisasi, proses pencarian jalur, hingga diperoleh lintasan akhir dari S ke G.
3. Perbandingan hasil jalur (panjang lintasan, jumlah belokan, dan waktu komputasi) jika algoritma Anda dibandingkan dengan algoritma path planning lain (misalnya Dijkstra vs A*, atau A* vs RRT).
4. Visualisasi dan analisis hasil simulasi, termasuk:
   - peta lingkungan,
   - jalur yang dihasilkan,
   - posisi Start dan Goal,
   - serta interpretasi mengapa jalur tersebut dianggap optimal atau layak untuk robot bergerak.

Hasil dapat disajikan dalam bentuk kode Python dan visualisasi grafik (misalnya peta grid dengan jalur hasil perencanaan).


# DIBUAT OLEH:
## KELOMPOK 1:
- JAROT WIWOHO               (41422110036)
- RAIHAN RAMANDHA SAPUTRA    (41422110039)
