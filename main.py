import fastapi
import uvicorn

from utils import solve


app = fastapi.FastAPI()


@app.get("/solve/")
def solve_quadratic_equation(a: int, b: int, c: int):
    solution = solve(a, b, c)

    response = {
        "solution": solution
    }
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
