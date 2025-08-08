from fastapi import FastAPI


app=FastAPI()




@app.get('/')
def index():
    return {'message':'Hello FastApi'}













if __name__=='__main__':
    pass