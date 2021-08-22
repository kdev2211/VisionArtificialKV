import tkinter as tk
import re 
from tkinter import ttk
from tkinter import *
import pymysql
import cv2
import pytesseract
import pymysql
from datetime import date, datetime
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

class DataBase:
  
    connection=pymysql.connect(
            host='localhost',
            user='root',
            password='Cris.2211',
            db='registro_matricula'
        )
    cursor = connection.cursor()
    print("Conexion Exitosa!!!")

    def insert_reporte(self,desc, tipo, plate):

        self.cursor = self.connection.cursor()

        sql1="select * from registro_vehiculos where num_matricula='{}';".format(plate)
        try:
            
            self.cursor.execute(sql1)
            plate1=self.cursor.fetchone()
      
            print (plate1)
            print("--------------")

     

            if (plate1 != None):

                sql="insert into registro_reportes(descripcion, tipo, matricula_vehiculo) values('{}','{}','{}');".format(desc,tipo,plate)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print(self.cursor.rowcount, "Record inserted successfully into table")
                    self.cursor.close()
                    print (desc)
                    print (tipo)
                    print (sql)
                except Exception as e:
                    raise          
            else:         
                print ("Esta placa no se encuentra registrada en el sistema") 
        except Exception as e:
            raise 
       



    def insert_placa(self,num, prop, marca, modelo):

        self.cursor = self.connection.cursor()

   
        sql="insert into registro_vehiculos(num_matricula, propietario, marca, modelo) values('{}','{}','{}','{}');".format(num,prop,marca, modelo)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(self.cursor.rowcount, "Record inserted successfully into table")
            self.cursor.close()
     
        except Exception as e:
            raise

    def insert_tasa_peaje(self,num, monto, fecha):

        self.cursor = self.connection.cursor()

        sql1="select * from tasa_peaje where matricula_vehiculo='{}';".format(num)
        try:
            
            self.cursor.execute(sql1)
            plate1=self.cursor.fetchone()


            

            if (plate1):

                date = datetime.strptime(plate1[3], '%Y, %m, %d')

                TODAY = datetime.today()
                sTODAY = TODAY.strftime("%Y, %m, %d")

                DTODAY = datetime.strptime(sTODAY, '%Y, %m, %d')
               

                delta = DTODAY - date
            
                if delta.days > 30:
                    cv2.putText(image,"FACTURAS VENCIDAS",(x-250,y-220),1,2.2,(0,0,255),2)

                    sqlF="insert into registro_reportes(descripcion, tipo, matricula_vehiculo) values('{}','{}','{}');".format("Mora en pago de credito de peaje","6",num)
                    try:
                        self.cursor.execute(sqlF)
                        self.connection.commit()
                        print(self.cursor.rowcount, "Record inserted successfully into table")
                  
                        print (sqlF)
                    except Exception as e:
                        raise                         

                else:
                    return False    

                añadido = plate1[2] + monto
                sql="update tasa_peaje set monto = '{}' WHERE id_peaje = '{}';".format(añadido, plate1[0])

                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print (sql)
              
                    self.cursor.close()
                except Exception as e:
                    raise

            else: 
                sql="insert into tasa_peaje(matricula_vehiculo, monto, fecha) values('{}','{}','{}');".format(num,monto,fecha)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print(self.cursor.rowcount, "---- COBRO DE PEAJE ----")
                    self.cursor.close()


                except Exception as e:
                    raise




        except Exception as e:
            raise




    def get_placa(self,placa):
        sql="select * from registro_vehiculos where num_matricula='{}';".format(placa)
        try:
    
            self.cursor.execute(sql)
            plate=self.cursor.fetchone()

            print ("REGISTROS:", plate)
            print("--------------")

          

            if (plate != None):
                cv2.putText(image,"PLACA REGISTRADA",(x-250,y-300),1,2.2,(0,255,0),2)
            else:    
                cv2.putText(image,"PLACA SIN REGISTRAR",(x-250,y-300),1,2.2,(0,255,0),2)
       
            
        except Exception as e:
            raise 

    def get_reporte(self,placa):

        sql1="select * from registro_vehiculos where num_matricula='{}';".format(placa)
        try:
            
            self.cursor.execute(sql1)
            plate1=self.cursor.fetchone()
      
            print (plate1)
            print("--------------")

     

            if (plate1 != None):

                sql="select descripcion, matricula_vehiculo, tipo_reportes.tipo from registro_reportes, tipo_reportes WHERE registro_reportes.tipo=tipo_reportes.id_tipo and matricula_vehiculo='{}';".format(placa)
                try:
            
                    self.cursor.execute(sql)
                    plates=self.cursor.fetchone()
                
                    print ("REPORTES:", plates)
                    print("--------------")

                

                    if (plates != None):
                        cv2.putText(image,"VEHICULO CON REPORTE",(x-250,y-260),1,2.2,(0,0,255),3)
                    else:    
                        return False
                except Exception as e:
                    raise 

            else:         
                print ("Esta placa no se encuentra registrada en el sistema") 
        except Exception as e:
            raise 


