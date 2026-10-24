import express, { Request, Response } from 'express'
import val from '@utils/ran'

const app = express()

app.get('/', async (req: Request, res: Response) => {
  res.json({message:'okay'})
}) 

console.log(val(),': from module')


app.listen(7000,()=>{
  console.log('server running on port 7000')
})