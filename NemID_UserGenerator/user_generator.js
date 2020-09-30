const port = 8088;
const express = require('express');

var app = express();

app.use(express.json());


app.post('/generate-nemId', (req, res) =>{
    cpr = req.body.cpr;
    var lastCpr = cpr.slice(cpr.length - 4);
    
    rand_user_num = "";
    for(i = 0; i < 5; i++)
        rand_user_num += Math.floor(Math.random() * Math.floor(10)).toString();

    generated_nemId = rand_user_num.toString() + lastCpr.toString();
    //console.log("Returning: " + generated_nemId)

    res.status(201).send({nemId: generated_nemId});
});

app.listen(port, (err) => {
    if(err){
        console.log(err);
    }
    else{
        console.log("Listening on port " + port);
        console.log("User generator is running...");
    }
});