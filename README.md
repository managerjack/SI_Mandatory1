
## Tasks

**2.Legacy CentralSystem(To be developed):**
**- The system must read the people.csv file**
**-For each person that is found in the file it will:** 
	**- Generate a CPR similarly to how a normal CPR looks:ddMMyyy-[random-4-digits]**
	**- Build an xml body that containsthe first name, last name and CPR number**
	**- Send a POST request to http://localhost:8080/nemIDwith the XML as a body**
	**- The NemID system will return a JSON body:**
	{
		"nemID": "some 9 digit nemID"
	}
	**- An msgpack file will be created with the name [CPR].msgpack which will contain f_name, l_name, birth_date[DD-MM-YYYY], email, country, phone, address, CPR and NemID number. Isuggest you makea JSON object and then serialize it.**

---

**4.NemID User Generator:**
**- Will receive a POST request to http://localhost:8088/generate-nemIDwith body:**
{
	"cpr": "some 10 digit CPR",
	"email": "some@email.com"
}
**- Will return a JSON response (status 201):**
	"nemID": "random_5_digit_number-Last_4_digits_of_CPR"

---

**5.NemID Password Generator:**
**- Will receive a POST request to http://localhost:8089/generate-password-nemIDwith body:**
{
	"nemID": "random_5_digit_number-Last_4_digits_of_CPR",
	"cpr": "cpr_number"
}
**- Will send a JSON response (status 200):**
{
	"nemIdPassword": "first 2 digits of nemId and last 2 digits of the cpr"
}

---

**6.NemID Code Generator:**
**- Will receive a POST request at http://localhost:8090/nemid-authwith JSON body:**
{
	"nemIdCode": "code of 4 digits",
	"nemId": "generated 9 digit nemID"
}
**- Check against the data from the database. If it matches this will return a JSON bodywith status code 200. Otherwise it will return a 403(forbidden):**
{
	"generatedCode": "random 6 digit code"
}
