from django.db import models


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