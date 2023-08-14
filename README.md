# Screenshot Tool

## Açıklama
Bu, ekran görüntülerini belirtilen aralıklarla yakalayıp e-posta yoluyla gönderen Python tabanlı bir ekran görüntüsü aracıdır. Araç, aracı Windows makinelerinde kolayca kullanmak için kullanılan bir yürütülebilir (.exe) dosya oluşturma özelliğiyle birlikte gelir.

Araç ilk başta kullanıcıların mailine ekran görüntülerin gidip gitmediğini kontrol etmek için kullanıcı "Ctrl+C" kombinasyonuna basana kadar terminalde belirlenen maile screenshot gönderir. Eğer mail şifresinde veya adın da bir sıkıntı varsa aşağıda ki gibi hata verecektir:

![image](https://github.com/ugurcomptech/ScreenShotTool/assets/133202238/64e31928-ddf0-487e-acd9-cb3beb988f9b)

Eğer Mail yapılandırması doğru ise mailler başarılı olarak gönderilecektir:

![image](https://github.com/ugurcomptech/ScreenShotTool/assets/133202238/7c8106b4-c5c9-41fe-96ac-4e02510be0e6)

Kullanıcı "Ctrl+C" kombinasyonuna basınca deneme maillerinin gönderilmesi durdurulacak ve exe dosyası oluşacaktır.

![image](https://github.com/ugurcomptech/ScreenShotTool/assets/133202238/74d50aa4-1b2c-41d5-a489-34dc5ba02824)


**Not**: Bu araç potansiyel olarak kötü niyetli amaçlar için kullanılabilir. Yalnızca alıcının rızasıyla ve yasal amaçlar için sorumlu bir şekilde kullanınız.

## Özellikler
- Belirtilen aralıklarda ekran görüntüleri yakalar.
- Ekran görüntülerini e-posta yoluyla gönderir.
- Windows üzerinde kolay kullanım için yürütülebilir bir dosya oluşturur.

## Kullanım
1. Gereken bağımlılıkların yüklü olduğundan emin olmak için şunu çalıştırın:

  ```bash
  pip install -r requirements.txt
  ```

2. Komut satırı arayüzünde komutları düzenleyin.

3. Betiği çalıştırın:

  ```bash
  python screenshot_tool.py -s <sender_email> -p <sender_password> -r <receiver_email> -i <interval> -n <exe_name> -c <icon_path>
  ```

4. Betik ekran görüntülerini yakalayacak ve belirtilen aralıkta e-posta yoluyla gönderecektir.

## Argümanlar
- `-s, --sender-email`: Gönderenin e-posta adresi.
- `-p, --sender-password`: Gönderenin e-posta parolası.
- `-r, --receiver-email`: Alıcının e-posta adresi.
- `-i, --interval`: Ekran görüntüleri arasındaki aralık (saniye cinsinden).
- `-n, --exe-name`: Oluşturulan exe dosyasının adı.
- `-c, --icon-path`: Yürütülebilir dosya için simge dosyasının yolu.

## Sorumluluk Reddi
Geliştirici, bu aracın kötüye kullanımından veya neden olabileceği herhangi bir zarardan sorumlu değildir.  

## Lisans

[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

Bu projeyi [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) altında lisansladık. Lisansın tam açıklamasını [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) sayfasında bulabilirsiniz.
