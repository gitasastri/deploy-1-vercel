#ada dua package 
#fastapi -> membuat api 
#uvicorn -> menjalankan api/server

from fastapi import FastAPI, Request, Response 
import pandas as pd 

#membuat object FastAPI
app = FastAPI()



# mendaftarkan endpoint/API
# @app.get("/") #get adalah methodnya, / adalah url dari halaman utama 
# def getHome(): #function untuk mengambil dari halaman utama 
#     #return berupa Json yg mirip dict python
#     return {
#         "message": "Ini halaman utama"
#         }

#API PART 2 CREATE HEADER
@app.get("/") 
def getHome(request: Request, response: Response):  
    #melihat isi headers dari request
    headers = request.headers 

    #membuat response 
    response = Response("Ini halaman utama")

    #return json data
    return {
        "req-headers" : headers,
        "response-headers" : response.headers,
        "respon-body" : response.body
    }
#JANGAN LUPA KOMA

@app.get("/hello") #get adalah methodnya, / adalah url dari halaman utama 
def getHello(): #function untuk mengambil dari halaman utama 
    #return berupa Json yg mirip dict python
    return {
        "message": "Hello World"
        }

#contoh lain
#integrasi dengan dataframe 
df = pd.DataFrame({
    "names" : ['Yuda', 'Yudi', 'Yadi'],
    "location": ['Jakarta', 'Bandung', 'Surabaya']
})
#mau kita tampilin di API, buat lg endpoint


# @app.get("/see-all") #endpoint untuk melihat seluruh data dari df
# def getSeeAll(): #function untuk 
#     #return berupa Json yg mirip dict python
#     return df.to_dict

#hasilnya, 
# column : {index:value}

# {
#   "names": {
#     "0": "Yuda",
#     "1": "Yudi",
#     "2": "Yadi"
#   },
#   "location": {
#     "0": "Jakarta",
#     "1": "Bandung",
#     "2": "Surabayar"
#   }
# }

#hasil lain, 
#pake orient parameter = records 
#expct 
# {column:value},
# {column:value},
# {column:value}

# @app.get("/see-all") #endpoint untuk melihat seluruh data dari df
# def getSeeAll(): #function untuk 
#     #return berupa Json yg mirip dict python
#     return df.to_dict(orient='records')

#save aja nanti running sendiri di terminalnya

#cari sesuai nama dari url 
@app.get('/names/{name}') #endpoint untuk melihat seluruh data dari df
def findName(name): 
    #filter df
    result = df[df['names'] == name] #hasilnya ditampung di variabel result
    #df['names'] ini harus nama kolom

        #jika ada data = tampilkan 
    #jika no data = error 404
    if len(result) == 0:
        raise HTTPException(status_code=404, detail= "Data Tidak Ditemukan")
    else: 
        return result.to_dict(orient='records')








