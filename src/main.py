from fastapi import FastAPI
import logfire
from craft.routers import user, auth
from craft.config import CONFIG


app = FastAPI()

logfire.configure(
    token=CONFIG.logfire_token,
    code_source=logfire.CodeSource(
        repository='https://github.com/JuR-0/craft',
        revision='master',
    )
)
logfire.instrument_fastapi(app, capture_headers=True)

app.include_router(user.router)
app.include_router(auth.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
