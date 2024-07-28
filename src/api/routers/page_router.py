from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles


page_router: APIRouter = APIRouter(
    prefix="/app"
)
templates = Jinja2Templates(directory="src/templates")


@page_router.get("/main_page", response_class=HTMLResponse)
async def main_page(req: Request):
    return templates.TemplateResponse(
        request=req, name="base_page.html"
    )