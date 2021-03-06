
## Tasks

**2. Legacy Central System(To be developed):**<br/><br/>
**- The system must read the people.csv file**<br/><br/>

*"Legacy_Central_System" --> "cpr_generator.py" --> "def create_nemIds()"*<br/><br/>

**- For each person that is found in the file it will:**<br/><br/>
>**- Generate a CPR similarly to how a normal CPR looks:ddMMyyy-[random-4-digits]**<br/><br/>

>*"Legacy_Central_System" --> "cpr_generator.py" --> "def create_nemIds()"*<br/><br/>
	  
>**- Build an xml body that containsthe first name, last name and CPR number**<br/><br/>

>*"Legacy_Central_System" --> "cpr_generator.py" --> "def create_xml(person)"*<br/><br/>

>**- Send a POST request to http://localhost:8080/nemIDwith the XML as a body**<br/><br/>

>*"Legacy_Central_System" --> "nemId_generator.py"*<br/><br/>

>**- The NemID system will return a JSON body:**<br/><br/>
	{<br/>
		"nemID": "some 9 digit nemID"<br/>
	}<br/><br/>

>*"Proof" --> "Auth_User_200.PNG"*<br/><br/>

>**- An msgpack file will be created with the name [CPR].msgpack which will contain f_name, l_name, birth_date<br/>[DD-MM-YYYY], email, country, phone, address, CPR and NemID number. Isuggest you makea JSON<br/>object and then serialize it.**<br/><br/>

>*"Legacy_Central_System" --> "cpr_generator.py" --> "def save_msgpack(person)"*

---

**4.NemID User Generator:**<br/><br/>
**- Will receive a POST request to http://localhost:8088/generate-nemID with body:**<br/><br/>
{<br/>
	"cpr": "some 10 digit CPR",<br/>
	"email": "some@email.com"<br/>
}<br/><br/>

*"NemID_UserGenerator" --> "user_generator.js"*<br/><br/>

**- Will return a JSON response (status 201):**<br/><br/>
"nemID": "random_5_digit_number-Last_4_digits_of_CPR"<br/><br/>

*"NemID_UserGenerator" --> "user_generator.js"*

---

**5.NemID Password Generator:**<br/><br/>
**- Will receive a POST request to http://localhost:8089/generate-password-nemIDwith body:**<br/><br/>
{<br/>
	"nemID": "random_5_digit_number-Last_4_digits_of_CPR",<br/>
	"cpr": "cpr_number"<br/>
}<br/><br/>

*"NemID_PasswordGenerator" --> "password_generator.js"*<br/><br/>

**- Will send a JSON response (status 200):**<br/><br/>
{<br/>
	"nemIdPassword": "first 2 digits of nemId and last 2 digits of the cpr"<br/>
}<br/><br/>

*"Proof" --> "Auth_User_200.PNG"*

---

**6.NemID Code Generator:**<br/><br/>
**- Will receive a POST request at http://localhost:8090/nemid-authwith JSON body:**<br/>
{<br/>
	"nemIdCode": "code of 4 digits",<br/>
	"nemId": "generated 9 digit nemID"<br/>
}<br/><br/>

*"NemID_CodeGenerator" --> "auth_code_generator.js"*<br/><br/>

**- Check against the data from the database. If it matches this will return a JSON bodywith status code 200.<br/> Otherwise it will return a 403(forbidden):**<br/>
{<br/>
	"generatedCode": "random 6 digit code"<br/>
}<br/><br/>

*"NemID_CodeGenerator" --> "auth_code_generator.js"*
