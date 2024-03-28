from app import app
from os import getenv
import uvicorn

if __name__ == "__main__":
    port = int(getenv("PORT", 8000))
    uvicorn.run("main:app", port = port, reload = True)
    # app.run(debugs=True) # for testing