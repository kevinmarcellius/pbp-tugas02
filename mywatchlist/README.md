# Tugas 3 PBP
Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

[Link mywatchlist/html](https://pbp-tugas02-kevin.herokuapp.com/mywatchlist/html/)

[Link mywatchlist/xml](https://pbp-tugas02-kevin.herokuapp.com/mywatchlist/xml/)

[Link mywatchlist/json](https://pbp-tugas02-kevin.herokuapp.com/mywatchlist/json/
)

## Perbedaan antara JSON, XML, dan HTML
1. HTML adalah markup language yang digunakan untuk menampilkan data dalam web browser
2. XML merupakan markup language dan menggunakan tag structure. XML menggunakan start tag dan end tag. XML awalnya diciptakan untuk membawa data, bukan menampikan data.
3. JSON merupakan format data, bukan markup language dan digunakan untuk menampilkan objek. JSON lebih mudah diparse daripada XML.
## Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan untuk mempermudah pengiriman data dari clients ke server atau sebaliknya. Contoh format yang digunakan untuk pengiriman data adalah HTML, XML, dan JSON
## Implementasi
1. Aktifkan virtual environment, lalu buat aplikasi django baru menggunakan perintah berikut 
```shell
python manage.py startapp mywatchlist
```
2. Pada `project_django/settings.py`, tambahkan `mywatchlist` pada `INSTALLED_APPS`
3. Pada `project_django/urls.py`, tambahkan urlmywatchlist pada urpatterns
```shell
...
path('mywatchlist/', include('mywatchlist.urls')),
...
```
4. Pada `mywatchlist/fixtures`, buat file .json baru yang berisi data-data yang akan ditampilkan. Pada tugas ini nama file yang saya buat adalah `initial_watchlist_data.json`. Lalu, jalankan perintah `python manage.py loaddata initial_wishlist_data.json` untuk memasukkan data tersebut ke dalam database Django lokal.

5. Pada `mywatchlist/models.py` buat sebuah model untuk menampilkan data-data. Lalu lakukan migrasi menggunakan perintah `python manage.py makemigrations`dan `python manage.py migrate`
```shell
watched = models.BooleanField()
title = models.CharField(max_length=50)
rating = models.FloatField()
release_date = models.CharField(max_length=20)
review = models.CharField(max_length=60)
```
6. Pada `mywatchlist/views.py`, buat fungsi-fungsi untuk menampilkan data dalam format XML, json, dan html
```shell
def show_html(request):
    data_watchlist = WatchlistItem.objects.all()
    context = {
    'list_movies': data_watchlist,
    'name': 'Kevin Marcellius Alrino',
    'student_id': '2106706193'
    }
    return render(request, "mywatchlist.html", context)
def show_xml(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
6. Pada `mywatchlist/urls.py` tambahkan urls berikut ke dalam `urlpatterns` untuk melakukan routing
```shell
path('html/', show_html, name='show_html'),
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'),
# sesuaikan dengan nama fungsi yang dibuat di views.py
```
## Postman
HTML
XML
JSON


## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.
