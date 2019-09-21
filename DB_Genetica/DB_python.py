import mysql.connector

#######################################
# Establecer la conexion
#######################################
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="genoma123",
  port = '3306'
  #database = "DB"
)

mycursor = mydb.cursor()
#######################################
#Mostrar bases de datos
#######################################
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

#Para eliminar una base de datos similar si existe, y poder trabajar bien
mycursor.execute("DROP DATABASE IF EXISTS QTL_Genetica")
mycursor.execute("CREATE DATABASE QTL_Genetica")

mydb = mysql.connector.connect(
	host="localhost",
	user="user",
	passwd="genoma123",
	port='3306',
	database="QTL_Genetica"
)

mycursor2=mydb.cursor()

mycursor2.execute("SHOW DATABASES")
#Imprimir
for x in mycursor2:
  print(x)

# Crear tablas
mycursor2.execute("CREATE TABLE Person (person_id INT AUTO_INCREMENT, constraint person_id_pk PRIMARY KEY(person_id), name VARCHAR(255), sex ENUM('M','H'), age INT(3), state VARCHAR(20))")
mycursor2.execute("CREATE TABLE Mediciones (med_id INT AUTO_INCREMENT PRIMARY KEY, type VARCHAR(255), value FLOAT(6,3), person_id INT, constraint person_id_fk foreign key(person_id) references Person(person_id) on update restrict)")

#Mostrar las tablas
mycursor2.execute("SHOW TABLES")
for x in mycursor2:
  print(x)

#Llenar las tablas
import pandas as pd
import math
data = pd.read_csv('Mediciones.csv') #Se carga los datos del archivo csv a una variable, quitando a Mario y la variable Día

#Se carga la tabla Person
sql="INSERT INTO Person (name, sex, age, state) VALUES (%s, %s, %s, %s)"
for i in range(0,data.shape[0]):#for i in range(0,data.shape[0]): número de filas con shape[0], número de columnas con shape[1] 
	val=[data.iloc[i,0],]
	val.append(data.iloc[i,1])
	val.append((data.iloc[i,2]).item())
	val.append(data.iloc[i,3])
	val=tuple(val)
	mycursor2.execute(sql, val)

#Cargar la tabla Mediciones
sql="INSERT INTO Mediciones (type,value,person_id) VALUES (%s, %s, %s)"
for i in range(0,data.shape[0]):
	for j in range(4,data.shape[1]):
		if(j==4):
			val=['Altura',]
		elif(j>=5 and j<=9):
			val=['Frente',]
		elif(j==10):
			val=['Frente Promedio',]
		elif(j>=11 and j<=15):
			val=['Brazo',]
		elif(j==16):
			val=['Brazo Promedio',]
		elif(j==17):
			val=['Pie',]
		elif(j==18):
			val=['Presión sistólica',]
		elif(j==19):
			val=['Presión diastólica',]
		val.append((data.iloc[i,j]).item())
		val.append(i+1)
		val=tuple(val)
		mycursor2.execute(sql, val)

#Commit
mydb.commit()
