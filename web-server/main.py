# Import store
import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Comando para ejecutar uvicorn
# uvicorn main:app --reload
@app.get('/')
def get_list():
    return [1, 2, 3]


@app.get('/contact', response_class=HTMLResponse)
def get_list2():
    return """
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
    """


@app.get('/contacts')
def get_list3():
    return {"Name": "LKS Code"}


def run():
    """Function Start"""
    store.get_categories()


if __name__ == '__main__':
    run()
