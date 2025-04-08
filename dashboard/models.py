from django.db import models

# bang contact de luu tru thong tin lien he
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'contact'

class Test(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateField(auto_now_add=True)
    content = models.TextField()
    resultTachTu = models.TextField()
    resultGanNhan = models.TextField()
    resultPhanLoai = models.TextField()

    def __str__(self):
        return f"Test {self.id} - {self.time}"

    class Meta:
        db_table = 'vanban'