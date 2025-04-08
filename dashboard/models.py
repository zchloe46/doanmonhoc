from django.db import models

# bang van_ban de luu tru cac van ban da duoc nhap vao
class VanBan(models.Model):
    idVB = models.AutoField(primary_key=True)
    time = models.DateField(auto_now_add=True) 
    content = models.TextField()

    def __str__(self):
        return f"VanBan {self.idVB} - {self.time}"

    class Meta:
        db_table = 'van_ban'

# bang tach_tu de luu tru ket qua phan tich tu
class TachTu(models.Model):
    idVB = models.ForeignKey(VanBan, on_delete=models.CASCADE, to_field='idVB', db_column='idVB')
    resultTachtu = models.TextField()

    def __str__(self):
        return f"TachTu for VanBan {self.idVB.idVB}"

    class Meta:
        db_table = 'tach_tu'

# bang gan_nhan de luu tru ket qua gan nhan tu loai
class GanNhan(models.Model):
    idVB = models.ForeignKey(VanBan, on_delete=models.CASCADE, to_field='idVB', db_column='idVB')
    resultGannhan = models.TextField()
    def __str__(self):
        return f"GanNhan for VanBan {self.idVB.idVB}"

    class Meta:
        db_table = 'gan_nhan'

# bang phan_loai de luu tru ket qua phan loai van ban
class PhanLoai(models.Model):
    idVB = models.ForeignKey(VanBan, on_delete=models.CASCADE, to_field='idVB', db_column='idVB')  
    resultPhanloai = models.TextField()

    def __str__(self):
        return f"PhanLoai for VanBan {self.idVB.idVB}"

    class Meta:
        db_table = 'phan_loai'

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