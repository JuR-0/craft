from fastapi import FastAPI
import logfire
from project.routers import user

app = FastAPI()

logfire.configure(
    code_source=logfire.CodeSource(
        repository='https://github.com/JuR-0/craft',
        revision='master',
    )
)
logfire.instrument_fastapi(app, capture_headers=True)


app.include_router(user.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
