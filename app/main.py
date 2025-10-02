from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    '''Корневой маршрут, подтверждающий, что API работает.'''
    return {'message': 'Добро пожаловать в API интернет-магазина!'}