database = DataBase()


#INTERFAZ DE USUARIO       
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):

        master.geometry('250x350')
        master.resizable(0, 0)
        master.title('PLATE')
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text="REGISTRO DE PLACAS", background = 'black', foreground ="white", anchor='center',font = ("Times New Roman", 12), ).pack(side="top", fill="x", pady=10)


        ttk.Label(self, text = "PLACA: "+ numeracion, anchor='center',
            font = ("Times New Roman", 10)).pack(side="top", fill="x")


      
        tk.Button(self, text="FORMULARIO DE MATRICULAS",
                  command=lambda: master.switch_frame(PageOne)).pack(pady=10, fill="x")
        tk.Button(self, text="REGISTRAR UN REPORTE", 
                  command=lambda: master.switch_frame(PageTwo)).pack(pady=10, fill="x")

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="FORMULARIO DE MATRICULA", background = 'black', foreground ="white", anchor='center',font = ("Times New Roman", 12), ).pack(side="top", fill="x", pady=10)
#LABEL PROPIETARIO
        ttk.Label(self, text = "PROPIETARIO: ",
                font = ("Times New Roman", 10)).pack(side="top", fill="x", pady=5)


        # ENTRY PROPIETARIO

        entryPropietario = Entry(self)
        entryPropietario.pack(pady=10)

#LABEL MARCA
        ttk.Label(self, text = "MARCA: ",
                font = ("Times New Roman", 10)).pack(side="top", fill="x", pady=5)


          # ENTRY MARCA

        entryMarca = Entry(self)
        entryMarca.pack(pady=10)


#LABEL MODELO
        ttk.Label(self, text = "MODELO: ",
                font = ("Times New Roman", 10)).pack(side="top", fill="x")


          # ENTRY MODELO

        entryModelo = Entry(self)
        entryModelo.pack(pady=10)

#LABEL IDENTIDAD
        ttk.Label(self, text = "IDENTIDAD: ",
                font = ("Times New Roman", 10)).pack(side="top", fill="x")


          # ENTRY IDENTIDAD

        entryIdentidad = Entry(self)
        entryIdentidad.pack(pady=10)


        def buttonCallBack():

            
            inputPropietario = entryPropietario.get()
            inputMarca = entryMarca.get()
            inputModelo = entryModelo.get()
            inputIdentidad = entryIdentidad.get() 

            print (inputPropietario)
            print (inputMarca)
            print (inputModelo)
            print (inputIdentidad)
            print (numeracion)

            if inputPropietario =="":
                print("PORFAVOR LLENE TODOS LOS CAMPOS")

            elif inputMarca =="":
                print("PORFAVOR LLENE TODOS LOS CAMPOS")

            elif inputModelo =="":
                print("PORFAVOR LLENE TODOS LOS CAMPOS")

          
            elif inputIdentidad =="":
                print("PORFAVOR LLENE TODOS LOS CAMPOS")
            else:

                database.insert_placa(numeracion, inputPropietario, inputMarca, inputModelo)
                
                entryMarca.delete(0, 'end')
                entryPropietario.delete(0, 'end')
                entryModelo.delete(0, 'end')
                entryIdentidad.delete(0, 'end')

            

        tk.Button(self, text="VOLVER",
                  command=lambda: master.switch_frame(StartPage)).pack(side=LEFT, pady=10, padx=30)
        tk.Button(self, text ="SUBMIT", command = buttonCallBack).pack(side=RIGHT, pady=10, padx=30)



