# TUGAS 3 PBP

link HEROKU:
- https://tugas2pbpfathan.herokuapp.com/mywatchlist/html/
- https://tugas2pbpfathan.herokuapp.com/mywatchlist/json/
- https://tugas2pbpfathan.herokuapp.com/mywatchlist/xml/


### Perbedaan JSON, XML, HTML

1. Definisi    
- JSON atau *JavaScript Object Notation* adalah format file yang menggunakan *human-readable text* untuk menyimpan dan mentransmisikan objek data yang berisi pasangan *key-value*. JSON digunakan untuk menyimpan informasi secara terorganisir dan mudah diakses. 
- XML atau  *Extensive Markup Language* adalah bahasa *markup* yang bersifat *extensible* untuk menyimpan data.  XML memungkinkan Anda untuk mendefinisikan elemen markup dan menghasilkan bahasa markup yang disesuaikan.
- HTML atau *Hypertext Markup Language* adalah bahasa *markup* untuk web yang mendefinisikan struktur halaman web. Elemen-elemen seperti button, hyperlink, image, bahkan data dari *database* dapat ditampilkan pada halaman HTML.      

Perbedaan XML VS JSON   
*using XML*:
- menghasilkan dokumen XML (`.xml`)
- menggunakan XML DOM untuk me-*loop* pada dokumen
- mengambil *value* dan disimpan ke dalam variabel

*using JSON*:
- menghasilkan *JSON string* (`.json`)
- menggunakan JSON.parse() untuk melakukan *parse* pada *JSON string*
- alternatif yang lebih mudah digunakan dibanding XML.
- untuk beberapa aplikasi, JSON lebih cepat dan mudah daripada XML.

HTML tidak dapat dibandingkan karena HTML tidak bekerja seperti XML/JSON. XML cenderung lebih ke arah mengambil data dan menampilkannya. 

contoh JSON :
```py
Html>    
<Head>  
<title>  
Example of Header-levels  
</title>  
</Head>  
<Body>   
  
<h6> JavaTpoint </h6>   
<h5> JavaTpoint </h5>  
<h4> JavaTpoint </h4>  
<h3> JavaTpoint </h3>  
<h2> JavaTpoint </h2>  
<h1> JavaTpoint </h1>  
</Body>  
</Html>  
```

contoh XML:
```py
<employees>
  <employee>
    <firstName>John</firstName> <lastName>Doe</lastName>
  </employee>
  <employee>
    <firstName>Anna</firstName> <lastName>Smith</lastName>
  </employee>
  <employee>
    <firstName>Peter</firstName> <lastName>Jones</lastName>
  </employee>
</employees>
```

contoh JSON:
```py
{"employees":[
  { "firstName":"John", "lastName":"Doe" },
  { "firstName":"Anna", "lastName":"Smith" },
  { "firstName":"Peter", "lastName":"Jones" }
]}
```


### Mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah platform?

*Data delivery* sangat penting bagi proses kerja platform, karena kita membutuhkan mekanisme tersebut untuk menampilkan data dari database pada halaman *front-end*. Contohnya jika kita  melihat  di HP, jika tidak ada proses *data delivery* maka waktu terkini tidak dapat ditampilkan dan tidak muncul di sisi *user*, yang artinya tujuan dari program jam tersebut tidak tercapai.


### Implemetasi Checklist Tugas 3

Langkah-langkah yang dilakukan mirip seperti lab 1.
- buat *app* Django baru bernama `mywatchlist`
- tambahkan aplikasi `mywatchlist` pada variabel `INSTALLED_APPS` yang ada di `settings.py` di folder `project-django`
- di `models.py` input atribut sesuai perintah soal dan fieldnya mengikuti bentuk definisi atribut seperti tertera di bawah
```py
class WatchlistMovies(models.Model):
    is_watched = models.CharField(max_length=10)
    title = models.TextField()
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()
```
- buat 10 data pada `initial_mywatchlist_data.json` yang ada dalam `fixtures`
- buat `mywatchlist.html` dan sajikan sesuai keinginan. contoh di bawah
```py

    table tr {background-color:#25316D; color:#8758FF; border-color: #003865;}
</style>
<table style="width:100%; border: 10px;">
    <tr style="height:50px; color:#25316D; background-color:#8758FF;">
        <th><h2>Pernah Ditonton</h2></th>
        <th><h2>Judul Film</h2></th>
        <th><h2>Rating Film</h2></th>
        <th><h2>Tanggal Rilis</h2></th>
        <th><h2>Review Film</h2></th>
    </tr>
    {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
    {% for film in list_film %}
    <tr style="height:50px">
        <th><h3><p style="font-family: sans-serif;">{{film.is_watched}}</p></h3></th>
        <th><h3><p style="font-family: sans-serif">{{film.title}}</p></h3></th>
        <th><h3><p style="font-family: sans-serif">{{film.rating}}</p></h3></th>        
        <th><h3><p style="font-family: sans-serif">{{film.release_date}}</p></h3></th>        
        <th><h3><p style="font-family: sans-serif">{{film.review}}</p></h3></th>
        </tr>
    {% endfor %}
</table>
```
- modifikasi path di `urls.py` pada folder `project-django` seperti di bawah
```py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('mywatchlist/', include('mywatchlist.urls')),
    path('katalog/', include('katalog.urls')),

]
```
- buat 3 fungsi pada `views.py` untuk menyajikan data dalam format HTML, JSON, dan XML.
```py
def show_xml(request):
    data = WatchlistMovies.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistMovies.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
- membuat *routing* `mywatchlist` di `urls.py` seperti yg tertera di bawah
```py
urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('html/', show_mywatchlist, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]
```
- *push* ke dalam GitHub. Setelah di-*push*, deploy akan jalan dengan sendirinya dan tunggu sampai berhasil.


### Mengakses URL di Postman
1. url HTML
![image](https://user-images.githubusercontent.com/106417802/191498370-32937d2a-2926-4684-95ce-256fffd89d23.png)
2. url XML
![image](https://user-images.githubusercontent.com/106417802/191499049-707f81e3-68ff-4530-810a-36f91574fcd8.png)
3. url JSON
![image](https://user-images.githubusercontent.com/106417802/191499127-216fb8b3-8fd3-4f3b-b2c9-808e051cd4dd.png)


