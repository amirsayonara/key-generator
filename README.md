# Key Generator
[![License](https://img.shields.io/github/license/amirsayonara/key-generator)](LICENSE)
[![Twitter Follow](https://img.shields.io/twitter/follow/amir_sayonara)](https://twitter.com/amir_sayonara)

[Copyright (c) 2017 Amir Sayonara](LICENSE)

Menghasilkan key sesuai dengan keinginan kita

### Contoh Penggunaan
- Key default (bawaan program)
```
>>> Key()
GR54DQPXWC
```
- Key dengan validasi (menghasilkan key dengan jumlah karakter yang berada pada key pertama sebanyak 5)
```
>>> Key(validasi=True)
S6KSS7SOIS
```
- Key dengan format (menghasilkan key sesuai dengan format kita)
```
>>> Key(format='00AB')
30VE
>>> Key(format='00AA-BBBB-1111')
60RR-SRKG-2534
>>> Key(format='12345-ABCDE-67890')
12447-VTSWQ-20589
>>> Key(format='12345|AAAAA-BB-67')
98673|OQWTS-BD-00
```
- Key dengan format dan validasi (aturan sama dengan validasi sebelumnya, bedanya hanya di format, pastikan setidaknya mengandung 6 angka jika format key pertama adalah angka, begitu juga dengan huruf)
```
>>> Key(format='12345|AAAAA-BB-67', validasi=True)
92999|YRKUA-AE-98
>>> Key(format='0-AAAAA-BB-67', validasi=True)
Format salah, pastikan setidaknya mengandung 6 angka jika format key pertama adalah angka, begitu juga dengan huruf
>>> Key(format='0-AAAAA-BB-67-3333', validasi=True)
3-IGFTX-GL-33-3836
>>> Key(format='ABC-AAAAA-BB-00-000', validasi=True)
PPP-BMPQP-DO-19-587
```