import time
from plyer import notification

count = 0
lap = 0
workMin = 0
pauseMin = 0

print("Pomodoro çalışma zamanlayıcıya hoş geldiniz.")
lap = int(input("Kaç tur pomodoro yapmak istersiniz ? :"))
workMin = int(input("Her bir tur pomodoro kaç dakika olsun ? :"))
pauseMin = int(input("Her bir mola kaç dakika olsun ? :"))
while True:
    time.sleep(workMin)
    count += 1
    notification.notify(
        title = "Pomodoro Başladı , iyi çalışmalar",
        message = "Pomodoro Turu Başarıyla Tamamlandı. Tamamlanan Tur Sayısı :" + str(count) + " Şimdi Mola Vakti",

    )
    time.sleep(pauseMin)
    notification.notify(
        title = "Mola süresi doldu.",
        message = "Çalışmaya geri dön ! ",
    )
    if count == lap:
        notification.notify(
            title = "Başarıyla Tamamlandı",
            message = f"Belirttiğiniz tur miktarını {lap} tamamladınız.  ",
        ),
        break
