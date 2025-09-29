const express = require('express');
const fileUpload = require('express-fileupload');
const csv = require('csv-parser');
const fs = require('fs');
const app = express();
app.use(fileUpload());

app.get('/', (req,res)=>{
  res.send(`<h1>激光器功率诊断工具 — Node.js Demo</h1>
    <form ref='uploadForm' 
      id='uploadForm' 
      action='/analyze' 
      method='post' 
      encType="multipart/form-data">
        <input type="file" name="file" />
        <input type='submit' value='Upload!' />
    </form>`);
});

app.post('/analyze', (req,res)=>{
  if (!req.files || !req.files.file) return res.send("No file uploaded");
  const tempPath = "./temp.csv";
  req.files.file.mv(tempPath, err=>{
    if(err) return res.status(500).send(err);
    let rows=[];
    fs.createReadStream(tempPath).pipe(csv()).on('data',(r)=>rows.push(r)).on('end',()=>{
      let powers=rows.map(r=>parseFloat(r.power));
      let temps=rows.map(r=>parseFloat(r.water_temp));
      // simple regression slope calc
      let n=powers.length;
      let xm=temps.reduce((a,b)=>a+b,0)/n;
      let ym=powers.reduce((a,b)=>a+b,0)/n;
      let num=0,den=0;
      for(let i=0;i<n;i++){num+=(temps[i]-xm)*(powers[i]-ym);den+=(temps[i]-xm)**2;}
      let slope=num/den;
      res.send("回归 slope Power~water_temp="+slope.toFixed(3));
    });
  });
});

app.listen(3000, ()=>console.log("Server on http://localhost:3000"));
