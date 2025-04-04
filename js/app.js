const express = require("express")
const cors = require("cors")
const app = express()

app.use(express.json())
app.use(cors({
  methods: ["GET","POST"],
  credentials: true,
  origin:"http://localhost:8080"
}))
app.use(express.urlencoded({ extended: true }));



app.post("/suma",(req,res)=>{
  const {matriz1, matriz2} = req.body
    const resultado = matriz1.map((fila, i) => 
      fila.map((valor, j) => valor + matriz2[i][j])
    );
    console.log("resultado",resultado)
    res.json({"resultado":resultado})
})

const port = 4500
app.listen(port,()=>{
  console.log("Servidor iniciado en el puerto", port)
})