class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="FORMULARIO DE REPORTES", background = 'black', foreground ="white", anchor='center',font = ("Times New Roman", 12), ).pack(side="top", fill="x", pady=10)

        ttk.Label(self, text = "Tipo de reporte: ",
                font = ("Times New Roman", 10)).pack(side="top", fill="x", pady=10)

        # Combobox creation
        n = tk.StringVar()
        monthchoosen = ttk.Combobox(self, width = 27, textvariable = n)
        
        # Adding combobox drop down list
        reportes_lista = ["ESCOJA UNA OPCION", "INFRACCION","ROBO","DEFECTOS DE FABRICA","KILOMETRAJE","RIESGO VIAL"]

        #COMBOBOX        
   
        reportDropdown = ttk.Combobox(self, values = reportes_lista)
        reportDropdown.current(0)
        reportDropdown.pack(side="top", fill="x", pady=1)


        #TEXT BOX DESCRIPCION

        text_box = Text(
            self,
            height=5,
            width=20
        )
        text_box.pack(side="top", fill="x", pady=1)

        def buttonCallBack():
            print (reportDropdown.current())
            inputTipo = (reportDropdown.current())
            inputDescripcion = text_box.get(1.0,'end-1c')
            print (inputDescripcion)
            print (numeracion)
            
            database.insert_reporte(inputDescripcion, inputTipo, numeracion)  

         

        tk.Button(self, text="VOLVER",
                  command=lambda: master.switch_frame(StartPage)).pack(side=LEFT, pady=10)
        tk.Button(self, text ="SUBMIT", command = buttonCallBack).pack(side=RIGHT,pady=10)



placa = []

image = cv2.imread('Placas.jfif')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray,(3,3))
canny = cv2.Canny(gray,150,200)
canny = cv2.dilate(canny,None,iterations=1)

#_,cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(image,cnts,-1,(0,255,0),2)

for c in cnts:
  area = cv2.contourArea(c)

  x,y,w,h = cv2.boundingRect(c)
  epsilon = 0.09*cv2.arcLength(c,True)
  approx = cv2.approxPolyDP(c,epsilon,True)
  
  if len(approx)==4 and area>9000:
    print('area=',area)
    #cv2.drawContours(image,[approx],0,(0,255,0),3)

    aspect_ratio = float(w)/h
    if aspect_ratio>2.4:
      placa = gray[y:y+h,x:x+w]
      text = pytesseract.image_to_string(placa,config='--psm 11')
      

  
      new_string = re.sub(r"[^a-zA-Z0-9]"," ",text)
      print('PLACA: ',new_string)
      numeracion = " ".join(new_string.split())

      today = datetime.today()
      fecha = today.strftime("%Y, %m, %d")

      print (fecha)
      database.get_placa(numeracion)
      database.get_reporte(numeracion)
      database.insert_tasa_peaje(numeracion, 50, fecha)
 
    
      

      cv2.imshow('PLACA',placa)
      cv2.moveWindow('PLACA',780,10)
      cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
      cv2.putText(image,text,(x-20,y-10),1,2.2,(0,255,0),3)
   


      
cv2.imshow('Image',image)
cv2.moveWindow('Image',45,10)
cv2.waitKey(0)        

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()