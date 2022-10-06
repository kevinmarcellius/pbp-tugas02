[Tugas 4 PBP](#-tugas-4-pbp)<br>
[Tugas 5 PBP](#-tugas-5-pbp)

# Tugas 4 PBP

Kevin Marcellius Alrino<br>
2106706193<br>
[Link Aplikasi Heroku](https://pbp-tugas02-kevin.herokuapp.com/todolist)

## Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?

`{% csrf_token %}` berfungsi untuk mencegah serangan. Saat membuka suatu halaman `{% csrf_token %}` membuat suatu token di server-side dan memeriksa apakah request yang masuk memiliki token ini. Jika request yang masuk tidak memiliki token ini, maka request tersebut tidak akan dieksekusi. Jika tidak ada csrf tokeb maka webpage akan lebih rentan terhadap serangan.

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}` \)? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Bisa. Contohnya adalah yang saya gunakan pada `create-new-task.html`. Pada tag input, sertakan name yang akan berguna di `views.py`
```shell
<form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Title:</td>
                <td><input type="text" placeholder="Title" name="title" class="form-control"></td>
            </tr>
```
Lalu, pada views.py gunakan
`request.POST.get('title')` yang berguna untuk mengakses input yang sudah dimasukkan di field yang bernama `title`.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

User menekan tombol submit. Lalu, data yang dimasukkan user diakses dengan `request.POST.get(<input_name>)`. Lalu, di `views.py` buat task baru lalu save task tersebut. 
```shell
new_task = Task(user=user, title=title, description=description, date=date)
new_task.save()
```
setelah itu, pada fungsi `show_todolist` tambahkan variabel yang berfungsi untuk mengambil data yang diperlukan dari models.
```shell
todolist = Task.objects.filter(user=request.user)
```
Filter disini berfungsi untuk mengambil hanya task-task yang dibuat oleh user yang sedang login. Lalu masukkan variabel `todolist` ke context untuk ditampilkan di `todolist.html`.
```shell 
context = {
    'list_task': todolist,
    ....
```
Setelah itu, pada `todolist.html` gunakan for loop untuk menampilkan task yang ada di variabel `todolist`. 

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Buat django app baru menggunakan command `python manage.py startapp todolist`
2. Tambahkan `todolist` pada variabel `INSTALLED_APPS` di `project_django/settings.py`
3. Pada `todolist/models.py` buat class baru yang bernama Task dan buat field-field yang diperlukan. Setelah itu jalankan command `python manage.py makemigrations`dan `python manage.py migrate`
4. Tambahkan routing `path('todolist/', include('todolist.urls'))` pada `project_django/urls.py` 
5. Implementasikan fungsi `show_todolist` pada `todolist/views.py`
6. Buat file `create-new-task.html` pada folder templates sebagai halaman untuk membuat tugas baru. Pada file ini, buat form untuk menerima title dan description yang diinput oleh user.
7. Buat fungsi `create_new_task` pada `todolist/views.py` untuk mengambil data yang sudah diinput oleh user lalu buat task baru menggunakan data yang diinput oleh user.
8. Implementasikan login, register, dan logout. Implementasi yang saya gunakan untuk bagian ini sama dengan yang digunakan di Lab 3.
9. Pada `todolist/views.py`, implementasikan fungsi `delete_task` dan `update_status` yang berfungsi untuk menghapus task dan mengubah status task menjadi selesai atau belum selesai.
10. Pada `todolist.html` tambahkan elemen-elemen yang diperlukan, seperti table, tombol untuk logout, dan tombol untuk membuat task baru.
11. Pada `todolist/urls.py` buat routing yang diperlukan.
```shell
urlpatterns = [
    path('', show_todolist, name='show_todolist'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_new_task, name='create-new-task'),
    path('update-status/<int:pk>', update_status, name='update-status'),
    path('delete-task/<int:pk>', delete_task, name='delete-task'),
]
```

Akun:<br>
username: dummy1<br>
password: test@456<br>

username: dummy2<br>
password: test@123

# Tugas 5 PBP