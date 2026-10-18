from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Vercel explicitly scans for this specific object name at root level:
app = FastAPI()

@app.get("/")
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Fractal Generator</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #121212; color: white; }
                h1 { color: #0070f3; }
                p { font-size: 18px; }
            </style>
        </head>
        <body>
            <h1>Fractal Application</h1>
            <p>Welcome to the Vercel-compatible deployment of the Fractal project.</p>
            <small>Serverless dynamic rendering active.</small>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
  
