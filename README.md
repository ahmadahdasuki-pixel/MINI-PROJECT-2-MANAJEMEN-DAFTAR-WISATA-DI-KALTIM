#MINI PROJECT 2 MANAJEMEN DAFTAR WISATA DI KALTIM

NAMA: AHMAD AHDASUKI

NIM: 2509116021

KELAS: A SISTEM INFORMASI

PRAKTIKUM DASAR-DASAR PEMOGRAMAN


**FLOWCHART**
<img width="1879" height="2120" alt="image" src="https://github.com/user-attachments/assets/63f60940-a82c-4afe-a086-fbe03051a111" />


**CODINGAN**

<img width="782" height="283" alt="image" src="https://github.com/user-attachments/assets/70244bab-7f9a-4005-80ec-b4591390f2c9" />

<img width="788" height="454" alt="image" src="https://github.com/user-attachments/assets/008bb790-a297-4157-888c-af2e9ff4db2a" />

<img width="687" height="489" alt="image" src="https://github.com/user-attachments/assets/99996302-e0b2-465f-914f-f5a864237810" />

<img width="781" height="551" alt="image" src="https://github.com/user-attachments/assets/3a481fc0-46a7-43ca-9cd1-2bf99e3dd123" />

<img width="666" height="357" alt="image" src="https://github.com/user-attachments/assets/44cc2c3e-a3bb-49a3-aca9-b2e343af6225" />

<img width="703" height="311" alt="image" src="https://github.com/user-attachments/assets/15fed203-ddc5-40aa-934e-8dee55d9b9e2" />




**OUTPUT DAN ERROR HANDLING**

**SISTEM LOGIN**

<img width="975" height="220" alt="image" src="https://github.com/user-attachments/assets/fe62168a-b237-44d1-b535-cb6b16f99b6d" />
Di output pertama ini program akan menampilkan sistem login dan kita login menggunakan username dan password sebagai manajer..


<img width="979" height="200" alt="image" src="https://github.com/user-attachments/assets/3a8229d7-b4ef-4528-a584-5f2e444690e2" />
lalu lanjut sistem login akan menginstruksikan untuk menginput password yang sudah kita buat di dictionary sebelumnya.




**MENU MANAJER**

<img width="970" height="290" alt="image" src="https://github.com/user-attachments/assets/3bf699b4-e852-4f20-9c33-0875d09d092a" />

Slanjutnya program akan menampilkan menu utama yang hanya bisa di akses oleh manajer.

<img width="563" height="581" alt="image" src="https://github.com/user-attachments/assets/c1e711fc-7919-4975-95b8-faf8307d6efc" />

ini adalah output pilihan 1 yaitu menampilkan daftar wisata yang sudah kita buat dictionary list wisatanya di program.

<img width="400" height="351" alt="image" src="https://github.com/user-attachments/assets/83e48ed8-3854-419a-a180-10a6ae1fb0d0" />

selanjutnya program akan terus berulang dan menampilkan menu utama yang hanya bisa di akses oleh manajer dan disini saya menginput pilihan 2 yaitu menambah daftar wisata,jadi saya menambah wisata baru,lokasi, dan harga tiket untuk wisata baru tersebut.ouput akan menampilkan data wisata baru berhasilkan di tambahkan.

**ValueError**
<img width="488" height="355" alt="image" src="https://github.com/user-attachments/assets/4d745fad-4783-4ecf-96e0-627d49f35971" />

Lalu saya menaruh Error Handling juga di output pilihan 2 ini jadi apabla saat menginput harga tiket inputnya kata atau kalimat maka "ValueError" akan muncul karena ada kesalahan dalam meninginputnya,karena disitu kita harus input angka. 

<img width="525" height="205" alt="image" src="https://github.com/user-attachments/assets/2248a730-ef13-4309-b15d-39dc42e1d09b" />

Di output pilihan 3 ini adalah mengubah data wisata atau update.kita akan input data wisata mana yang ingin di update data nya menjadi yang baru,jadi setelah kita memilih salah satu wisata yang ingin di update lalu kita akan meingnput lokasi dan harga tiket baru nyaa dan ouput akan menampilkan data wisata berhasl di perbarui.

**ValueError**
<img width="525" height="203" alt="image" src="https://github.com/user-attachments/assets/e3870c20-b142-492b-ac40-d6d5163b2333" />

Error Handling disini akan muncul karena saat menginput harga tiketnya harus berupa angka,soalnya di program tertulis int(input) yang berarti jika kita menginput kata atau kalimat maka "ValueError" akan muncul.

<img width="446" height="200" alt="image" src="https://github.com/user-attachments/assets/27630144-3567-4883-bdcf-f3341b18639c" />

Lnjut ke pilihan ke 4 yaitu Delete_wisata.kita akan memilih data wisata yang mana ingin di hapus dan input nama wisata yang di hapus maka output akan menampilkan wisata berhasil di hapus.

**KeyboardInterupt**
<img width="535" height="151" alt="image" src="https://github.com/user-attachments/assets/6d6ea4f4-5f9c-4da1-95bd-59b7aa35c4aa" />

Error Handling disini adalah "KeyboardINterupt" apabila saat ingin menginput data kita menekan CTRL+C maka erorhandling nya akan muncul.

<img width="501" height="158" alt="image" src="https://github.com/user-attachments/assets/e8935591-bece-4195-bc9e-ab4627566aa4" />

Ini output pilihan ke 5 yaitu keluar dari program dan program akan selesai.

**ELSE**
<img width="509" height="316" alt="image" src="https://github.com/user-attachments/assets/b3abfc4a-752b-412d-80d6-8ec8dfe25629" />

ini adalah output else apabila kita menginput menu di luar akses dari menu 1-5 sebagai manajer, maka akan muncul input tidak valid.

**MENU KARYAWAN**
<img width="677" height="207" alt="image" src="https://github.com/user-attachments/assets/abaeaa7d-1a55-4f4f-a20f-a8c94f7f7ff9" />

Lanjut berulang ke menu sistem login dan kali ini kita login sebagai karyawan yang akan menggunakan program tersebut lalu kita akan menginput username dan password sebagai karyawan.

<img width="357" height="439" alt="image" src="https://github.com/user-attachments/assets/59c5473f-61ac-4a1e-8454-23268544929d" />

Lanjut ke pilihan 1 satu kita sebagai karyawan yaitu menampilkan menu wisata untuk melihat daftar wisata yang sudah di buat di program dengan dictionary list wisata sebelumnya.

<img width="480" height="160" alt="image" src="https://github.com/user-attachments/assets/af212517-b6c7-48c9-92c4-188940fc2a25" />

Di output Pilihan ke 2 kita sebagai karyawan akan keluar dari program dan program selesai setelah kita melihat daftar wisata yang di buat di program tersebut.

**ELSE**
<img width="415" height="233" alt="image" src="https://github.com/user-attachments/assets/d7b55e75-b8c1-41fd-b1f3-3b6a06b8e2a2" />

ini adalah output else karena menginput di luar akses 1-2 dari pilihan menu sebagai karyawan,maka akan muncul input tidak valid.



















  







