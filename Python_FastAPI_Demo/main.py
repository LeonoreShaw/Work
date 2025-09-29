from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import HTMLResponse
import pandas as pd
from sklearn.linear_model import LinearRegression

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    return '''
    <h1>激光器功率诊断工具 — FastAPI Demo</h1>
    <form action="/analyze" enctype="multipart/form-data" method="post">
    <input name="file" type="file" accept=".csv">
    <input type="submit">
    </form>
    '''

@app.post("/analyze")
async def analyze(file: UploadFile):
    df = pd.read_csv(file.file)
    required = ["time","power","water_temp","spot_cx","spot_cy","spot_sizex","spot_sizey"]
    if not all(c in df.columns for c in required):
        return {"error":"缺少必要列"}
    X = df[["water_temp","spot_cx","spot_cy","spot_sizex","spot_sizey"]].fillna(method="ffill")
    y = df["power"].fillna(method="ffill")
    model = LinearRegression().fit(X,y)
    coeffs = dict(zip(X.columns, model.coef_))
    main = max(coeffs, key=lambda k: abs(coeffs[k]))
    return {"coeffs":coeffs, "diagnosis":f"功率下降主要受 {main} 影响 (coef={coeffs[main]:.3f})"}
