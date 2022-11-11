from pickletools import string1
from urllib import response
from fastapi import FastAPI
from pydantic import BaseModel
from factory import connector1
import uvicorn
import pandas as pd
# from fastapi import FastAPI, Request, Form
# from fastapi.templating import Jinja2Templates

api = FastAPI()
#templates = Jinja2Templates(directory="templates/")
class cattlemilkingdays(BaseModel):
    PinCode : str


@api.get('/api/')
async def read_form():
    return "Welcome to the feed API!"
    
@api.post('/api/satish')
async def cattlemilkingdays(request:cattlemilkingdays):
    response_json = connector1.milking(request.dict())
    return response_json
    #return templates.TemplateResponse('form.html', context={'request':cattlemilkingdays, 'response_json': response_json})
if __name__ == '__main__':
    uvicorn.run(api,host='127.0.0.1',port=8000)
#server = uvicorn.run(api)