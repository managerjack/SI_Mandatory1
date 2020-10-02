
## Tasks

**2.Legacy CentralSystem(To be developed):**<br/>
**- The system must read the people.csv file**<br/>
**-For each person that is found in the file it will:**<br/> 
	**- Generate a CPR similarly to how a normal CPR looks:ddMMyyy-[random-4-digits]**<br/>
	**- Build an xml body that containsthe first name, last name and CPR number**<br/>
	**- Send a POST request to http://localhost:8080/nemIDwith the XML as a body**<br/>
	**- The NemID system will return a JSON body:**<br/>
	{<br/>
		"nemID": "some 9 digit nemID"<br/>
	}<br/>
	**- An msgpack file will be created with the name [CPR].msgpack which will contain f_name, l_name, birth_date<br/>[DD-MM-YYYY], email, country, phone, address, CPR and NemID number. Isuggest you makea JSON<br/>object and then serialize it.**

---

**4.NemID User Generator:**<br/>
**- Will receive a POST request to http://localhost:8088/generate-nemIDwith body:**<br/>
{<br/>
	"cpr": "some 10 digit CPR",<br/>
	"email": "some@email.com"<br/>
}
**- Will return a JSON response (status 201):**<br/>
	"nemID": "random_5_digit_number-Last_4_digits_of_CPR"

---

**5.NemID Password Generator:**<br/>
**- Will receive a POST request to http://localhost:8089/generate-password-nemIDwith body:**<br/>
{<br/>
	"nemID": "random_5_digit_number-Last_4_digits_of_CPR",<br/>
	"cpr": "cpr_number"<br/>
}<br/>
**- Will send a JSON response (status 200):**<br/>
{<br/>
	"nemIdPassword": "first 2 digits of nemId and last 2 digits of the cpr"<br/>
}

---

**6.NemID Code Generator:**<br/>
**- Will receive a POST request at http://localhost:8090/nemid-authwith JSON body:**<br/>
{<br/>
	"nemIdCode": "code of 4 digits",<br/>
	"nemId": "generated 9 digit nemID"<br/>
}<br/>
**- Check against the data from the database. If it matches this will return a JSON bodywith status code 200.<br/> Otherwise it will return a 403(forbidden):**<br/>
{<br/>
	"generatedCode": "random 6 digit code"<br/>
}
