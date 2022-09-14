# Link herokuapp
https://tugas2pbpfathan.herokuapp.com/katalog/



# bagan request client
![image](https://user-images.githubusercontent.com/106417802/190195744-fad1056a-98f4-4a37-9ab5-8462f4eb5c9b.png)

Saat _user_ meminta _request_ ke server, Django akan mengarahkan ke urls.py/urlconfig yang nantinya akan diteruskan ke views.py. Nantinya di dalam views.py ini, apabila dibutuhkan, dapat memanggil _query_ ke models untuk melakukan transaksi data dengan _database_ yang akan dikembalikan lagi ke views sebagai _response_ dari request user. _Response_ yang keluar akan meng-generate suatu halaman HTML (katalog.html) yang nantinya akan tampil dengan _display_ dari data-data yang diambil dari database. Selanjutnya, _user_ sudah dapat mengakses halaman HTML.


# Mengapa perlu menggunakan _Virtual Environment?
Dengan memakai _virtual_ _environment_, kita seperti memakai ruang lain terpisah untuk project Django yang dikerjakan tanpa menganggu Python yang notabene-nya aplikasi global. _Virtual_ _environment_ juga dapat mengatur _packages_ apa saja yang diperlukan untuk diinstal dalam _project_ ini sehingga _workspace_ dari _project_ terkesan lebih "bersih". _Virtual_ _environment_ juga dipakai untuk menghindari _error_ yang disebabkan oleh perbedaan versi _libraries_ dari _project_ dan Django-nya sendiri. Kita tetap masih dapat membuat aplikasi web berbasis Django tanpa virtual environment, hanya saja kurang aman dan efektif. Secara keseluruhan, _virtual_ _enviroment_ adalah salah satu _best_ _practice_ saat mengerjakan berbagai macam _project_ yang berbeda.



# Proses Implementasi
Pertama, untuk mengambil data dari model, buat variabel untuk menampung data yang akan diambil dari _database_. Kedua, untuk proses _routing_, modifikasilah urls.py yang terdapat di folder katalog dan project-django. Ketiga, modifikasilah katalog.html sesuai arahan untuk menampilkan pemetaan data sesuai template. Terakhir, buatlah app heroku yang baru, simpan juga API _key_ akun heroku, lalu masukkan keduanya pada action secrets _repository_ yang sama. Nama app heroku akan ditampung oleh HEROKU_APP_NAME dan API key akan ditampung oleh HEROKU_API_KEY. Lakukan re-run _workflows_ pada tab _actions_. Aplikasi sudah berjalan dan dapat diakses melalui internet.
