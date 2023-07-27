from django.db import models
from django.utils import timezone
import random

# Create your models here.
class GuessNumbers(models.Model):
    name = models.CharField(max_length=24)  # 로또 번호 리스트의 이름
    text = models.CharField(max_length=255)  # 로또 번호 리스트에 대한 설명
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]')  # 로또 번호들이 담길 str
    num_lotto = models.IntegerField(default=5)  # 6개 번호 set의 개수
    update_date = models.DateTimeField()

    def generate(self):  # 로또 번호를 자동으로 생성
        self.lottos = ""
        origin = list(range(1, 46))  # 1~45의 숫자 리스트
        # 6개의 번호를 set 개수만큼 뒤섞은 후 앞의 6개를 골라내어 sorting
        for _ in range(0, self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) + '\n'
        self.update_date = timezone.now()  # settings의 TIME_ZONE에 해당하는 시간대가 입력됨
        self.save()  # GuessNumbers object를 DB에 저장

    def __str__(self):  # Admin page에서 display되는 텍스트에 대한 변경
        return f"pk {self.pk} : {self.name} - {self.text}"
