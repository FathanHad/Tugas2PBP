# JavaScript & AJAX
### link dapat diakses [disini](https://tugas2pbpfathan.herokuapp.com/todolist/)

### Perbedaan *asynchronous programming* dengan *synchronous programming*

Pada *synchronous programming*, hanya satu operasi yang bisa dijalankan pada satu waktu, Ini dikarenakan syncronous merupakan *single-thread model*. Setiap program/tugas harus diselesaikan terlebih dahulu sebelum berpindah ke program/tugas selanjutnya. Maka dari itu, eksekusi dari setiap operasi itu bergantung pada keberhasilan operasi yang dilakukan sebelumnya. Arsitektur seperti ini dikenal dengan *blocking architecture*.

Pada *asynchronous programming*, operasi tidak bergantung pada operasi lainnya, sehingga program/tugas dapat berjalan secara paralel. Banyak operasi dapat dilakukan secara serentak tanpa harus menunggu program/tugas lainnya selesai dilakukan. Arsitektur seperti ini dikenal dengan *non-blocking architecture*.

### Arti Paradigma *Event-Driven Programming* dan contoh penerapannya

*Event-Driven Programming* merupakan paradigma programming dimana alur program ditentukan oleh event yang di-trigger oleh user seperti *mouse click* atau *button press*. Contoh pada tugas 6 yaitu akan membuat modal jika button Add New Task ditekan

### Penerapan *asynchronous programming* pada AJAX

AJAX mengimplementasikan teknik yang membuat halaman web dapat diupdate secara asynchronous tergantung event yang di-trigger user. Hanya beberapa bagian dari halaman yang datanya berubah sedikit saja yang akan di-*refresh*, bukannya seluruh halaman web. AJAX dapat mengakses data dari sumber luar bahkan setelah halaman web dimuat seluruhnya. 

### Implementasi Checklist

1. Membuat views untuk AJAX dan mengembalikan data dalam bentuk JSON
2. buat routing pada urls.py sesuai function
3. Pada AJAX GET, gunakan endpoint `/todolist/json` yang berisi data todolist untuk tujuan request method GET yang akan dibuat. Pada todolist.html, buat fungsi yang akan melakukan request ke endpoint `/todolist/json` dan data yang didapat akan diiterasi menjadi elemen HTML yang nanti ditambahkan ke halaman web. Fungsi tersebut harus selalu di-load setiap kali pengguna mengakses halaman tersebut.
4. pada AJAX POST, buat views yang akan membuat objek task dan me-return JsonResponse sebagai nilai kembaliannya. Nanti, JSON tersebut akan diterima oleh todolist.html. Untuk setiap kembalian dari views akan diproses di dalam todolist.html dan dijadikan card yang akan ditampilkan di halaman web. Buat juga modal untuk menambahkan task.