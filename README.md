Python To Do List Uygulaması Değişkenler ve Açıklamaları


self.master:  tkinter için ana pencere

self.todo_list: ToDoList sınıfının örneği yapılacak görevleri yönetiyor.

self.task_title_label: görev başlıklarını gösteren etiket.

self.task_title_entry: görevlerin giriş widgetı

self.task_details_entry: görevleri açıklamak için ekstra giriş

self.task_details_label: görevlerin ekstra açıklamasını girmeye yönlendiren etiket.

self.priority_label: görevlerin öncelik sırasının girilmesine yönlendiren etiket.

self.priority_entry: görevin öncelik sırasının giriş widgetı.

self.add-button: add task metodunu çalıştıran buton.

self.list_button: list task metodunu çalıştıran buton.

self.complete_button: complete task metodunu çalıştıran buton.

self.remove_button: remove task metodunu çalıştıran buton.

self.filename: görevleri bir JSON dosyasına kaydetmek için oluşturduğum dosya adı.

self.task: görevleri içeren bir sözlük. her görev title,details,priority ve completed anahtarına sahip.


Metodlar:


__init__(self,master): uygulamanın ana bileşenlerini çalıştıran metod

get_task_index(self): Kullanıcdan görevin indeksini alan metod geçersizse none döndürür.

list_tasks(self): To do list örneğinden görev listesini alır ve bunları messagebox da görüntüler.

complete_task(self): Girilen indekse göreve görevi tamamlanmış olarak işaretler.

remove_completed_task(self): Tamamlanmış görevleri listeden kaldırır.

add_task(self): yeni görev ekler

__init__(self,filename”todolist.json”): bir dosya adıyla todolist örneğini başlatır ve görevleri dosyadan yükler.

load_tasks(self): görevleri bir json dosyasından yükler dosya yoksa boş liste döndürür.

save_tasks(self,title,details,priority): yeni görevi listeye ekler



