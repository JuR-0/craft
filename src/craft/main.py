from fastapi import FastAPI
import logfire
from craft.routers import user, auth
from craft.config import CONFIG

app = FastAPI(version=CONFIG.api_version)

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


def run():
    import uvicorn

    uvicorn.run("craft.main:app", host=CONFIG.api_host,
                port=CONFIG.api_port, reload=True)
