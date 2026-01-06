from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from workflow import run_workflow

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/process")
async def process(request: Request,
                  topic: str = Form(...),
                  recipient: str = Form(...)):

    research, summary, email = run_workflow(topic, recipient)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "topic": topic,
            "recipient": recipient,
            "research": research,
            "summary": summary,
            "email": email
        }
    )
