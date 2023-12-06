from fastapi import FastAPI
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.models import OAuthFlowAuthorizationCode
from fastapi.openapi.models import OAuthFlowAuthorizationCode as OAuthFlowAuthorizationCodeModel
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
# from fastapi.openapi.models import OAuthFlowsAuthorizationCode

app = FastAPI(
    title="Your API Title",
    description="Your API Description",
    version="1.0.0",
    openapi_url="/openapi.json",
    redoc_url=None,  # Disable ReDoc
    docs_url="/swagger",
)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

