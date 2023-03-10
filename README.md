# Linear Search

CARA KERJA PROGRAM
*user menginputkan data yang hendak dicari pada array
*setelah data dimasukkan maka akan menampilkan output berupa "(data) ditemukan pada index ..."
*contohnya ketika user menginputkan data "Avivah", maka akan menampilkan output: Avivah ditemukan di index 1
*kemudian pada bagian array yang disertai kolom, outputnya: Wibi ditemukan di index 3 kolom 1


FUNGSIONALITAS PROGRAM:
dapat digunakan untuk memudahkan kita mencari tau data yang dicari berada pada index ke berapa di dalam array


ALGORITMA YANG DIGUNAKAN:
Algoritma yang saya gunakan pada program ini, yaitu algoritma linear search 
linear search adalah algoritma yang digunakan untuk mencari nilai pada sebuah array dengan cara memeriksa satu per satu elemen dalam urutan, hingga elemen tersebut ditemukan atau seluruh elemen telah diperiksa.


ELEMEN YANG DIGUNAKAN PADA PROGRAM:
arr : array yang akan dicari elemennya. 
x : adalah elemen yang akan dicari dalam array.
for i in range(len(arr)): berfungsi melakukan loop di setiap elemen dalam array. 
if type(arr[i] == list: untuk memeriksa apakah elemen adalah sebuah array.
elif arr[i] == x: untuk memeriksa apakah elemen ini sama dengan elemen x yang dicari. 
return -1: jika elemen x tidak ada di array, maka fungsi mengembalikan nilai -1.
x1: parameter 1.
y: parameter 2.
search = linearsearch(x1,y): berfungsi memanggil fungsi linearsearch untuk mencari elemen y dalam array x1.
if search== -1:untuk melihat apakah elemen ditemukan di array x1.
array =["Arsel","Avivah","Daiva",[Wahyu", "Wibi"]].
While True: Perulangan. 
break: berhentiin perulangan.


