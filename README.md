# P11-ImplementasiOTP

<h1>Penjelasan OTP</h1>
Penjelasan Mengenai OTP
		Proses enkripsi pada OTP yang saya implementasikan melibatkan konversi plaintext dan kunci ke dalam format biner menggunakan fungsi yang telah disediakan. Karena hasilnya berupa daftar (list), setiap elemen dalam daftar plaintext diambil satu per satu. Kemudian, setiap elemen tersebut di-XOR dengan elemen yang sesuai dalam daftar kunci menggunakan perulangan. 
  
Hasil XOR ini kemudian digabungkan kembali menjadi satu variabel.Proses dekripsi dilakukan dengan cara yang sama. Dikarenakan kita sudah memiliki variabel biner dari hasil enkripsi beserta kuncinya, proses dekripsi dapat diimplementasikan kembali dengan menggunakan perulangan yang serupa.

Untuk hasilnya tinggal jalankan Saja
