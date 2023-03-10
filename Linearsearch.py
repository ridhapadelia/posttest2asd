def linearsearch(arr,x):
    for i in range(len(arr)):
        if type(arr[i]) == list:
            data = linearsearch(arr[i],x)
            if data == -1:
                return -1
            else:
                print(x, "ditemukan di indeks" ,i, "kolom" ,searchdata,)
                exit()
        elif arr[i] == x:
            return i
    return -1

def Linesearch(x1,y):
    search = linearsearch(x1,y)
    if search == -1:
        print(y," tidak ditemukan")
    else:
        print(y, "ditemukan di index", search)

Array = ["Arsel","Avivah","Daiva",["Wahyu","Wibi"]]

g = len(Array)
while True:
    elemen = input("Masukan data yang ingin dicari: ")
    Linesearch(Array,elemen)
    break
