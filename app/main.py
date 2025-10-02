from fastapi import FastAPI

from routers import categories, prooducts


app = FastAPI(
    title='Интернет-магазин "MyLavka"',
    version='0.1.0',
)

app.include_router(categories.router)
app.include_router(prooducts.router)


@app.get('/')
async def root():
    '''Корневой маршрут, подтверждающий, что API работает.'''
    return {'message': 'Добро пожаловать в API интернет-магазина!'}