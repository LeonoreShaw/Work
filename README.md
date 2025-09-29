# 激光器功率诊断工具 — 多语言实现示例 (详细版)

本项目展示了 **6 种不同技术栈**，如何实现一个网页工具：

* 上传 CSV 数据（包含功率、水温、光斑信息等）
* 分析功率降低的可能原因
* 输出诊断结果和可视化图表

---

## 📂 压缩包内容

1. **Python_Streamlit_Demo.zip**
2. **Python_Dash_Demo.zip**
3. **Python_FastAPI_Demo.zip**
4. **JS_Frontend_Demo.zip**
5. **NodeJS_Demo.zip**
6. **R_Shiny_Demo.zip**

---

## 🚀 运行方法 & 实现说明

### 1. Python_Streamlit_Demo

**运行：**

```bash
cd Python_Streamlit_Demo
pip install -r requirements.txt
streamlit run app.py
```

访问 [http://127.0.0.1:8501](http://127.0.0.1:8501)

**实现内容：**

* 前端页面由 **Streamlit** 自动生成，不需要手写 HTML/JS
* 代码逻辑：

  1. 上传 CSV 文件 → `st.file_uploader`
  2. Pandas 读取数据，展示表格
  3. 使用 Matplotlib 绘制功率随时间曲线
  4. 使用 Seaborn 绘制相关性热图
  5. 用 scikit-learn 的 **线性回归** 拟合功率与各因素的关系，输出主要影响因素

👉 特点：快速原型开发，科研人员友好。

---

### 2. Python_Dash_Demo

**运行：**

```bash
cd Python_Dash_Demo
pip install -r requirements.txt
python app.py
```

访问 [http://127.0.0.1:8050](http://127.0.0.1:8050)

**实现内容：**

* 前端 UI 使用 **Dash (Plotly)** 生成，支持更强交互
* 上传 CSV → `dcc.Upload` 组件
* 数据处理和回归分析在 Python 后端完成
* 图表用 **Plotly Graphs** 动态绘制，可缩放/悬停查看

👉 特点：交互性比 Streamlit 更强，适合数据分析类 Web App。

---

### 3. Python_FastAPI_Demo

**运行：**

```bash
cd Python_FastAPI_Demo
pip install -r requirements.txt
uvicorn app:app --reload
```

访问 [http://127.0.0.1:8000](http://127.0.0.1:8000)

**实现内容：**

* **后端：FastAPI**

  * `/upload` 接口：接收 CSV 文件
  * Pandas 分析数据，返回 JSON 格式的诊断结果（回归系数、主要影响因素）
* **前端：HTML + JavaScript**

  * 使用 `<input type="file">` 上传
  * 通过 `fetch('/upload')` 向后端发送文件
  * 用 Chart.js 绘制功率曲线

👉 特点：前后端分离，适合扩展成大规模服务。

---

### 4. JS_Frontend_Demo

**运行：**
直接在浏览器打开：

```
JS_Frontend_Demo/index.html
```

**实现内容：**

* 纯前端（HTML + JS），无需服务器
* 使用 **PapaParse** 在浏览器端解析 CSV
* 使用 **Chart.js** 绘制曲线图
* 在前端用 JS 简单计算功率和水温/光斑的相关性，输出主要影响因素

👉 特点：无需后端，直接网页运行，适合轻量级工具。

---

### 5. NodeJS_Demo

**运行：**

```bash
cd NodeJS_Demo
npm install
node server.js
```

访问 [http://127.0.0.1:3000](http://127.0.0.1:3000)

**实现内容：**

* **后端：Node.js + Express**

  * `/upload` 接口接收 CSV 文件
  * 使用 `csv-parser` 解析数据
  * 简单统计分析（相关性/趋势）
  * 返回 JSON 诊断结果
* **前端：HTML + Chart.js**

  * 文件上传
  * 向 `/upload` POST 文件
  * 接收诊断结果并绘制图表

👉 特点：全 JS 技术栈，前后端都用 JavaScript，部署方便。

---

### 6. R_Shiny_Demo

**运行：**
在 R 环境中执行：

```R
shiny::runApp("R_Shiny_Demo")
```

访问 [http://127.0.0.1:3838](http://127.0.0.1:3838)

**实现内容：**

* **Shiny 自动生成前端**

  * 文件上传 → `fileInput`
  * 数据表格 → `renderTable`
  * 图表 → `ggplot2` 绘制
* 分析部分：

  * 用 `lm()` 做线性回归
  * 输出主要影响因素

👉 特点：统计人员友好，图表美观，代码简洁。

---

## 📊 示例数据格式

每个 demo 包含 `sample.csv`，格式如下：

```
time,power,water_temp,spot_cx,spot_cy,spot_sizex,spot_sizey
2025-09-29 00:00:00,100,20,0.00,0.00,1.00,1.00
2025-09-29 00:01:00,99,20.5,0.02,0.01,1.01,1.01
2025-09-29 00:02:00,97,21,0.05,0.02,1.03,1.02
```

---

## ✅ 总结

* **科研快速原型** → Streamlit / Dash
* **服务化部署** → FastAPI / Node.js
* **轻量工具** → JS 前端
* **统计科研人员** → R Shiny

你可以根据需求选择合适的版本。
