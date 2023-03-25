from flask import *
import mysql.connector
app=Flask(__name__)

@app.route("/")
def hello():
    return render_template("about.html")
    




@app.route("/loginform")
def loginform():
    return(render_template("loginform.html"))


@app.route("/entry",methods=['POST','GET'])
def entry():
   try:
       
        a=request.form['user']
        b=request.form['password']
        d=request.form['database']
        e=request.form['table']
        mydb=mysql.connector.connect(host="localhost",user=a,passwd=b,database=d)
        mycursor=mydb.cursor()
        mycursor.execute("show tables")
        tab=mycursor.fetchall()
        mycursor.execute("show databases")
        db=mycursor.fetchall()
        #e=request.form['table']
        mycursor.execute("desc {}".format(e))
    
        myre=mycursor.fetchall()
        mycursor.execute("select * from {}".format(e))
        myre1=mycursor.fetchall()
        return render_template("display.html",my=myre,my1=myre1,c=len(myre),tab=tab,db=db)
   except TypeError:
       
       
       print("enter valid deatils of your database")

   
@app.route("/display")
def display():
    
    mycurs=request.args['mycurs']        
    return render_template("disp",mycurso=mycurs)

app.run(debug=True)
