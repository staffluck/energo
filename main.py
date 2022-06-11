import fastapi
import uvicorn

from utils import colored_items_solution, solve


app = fastapi.FastAPI()


@app.get("/solve/")
def solve_quadratic_equation(a: int, b: int, c: int):
    solution = solve(a, b, c)

    response = {
        "solution": solution
    }
    return response


@app.get("/colored_items_solve/")
def solve_colored_items(number: int):
    solution = colored_items_solution(number)

    response = {
        "solution": solution.name
    }
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
