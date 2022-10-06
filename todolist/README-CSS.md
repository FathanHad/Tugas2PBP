# *Web Design* Using HTML, CSS, and CSS Framework
### link dapat diakses [disini](https://tugas2pbpfathan.herokuapp.com/todolist/)

### Perbedaan Inline, Internal, dan External CSS, Sebutkan kelebihan dan kekurangan masing-masing


-  Inline CSS  
Inline CSS dipakai untuk men-*style* sebuah elemen HTML yang spesifik. Cara menggunakannya yaitu menambahkan atribut `style` ke tiap HTML tag.   
Style ini tidak direkomendasikan karena tiap tag harus di-*style* secara manual. Tetapi, akan sangat berguna jika hanya sedikit elemen saja yang akan di-*styling*

- Internal CSS  
Internal CSS membutuhkan `<style>` tag dalam <head> *section*. *Style* ini sangat efektif untuk men-*styling* sebuah single page saja. Tetapi, akan memakan banyak waktu jika memakainya untuk multiple pages.

- External CSS   
External CSS akan menghubungkan web dengan file CSS external . Cara ini adalah cara yang efisien terutama untuk *styling* website besar karena kita hanya perlu meng-edit external file saja dan akan terimplementasi ke semua page.

### Macam-macam tag HTML5
- `<html>` : tag untuk membuat dokumen HTML
- `<head>` : tag untuk informasi meta data
- `<title>` : tag untuk membuat judul halaman
- `<body>` : tag untuk menaruh konten website
- `<h1>` - `<h6>` : tag untuk membuat heading
- `<table>` : tag untuk membuat tabel
- `<th>`, `<tr>`, `<td>`: tag untuk membuat baris, cell header, dan cell dalam tabel.
- `<div>` : tag untuk membuat sebuah bagian dalam dokumen

### Tipe-tipe CSS selector
- Selektor tag, memilih berdasarkan nama tag
- Selektor Class, memilih berdasarkan nama class yang diberikan. Selektor class dibuat dengan tanda `.` didepannya dan dapat menggunakan lebih dari satu class.
- Selektor ID, hampir mirip dengan selektor class, tetapi hanya boleh digunakan oleh satu elemen saja. Selektor ini ditandai dengan `#` di depannya
- Selektor atribut,  selektor yang memilih elemen berdasarkan atribut.
- Selektor Universal, selektor yang digunakan untuk menyeleksi semua elemen pada jangkauan tertentu. Selektor ini biasanya dipakai untuk me-reset `padding` dan `margin` CSS bawaan browser.

### implementasi checklist

- Tambahkan link pada `base.html` agar dapat memakai bootstrap.
- lakukan implementasi sesuai preferensi untuk login register dan create-task (menambah warna pada background, button, dan textfield)
- untuk halaman todolist, gunakan cards pada setiap task seperti di bawah ini
```py
 <div class="card text-white bg-secondary mb-3 card text-center">
    <div class="card-body mb-4">
        <h4 class="card-title">{{list.title}}</h4>
        <p> Date : {{list.date}} </p>
        <p> {{list.description}} </p>
        {% if list.is_finished %}
            <h5>Finished</h5>
        {% else %}
            <h5>Not Finished</h5>
        {% endif %}
        <button class="btn btn-outline-success">
            <a href="{% url 'todolist:update-task' list.id %}">Update Task</a>
        </button>
        <button class="btn btn-outline-danger">
            <a href="{% url 'todolist:delete-task' list.id %}">Delete</a>
        </button>
    </div>
</div>
```
- gunakan container agar halaman dapat menjadi responsive(saat page diubah, atribut juga ikut berubah ukurannya)

