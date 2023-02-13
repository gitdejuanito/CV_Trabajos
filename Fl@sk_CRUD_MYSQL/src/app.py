from flask import Flask, redirect, url_for, render_template, request
import os 
import conexionSQL_local as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, "src", "templates")

app= Flask(__name__, template_folder= template_dir)

@app.route("/")
def index ():
    cursor = db.conexion.cursor()
    cursor.execute("SELECT* FROM customers" )
    myresult=cursor.fetchall()  ##se obtienen en tuplas

    insertObject=[] ##con lo siguiente se hace diccionario
    columnNames= [column[0] for column in cursor.description ]
    for record in myresult:
        insertObject.append(dict(zip(columnNames,record)))

    cursor.close()


    return render_template ("base.html", data=insertObject)

#agregar customers
@app.route("/customer", methods=["POST"])
def addCustomer():
    username= request.form["customerid"]
    first_name= request.form["first_name"]
    last_name= request.form["last_name"]
    birth_date=request.form["birth_date"]
    phone=request.form["phone"]
    address=request.form["address"]
    city=request.form["city"]
    state=request.form["state"]
    points=request.form["points"]


    if username and first_name and last_name and birth_date and phone and address and city and state and points:
        cursor=db.conexion.cursor()
        sql = "INSERT INTO customers (customer_id, first_name, last_name, birth_date, phone, address, city, state, points) VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data= (username, first_name, last_name, birth_date, phone,address, city, state, points)
        cursor.execute(sql,data)
        db.conexion.commit()
        return redirect(url_for("index"))


@app.route("/delete/<string:id>")
def delete(id):
        cursor=db.conexion.cursor()
        sql = "DELETE FROM customers WHERE customer_id=%s"
        data= (id,)
        cursor.execute(sql,data)
        db.conexion.commit()
        return redirect(url_for("index"))

@app.route("/update/<string:id>", methods=["POST"])
def update(id):
   
    first_name= request.form["first_name"]
    last_name= request.form["last_name"]
    birth_date=request.form["birth_date"]
    phone=request.form["phone"]
    address=request.form["address"]
    city=request.form["city"]
    state=request.form["state"]
    points=request.form["points"]

    if  first_name and last_name and birth_date and phone and address and city and state and points:
        cursor=db.conexion.cursor()
        sql = "UPDATE customers SET first_name=%s, last_name=%s, birth_date=%s, phone=%s, address=%s, city=%s, state=%s, points=%s  WHERE customer_id = %s"
        data= ( first_name, last_name, birth_date, phone,address, city, state, points, id)
        cursor.execute(sql,data)
        db.conexion.commit()
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True,port=8000)