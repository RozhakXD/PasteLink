# PasteLink - View Booster for Pastelink

**PasteLink** adalah tools sederhana yang dirancang untuk meningkatkan jumlah tampilan (views) pada tautan yang dihosting di [Pastelink](https://pastelink.net). Dengan menggunakan kombinasi berbagai agen pengguna (user-agent) acak, tools ini dapat mensimulasikan permintaan dari perangkat yang berbeda untuk menghasilkan tampilan yang lebih banyak.

## Fitur
- Menggunakan agen pengguna (user-agent) acak untuk mengurangi kemungkinan deteksi.
- Mendukung eksekusi paralel untuk mempercepat proses permintaan.
- Simulasi permintaan dari perangkat Android dan Windows.
- Statistik tampilan `sukses`, `gagal`, dan `error` secara real-time.

## Cara Kerja
1. Pengguna diminta untuk memasukkan tautan dari **Pastelink** yang valid.
2. Memasukkan jumlah permintaan yang ingin dikirim.
3. Script secara otomatis akan mengirim permintaan GET ke tautan yang diberikan dengan **User-Agent** acak.
4. Hasil akan ditampilkan di terminal, dengan jumlah permintaan yang berhasil, gagal, atau terjadi kesalahan.

## Persyaratan
- **Python 3.x**
- **requests** library (install menggunakan `pip install requests`)

## Instalasi
1. Clone repository ini atau unduh file `Run.py` ke dalam direktori lokal.

    ```bash
    git clone https://github.com/RozhakXD/PasteLink.git
    ```
3. Install dependencies yang dibutuhkan:

    ```bash
    pip install requests
    ```
4. Jalankan script:

    ```bash
    python Run.py
    ```

## Penggunaan
1. Ketika menjalankan script, Anda akan diminta untuk memasukkan tautan Pastelink. Pastikan tautan dimulai dengan `https://pastelink.net/`.
2. Masukkan jumlah permintaan yang ingin dikirim. Misalnya, 100 permintaan untuk 100 views.
3. Script akan menjalankan proses, dan Anda akan melihat hasilnya langsung di terminal:
    - Success: jumlah permintaan yang berhasil.
    - Failed: jumlah permintaan yang gagal.
    - Error: jumlah error yang terjadi.

## Masalah dan Solusi
Jika views tidak masuk, kemungkinan besar terjadi **spam** karena Anda terlalu banyak menginputkan jumlah permintaan (request) yang dikirim sekaligus. Berikut adalah beberapa cara yang dapat membantu mengatasi masalah tersebut:
- **Kurangi JUMLAH PERMINTAAN**: Cobalah mengurangi jumlah permintaan yang dikirimkan dalam satu waktu agar tidak terdeteksi sebagai spam.
- Gunakan **VPN**: Mengubah lokasi IP dengan menggunakan VPN bisa membantu menghindari deteksi spam.
- Aktifkan **MODE PESAWAT**: Pada perangkat mobile, aktifkan dan matikan **mode pesawat** sebelum mengirim permintaan baru untuk menyegarkan jaringan.

## Tangkapan Layar
![FunPic_20240928](https://github.com/user-attachments/assets/7ff00876-3a48-43d2-bb22-be644ea9ae86)

## Dukungan
Jika Anda merasa project ini bermanfaat dan ingin memberikan dukungan, Anda bisa memberikan tip melalui:
- [Trakteer](https://trakteer.id/rozhak_official/tip)
- [PayPal](https://paypal.me/rozhak9)

Dukungan Anda sangat membantu untuk terus mengembangkan project ini.

## Changelog
**v1.0.0**
- Rilis awal dengan fitur utama: mengirim permintaan otomatis ke tautan Pastelink.

## Tanggung Jawab Pengguna
Script ini dibuat hanya untuk keperluan edukasi dan testing. Penggunaan script ini untuk tujuan yang melanggar kebijakan **Pastelink** atau situs lain merupakan tanggung jawab pengguna. Gunakan dengan bijak!

## Melaporkan Masalah
Jika Anda menemukan bug atau masalah lainnya, silakan laporkan melalui [GitHub Issues](https://github.com/RozhakXD/PasteLink/issues).

## Lisensi
Script ini dilisensikan di bawah lisensi [MIT](https://github.com/RozhakXD/PasteLink?tab=MIT-1-ov-file).
