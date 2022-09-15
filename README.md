# Tugas 2 PBP
Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

Link aplikasi heroku: https://pbp-tugas02-kevin.herokuapp.com/katalog/

## Bagan

![MVTarchitecture](https://user-images.githubusercontent.com/112237431/190309693-03b61353-1a48-4c99-bdc4-dd3f89b95fa9.jpg)
![controlflowMVT](https://user-images.githubusercontent.com/112237431/190309713-2f29ae50-f3d9-4de9-b7eb-3077f587d092.jpg)
Sumber: https://techvidvan.com/tutorials/djangos-mvt-architecture/?amp=1

## Hubungan urls.py, models.py, views.py, dengan katalog.html
Ketika ada request dari user yang masuk ke  `urls` akan dilakukan parse argument, lalu dilakukan routing untuk meneruskan argument ke `views` yang terkait, lalu views akan meminta value dari `models`, lalu models akan mengambil value dari database dan mengembalikan value ke `views`. `views` akan menggabungkan `template/katalog.html` dengan value yang sudah didapat dari `models`.

## Implementasi poin 1 sampai 4:
1. Pada `katalog/views.py`, buat fungsi yang menerima parameter `request` dan mengembalikan `render(request, "katalog.html", context)` dan dalam fungsi tersebut tambahkan potongan kode yang berfungsi untuk memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel.
```shell
   def show_catalog(request):
        return render(request, "katalog.html", context)
    data_katalog = CatalogItem.objects.all()
    context = {
    'list_item': data_katalog,
    'name': 'Kevin Marcellius Alrino',
    'student_id': '2106706193'
    }
   ```
2. Pada `katalog/urls.py`, tambahkan kode berikut untuk melakukan routing terhadap fungsi views yang telah dibuat sehingga nantinya halaman HTML dapat ditampilkan lewat browser.
```shell
from django.urls import path
from katalog.views import show_catalog

app_name = 'katalog'

urlpatterns = [
    path('', show_catalog, name='show_catalog'), 
    # sesuaikan dengan nama fungsi yang dibuat di katalog/views.py
]
```
Daftarkan juga aplikasi `katalog` ke dalam `project_django/urls.py` dengan menambahkan potongan kode berikut pada variabel urlpatterns.
```shell
...
path('katalog/', include('katalog.urls')),
...
```
3. Pada `templates/katalog.html` buat sebuah for loop untuk menambahkan daftar barang ke dalam tabel
```shell
...
    {% for item in list_item %}
    <tr>
        <th>{{item.item_name}}</th>
        <th>{{item.item_price}}</th>
        <th>{{item.item_stock}}</th>
        <th>{{item.rating}}</th>
        <th>{{item.description}}</th>
        <th>{{item.item_url}}</th>
    </tr>
{% endfor %}
...
```
4. Untuk melakukan deployment, buka konfigurasi repositori GitHub dan buka bagian Secrets untuk GitHub Actions (`Settings -> Secrets -> Actions`). Tambahkan variabel repository secret baru untuk melakukan deployment. Pasangan Name-Valuenya adalah sebagai berikut.
```shell
(NAME)HEROKU_APP_NAME
(VALUE)<NAMA_APLIKASI_HEROKU_YANG_SUDAH_DIBUAT>
```
```shell
(NAME)HEROKU_API_KEY
(VALUE)<VALUE_API_KEY>
```
`<VALUE_API_KEY>` didapat dari `Account Settings -> API Key` pada `https://dashboard.heroku.com/`
## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.
