from flask import Flask , request , redirect , render_template , session
from flask_mysqldb import MySQL
from datetime import datetime 
from mail import msgs



app=Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'localhost'
app.config['MYSQL_PASSWORD'] = 'Chaitra@123'
app.config['MYSQL_DB'] = 'Hos'
mysql = MySQL(app)

app.secret_key = "super secret key"

@app.route('/',methods=['GET','POST'])
def index():
	return render_template("home.html")

@app.route('/apply',methods=['GET','POST'])
def apply():
	# return render_template("home1.html")
	if  'email' in session:
		return render_template("home1.html")
	else:
		return render_template("login.html")

@app.route('/opd',methods=["GET","POST"])
def opd():
	return render_template("home3.html")

@app.route('/checkup')
def checkup():
	return render_template("home2.html")

@app.route('/info')
def info():
	return render_template("home4.html")

@app.route('/a',methods=["GET","POST"])
def home2():
	if request.method == "POST":
		drname=request.form['drname']
		print(drname)
		return render_template("home4.html",drname=drname)



@app.route('/detail',methods=["GET","POST"])
def home4():
	if request.method == "POST":
		drname=request.form['drname']
		name=request.form['name']
		addr=request.form['addr']
		date=request.form['date']
		gender=request.form['gender']
		age=request.form['age']
		weight=request.form['weight']

		str=None
		flag1=False

		email="chaitra@gmail.com"

		cur=mysql.connection.cursor()

		# now2 = datetime.now()
		# now1 = now2.strftime('%Y-%m-%d ')
		# date1 = date.strftime('%Y-%m-%d ')
		# val = date1 - now1
		# print(val)
		# if val>2 or val<0:
		# 	str="Invalid date"
		# 	return render_template("home4.html",str=str,flag1=True)

		cur.execute("INSERT INTO appointment(name,ref_id,address,con_Dr,a_date,sex,age,weight) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",(name,email,addr,drname,date,gender,age,weight))
		mysql.connection.commit()
		cur.close()
		msgs()
	return render_template("home.html")

@app.route('/register',methods=['GET','POST'])
def register():
	return render_template("register.html")
	
@app.route('/sreg',methods=["GET","POST"])
def sreg():
	if request.method == "POST":
		fullname=request.form['name']
		email=request.form['email']
		password=request.form['password']
		conpassword=request.form['conpassword']
		data=None
		str1=None
		str2=None
		flag1=False
		flag2=False

		cur=mysql.connection.cursor()
		cur.execute("SELECT email FROM customer WHERE email=%s",(email,))
		data=cur.fetchone()
		#cur.close()
		# if data == None:
		# 	print("Data none:",data)
		#print("Data is none:",data)
		if(data != None):
			str1="Email is already used."
			print("Data:",data)
			return render_template("register.html",str1=str1, flag1=True)

		if(password != conpassword):
			print("not matching")
			str2="password is not matching."
			return render_template("register.html",str2=str2, flag2=True)

		#password= hashlib.md5(password.encode())
		password=password.encode('utf-8')

		cur.execute("INSERT INTO customer(fullname, email,password) VALUES (%s, %s, %s)",(fullname,email, password))
		mysql.connection.commit()
		session['email']=email
		cur.close()
		return render_template("login.html")
	return 'DataBase error!!'

@app.route('/apply/slog',methods=["GET","POST"])
def slog():
	if request.method == "POST":
		email=request.form['email']
		password = request.form['password']
		flag1=False

		#password= hashlib.md5(password.encode())
		print(password)


		cur=mysql.connection.cursor()
		cur.execute("SELECT email,password FROM customer WHERE email=%s and password=%s",(email,password,) )
		data=cur.fetchone()
		
		if data != None:
			session['email']=email
			return render_template("home1.html")
		else:
			str1="wrong emailid or password."
	return render_template("login.html",str1=str1,flag1=True)



if __name__ == '__main__':
	app.run(debug=True,port=5000)