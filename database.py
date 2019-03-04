import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin2112>",
    database="companydb"
)

my_cursor = mydb.cursor()

#Create a Database
my_cursor.execute("CREATE DATABASE companydb")

# Create Customer Table
my_cursor.execute("CREATE TABLE customer (uid INTEGER AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(255), lastname VARCHAR(255), birth_date VARCHAR(20), age INTEGER, gender VARCHAR(10), occupation VARCHAR(255), city VARCHAR(40), country VARCHAR(30), username VARCHAR(255), email VARCHAR(60), password CHAR(32), phone VARCHAR(30))")

sqlStuff= "INSERT INTO customer(firstname, lastname, birth_date, age, gender, occupation, city, country, username, email, password, phone) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
record1= [("Marylynne","Postians","12/Apr/1991",28,"Female","Doctor","Coventry", "England","Marns22","mpostians1w@gmail.com", "success11", "074245789876"),
          ("Nestor","Meys","02/Apr/2002",17,"Male","Student","London", "England","Nnstorr44","nmeys1x@gmail.com","tankyfull2", "081558223459"),
          ("Mindy","Stolte","23/Mar/2001",18,"Female","Student","Manchester", "England","Dystoll23","mstolte1y@yahoo.co.uk","wishmeluck","074668763982"),
          ("Iggie","Canlin","21/Jun/2003",16,"Male","Student","London","England","Iggscal11","icanlin1z@gmail.com","goodchain23","087897656477"),
          ("Reta","Scarsbrooke","16/Feb/2001",18,"Female","Student","Liverpool","England","Scarrford123","rscarsbrooke20@gmail.com","bestfriend55","087676794456"),
          ("Consuela","Sleeford","11/Sep/1997",22,"Female","Student","Paris", "France","Conslee18","csleeford21@gmail.com","blanket34","072345332343"),
          ("Carmen","Tarbin","18/Okt/1993",26,"Female","Data Analyst","Jakarta","Indonesia","Tarbbar66","ctarbin22@gmail.com","letstry00","071645718189"),
          ("Hayden","Braidman","12/Nov/2003",16,"Male","Student","Bogota","Colombia","Hayhay1","hbraidman23@engadget.com","betterfuture","088945763782"),
          ("Regan","Radki","15/Mar/2002",17,"Male","Student","Dublin","Ireland","Momkirad","rradki24@yahoo.com","gedget2019","083545763782"),
          ("Ibby","Castard","22/Jul/2001",18,"Female","Student","Liverpool","England","Castyib","icastard25@gmail.com","blogger444","088905788842"),
          ("Sibilla","Lightoller","12/Mar/1997",21,"Female","Student","London","England","Billalar","slightoller26@bbc.co.uk","tshirtnew1","077778763782"),
          ("Curcio","Yushkin","24/Jan/1995",24,"Male","Athlete","London","England","Kenjirokin","cyushkin27@gmail.com","blanket21","070098763782"),
          ("Jeane","Quigley","12/Feb/2000",19,"Female","Student","Rome","Italy","Jquiole9","jquigley28@yahoo.com","trafficn2","073345763782"),
          ("Cathi","Iroiki","15/Des/1986",32,"Female","Web Designer","Tokyo","Jepan","Iroikitagawa","cparcell29@umn.edu","transfermoney","073300093781"),
          ("Freeman","Grinaway","12/Mei/1990",29,"Male","Athlete","New Delhi","India","Gfreeway32","fgrinaway2a@bigcartel.com","visitus221","073345764324"),
          ("Kerrie","Carder","31/Jun/1992",27,"Female","Manager","Birmingham", "England","Kerderer","kcarder2b@gmail.com","goodmatch8","073335345465"),
          ("Colas","Zack","14/Jul/1988",31,"Male","Presenter","Berlin","Germany","Zackboy","czack2c@intel.com","footballuk4","073666637844"),
          ("Obie","Almon","25/Jan/1993",26,"Male","Athlete","Bristol","England","Obmonn15","oalmon2d@slate.com","leoandlibra","071145763889"),
          ("Nadia","Folliott","28/Feb/1984",35,"Male","Pilot","Birmingham","England","Nadiiefil12","nfolliott2e@typepad.com","firstflight86","073334563751"),
          ("Brooks","Antecki","31/Des/2001",17,"Male","Student","Coventry","England","Brookiy98","bantecki2f@moonfruit.com","dogandcat68","079847634456"),]

