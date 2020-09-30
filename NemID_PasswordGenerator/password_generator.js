const port = 8089;
const express = require('express');

var app = express();

app.use(express.json());


app.post('/generate-password-nemID', (req, res) =>{
    let nemId = req.body.nemId;
    let cpr = req.body.cpr;

    // First 2 digits of nemid
    let firstNemId = nemId.slice(0, 2);
    
    // Last 2 digits of cpr
    let lastCpr = cpr.slice(cpr.length - 2);

    let password = firstNemId.toString() + lastCpr.toString();
    
    res.status(201).send({nemIdPassword: password});
});

app.listen(port, (err) => {
    if(err){
        console.log(err);
    }
    else{
        console.log("Listening on port " + port);
        console.log("Password generator is running...");
    }
});