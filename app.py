from flask import Flask, request

# 导入生成春联的函数
from generate_couplets import generate_couplets

app = Flask(__name__)


@app.route('/')
def index():
    上联, 下联, 横批 = generate_couplets("张在旺")
    html_content = generate_couplet_html(上联, 下联, 横批)
    return html_content   
    

def generate_couplet_html(上联, 下联, 横批):
    html_template = f"""
<!DOCTYPE html>
<html lang="zh">

<head>
    <link href="https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --secondary-color: #8B0000;
            --background-color: #F5F5DC;
            --text-color: #333;
            --divider-color: #FF0000;
        }}

        body,
        html {{
            margin: 0;
            padding: 0;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: var(--background-color);
            font-family: Arial, sans-serif;
            color: var(--text-color);
        }}

     .card {{
            width: auto;
            height: auto;
            background-color: #FFF8DC;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}

     .header {{
            background-color: var(--secondary-color);
            color: white;
            padding: 20px;
            text-align: center;
            font-family: KaiTi, SimKai;
            font-size: 24px;
        }}

     .divider {{
            width: 100%;
            height: 1px;
            background-color: var(--divider-color);
            margin: 20px 0;
        }}

     .content {{
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
        }}

     .横批 {{
            text-align: center;
            font-family: 'Kalam', cursive;
            font-size: 28px;
            color: #FFD700;
            background-color: #FF0000;
            padding: 5px 20px;
            border-radius: 5px;
            margin-bottom: 30px;
            line-height: 1.5;
        }}

     .春联区域 {{
            display: flex;
            flex-direction: row;
            justify-content: space-around;
            width: 100%;
        }}

     .上联,
     .下联 {{
            display: flex;
            flex-direction: column;
            justify-content: center;
        }}

     .上联 span,
     .下联 span {{
            writing-mode: vertical-rl;
            text-orientation: upright;
            background-color: #FF0000;
            color: #FFD700;
            width: 40px;
            height: 40px;
            line-height: 40px;
            text-align: center;
            margin: 2px;
            border-radius: 5px;
            font-family: 'Kalam', cursive;
            font-size: 28px;
            letter-spacing: 2px;
        }}

     .下联 {{
            margin-left: 250px;
        }}

     .图片区域 {{
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1;
        }}

     .图片区域 img {{
            max-width: 100px;
            max-height: 200px;
        }}

     .input - container {{
            margin - top: 30px;
            display: flex;
            flex - direction: column;
            align - items: center;
        }}

     .input - box {{
            padding: 10px;
            width: 200px;
            margin - bottom: 10px;
            border: 1px solid #ccc;
            border - radius: 5px;
        }}

     .generate - button {{
            padding: 10px 20px;
            background - color: #8B0000;
            color: white;
            border: none;
            border - radius: 5px;
            cursor: pointer;
        }}
    </style>
    <meta charset="UTF - 8">
    <meta name="viewport" content="width=device - width, initial - scale = 1.0">
    <title>定制春联展示</title>
</head>

<body>
    <div class="card">
        <div class="header">定制春联</div>
        <div class="divider"></div>
        <div class="content">
            <div class="横批">{横批}</div>
            <div class="春联区域">
                <div class="上联">
                    {' '.join([f'<span>{char}</span>' for char in 上联])}
                </div>
                <div class="图片区域">
                    <img src="https://b0.bdstatic.com/35400fa7243e39235f1e016b21dbaad5.jpg@h_1280" alt="插入的图片">
                </div>
                <div class="下联">
                    {' '.join([f'<span>{char}</span>' for char in 下联])}
                </div>
            </div>
            <div class="input - container">
                    <form action="/generate" method="post">
                    <label for="name">请输入名字:</label><br>
                    <input type="text" id="name" name="name"><br><br>
                    <input type="submit" value="生成定制春联">
                    </form>
            </div>
        </div>
    </div>
</body>

</html>
"""
    return html_template


@app.route('/generate', methods=['POST'])
def generate():
    name = request.form.get('name')
    上联, 下联, 横批 = generate_couplets(name)
    html_content = generate_couplet_html(上联, 下联, 横批)
    return html_content    

 


if __name__ == '__main__':
    app.run(debug=False, port=65534)
