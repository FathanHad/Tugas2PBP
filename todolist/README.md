# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django
### link dapat diakses [disini](https://tugas2pbpfathan.herokuapp.com/todolist/)

### Kegunaan `{% csrf_token %}` pada elemen `<form>`?? Apa yang terjadi jika tidak menggunakannya???


CSRF token dibutuhkan untuk mencegah serangan CSRF. CSRF adalah sebuah serangan yang membuat pengguna internet  tanpa sadar mengirimkan request (permintaan) kepada suatu aplikasi website melalui aplikasi website yang sedang digunakan sehingga, aplikasi tersebut mengeksekusi suatu tindakan yang sebenarnya tidak dikehendaki oleh pengguna internet.

CSRF Token dapat mencegah serangan CSRF yang akan membuat penyerang tidak mungkin melakukan permintaan HTTP yang secara sepenuhnya valid yang cocok untuk diumpankan ke pengguna korban. Dikarena penyerang tidak dapat menentukan atau memprediksi nilai token CSRF pengguna, sehingga tidak dapat membuat permintaan dengan semua parameter yang diperlukan aplikasi untuk memenuhi permintaan tersebut.

### Apakah kita dapat membuat elemen `<form>` tanpa menggunakan generator seperti `{{ form.as_table }}`?? Jelaskan gambaran besar cara membuat `<form>` secara manual.

Ya, caranya yaitu dengan menggunakan `<form>` sebagai *wrapper*, lalu *set* atribut `method` dan `action` dengan *value* yang dibutuhkan. `method` atribut dipakai untuk menspesifikasi method HTTP yang digunakan untuk mengirim *request* ke server, sedangkan *action* atribut digunakan untuk menspesifikasi *endpoint* dari *request* yang akan dikirim. Setelah `<form>` dan elemennnya dibuat, kita dapat mengubah tipe atribut untuk menspesifikasi input apa yang kita inginkan dan memberikan `name` atribut suatu nilai untuk menspesifikasi *key* data yang akan dikirim. Terakhir, kita juga dapat memberikan elemen `<button>` untuk men-*trigger* HTTP *request* ke server.

### Jelaskan alur data dari submisi pengguna melalui HTML form, penyimpanan data dari *database*, sampai munculnya data yang telah disimpan pada *template* HTML

Saat user menekan button submit yang sudah di-link dengan suatu *function* pada views.py, yang mana akan di route ke sebuah function yang menerima request, HTML yang akan ditampilkan, dan input user. Data yang user masukkan pada form diambil oleh function dan ditampilkan pada `show_todolist`

### Implementasi Checklist

- Buat aplikasi baru bernama `todolist` kemudian masukkan pada `installed_apps` di `settings.py` pada `project_django`. Tambahkan path pada `urls.py` di `project_django` agar dapat mengakses  http://localhost:8000/todolist
- pada `models.py`, buat model bernama Task dan atribut sesuai ketentuan soal
- melakukan implementasi form registrasi, login, logout
- membuat templates untuk menampilkan halaman form todolist dan menambahkan hal-hal yang diminta soal
- membuat `forms.py` untuk mengambil data 'penambahan task' dan menampilkannya dengan bantuan fuction pada `views.py`
- membuat routing dengan menambahkan urlpatterns baru pada `urls.py` agar setiap fungsi pada views dapat diakses menggunakan url yang tersedia pada soal
- melakukan deployment ke heroku dan menambahkan 2 akun pengguna dan 3 task.
 