#my_cursor.executemany(sqlStuff, record1)
#mydb.commit()

# Create Purchase Table
#my_cursor.execute("CREATE TABLE purchase (paymentid INTEGER AUTO_INCREMENT PRIMARY KEY, uid INTEGER, productid VARCHAR(10), date VARCHAR(15), time VARCHAR(10), cardholder_name VARCHAR(255), cardnumber VARCHAR(40), expirydate VARCHAR(30))")

sqlStuff= "INSERT INTO purchase(uid,productid,date, time, cardholder_name, cardnumber, expirydate) VALUES (%s, %s,%s, %s, %s, %s, %s)"
record2= [(1, "A110","01/Jan/2019", "12:03","Terry", "450094774085778", "10/Dec/22" ),
(42,"A110","01/Jan/2019", "19:03","Marylynne", "4539547740855053", "09/Dec/22"),
(43,"A110","03/Jan/2019", "17:17","Nestor", "4929750919623298", "12/Oct/21"),
(44,"A110","05/Jan/2019", "18:11","Mindy", "4024007169992517", "11/Jul/22"),
(45,"A110","08/Jan/2019", "18:06","Iggie", "4485127677873678", "23/Jul/23"),
(46,"A110","09/Jan/2019", "15:19","Reta", "4532570511961576", "21/Nov/22"),
(47,"A110","09/Jan/2019", "15:15","Consuela", "4916165342390602", "22/Jan/22"),
(48,"A110","10/Jan/2019", "17:10","Carmen", "4485930967933023", "26/Mar/21"),
(49,"A110","10/Jan/2019", "15:01","Hayden", "4024007183389948", "29/Apr/21"),
(50,"A110","15/Jan/2019", "14:03","Regan", "4539103594291407", "19/Jun/23"),
(51,"A110","15/Jan/2019", "13:33","Ibby", "4485647027298565", "09/Jul/22"),
(52,"A110","15/Jan/2019", "13:54","Sibilla", "4716364935216504", "18/Aug/21"),
(53,"A110","15/Jan/2019", "21:34","Curcio", "4532991619391500", "15/Aug/21"),
(54,"A110","15/Jan/2019", "11:12","Jeane", "4532772708911378", "14/Sep/22"),
(55,"A110","16/Jan/2019", "12:54","Cathi", "4532744812437368", "25/Sep/22"),
(56,"A110","18/Jan/2019", "18:44","Freeman", "4929678355211171", "22/Aug/23"),
(57,"A110","19/Jan/2019", "18:22","Kerrie", "4556492697392537", "17/Jan/23"),
(58,"A110","20/Jan/2019", "19:03","Colas", "4532844662566066", "08/Feb/23"),
(59,"A110","20/Jan/2019", "20:03","Obie", "4024007120877377", "01/Jun/21"),
(60,"A110","21/Jan/2019", "20:03","Nadia", "4539371905364169", "05/Aug/20"),
(61,"A110","22/Jan/2019", "22:03","Brooks", "4929913622649584", "04/Nov/20"),]

my_cursor.executemany(sqlStuff, record2)
mydb.commit()

# Create Product Table
#my_cursor.execute("CREATE TABLE product (productid VARCHAR(10) PRIMARY KEY, product_name VARCHAR(255), product_price VARCHAR(255), product_type VARCHAR(255))")

sqlStuff= "INSERT INTO product(productid, product_name, product_price, product_type) VALUES (%s, %s, %s, %s)"
record3= ("A110", "Fitness App", "3.99","Software")

#my_cursor.execute(sqlStuff, record3)
#mydb.commit()



