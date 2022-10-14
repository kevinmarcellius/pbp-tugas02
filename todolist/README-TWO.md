# Tugas 6 PBP
[Link Aplikasi Heroku](https://pbp-tugas02-kevin.herokuapp.com/todolist)

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asynchronous programming:<br>
Asynchronous programming digunakan karena bisa terjadi lag saat function mengambil data dari API. Dengan asynchronous programming, pengguna tidak perlu menunggu suatu proses selesai dan bisa melakukan aktivitas lain di web tersebut, misal pindah ke halaman lain. Sehingga bisa ada lebih dari 1 proses yang berjalan secara bersamaan.<br>
Synchronous programming:<br>
Kebalikan dari asynchronous programming, synchronous programming bersifat sequential. Hanya ada 1 proses yang bisa dijalankan dalam waktu yang sama sehingga waktu menjalankan program lebih lambat.
## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming adalah suatu paradigma dimana alur dijalankannya program mengikuti event-event tertentu, misalnya hal-hal yang dilakukan user, seperti click button. Contoh pada tugas ini, yaitu pada saat menambahkan task, digunakan event listener pada tombol "Create"

## Jelaskan penerapan asynchronous programming pada AJAX.
1. Tambahkan code berikut pada header file html.
```shell
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
 ```
2. Tambahkan `<script>` ke dalam header.<br>
3. Dalam `<script>` tambahkan syntax jQuery yang diperlukan seperti $.ajax() POST, DELETE, dll.<br>
4. AJAX akan bertindak sebagai event listener dan akan menjalankan perintah sesuai event.<br>
5. Data akan berubah tanpa harus reload page.<br>
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Tambahkan code berikut pada header `base.html`.
```shell
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
 ```
2. Pada `todolist/views.py` tambahkan function berikut.
```shell

@login_required(login_url='/todolist/login')
def show_json(request):

    tasks = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", tasks), content_type="application/json")

@csrf_exempt
@login_required(login_url="/todolist/login/")
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.today()
        user = request.user
        new_task = Task(user=user, title=title, description=description, date=date)
        new_task.save()
        return JsonResponse(
            {
            "title": title,
            "date": date,
            "description": description,
            "is_finished": False,
        }, status=200)
```
3. Pada `todolist/urls.py` tambahkan path berikut.
```shell
    path('json/', show_json, name='show_json'),
    path('add/', add_task, name='add_task'),
```
4. Buat modal baru pada `todolist.html`<br>
```shell
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Create New Task</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form id="form_todolist" action = "/todolist/add/">
            {% csrf_token%}
          <div class="mb-3">
            <label for="title" class="col-form-label">Title:</label>
            <input type="text" class="form-control" id="title">
          </div>
          <div class="mb-3">
            <label for="description" class="col-form-label">Description:</label>
            <textarea class="form-control" id="description"></textarea>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="submit" value="submit" class="btn btn-primary" id="submit_btn">Create</button>
          </div>
        </form>
      </div>

    </div>
  </div>
</div>
```
5. Pada `todolist.html`, tambahkan fungsi GET dan POST dan listener<br>
```shell
       $(document).ready(function(){
            $.getJSON("{% url 'todolist:show_json' %}", function(task){
                $.each(task, function(index,value){
                console.log(value)
                    $("#todolist_container").append(
                    `<div class="col-12 col-md-6 col-lg-4">
                            <div class="card">
                                <h5 class="card-title">${value.fields.title}</h5>
                                <p class="card-text">${value.fields.date}.</p>
                                <p class="card-text">${value.fields.description}.</p>
                                <p class="card-text">Finished : ${value.fields.is_finished}.</p>
                            </div>
                        
                            </div>`    
                    )
                })
        })
        $("#form_todolist").on("submit",function(e) {
        e.preventDefault() 
        let date = $("#date").val();
        let title = $("#title").val();
        let description = $("#description").val();
        $.ajax({
          method: "POST",
          url: "/todolist/add/",
          data: {"date":date, "title":title, "description":description},
        }).done(function(resp) {
          console.log(resp)
          $("#todolist_container").append(
            `<div class="col-12 col-md-6 col-lg-4">
                            <div class="card">

                                <h5 class="card-title">${resp.title}</h5>
                                <p class="card-text">${resp.date}.</p>
                                <p class="card-text">${resp.description}.</p>
                                <p class="card-text">Finished : ${resp.is_finished}.</p>
                            </div>
                        </div>`    
          )
          $("#exampleModal").modal("toggle")
        });
    })
    })


```