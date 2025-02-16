
    
from openai import OpenAI
import json


def generate_couplets(name):
    prompt = f'''
    # 角色设定
    你是一位精通楹联文化的国学大师，擅长将人名拆解为富有诗意的春联。请遵循以下规则创作：

    # 创作规则
    1. **姓名解构**
    - 单字名：取字义+谐音（如「梅」→「梅香」+「媒」）
    - 双字名：姓与名分开处理（如「张伟」→「张」门纳福+「伟」业宏开）
    - 三字名：首字姓+后两字组合（如「欧阳修」→「欧」风送瑞+「阳修」德厚）

    2. **对仗要求**
    - 平仄：上联仄起，下联平收
    - 结构：词性相对（名词对名词，动词对动词）
    - 字数：建议7字联（上联：仄仄平平平仄仄，下联：平平仄仄仄平平）

    3. **意象组合**
    - 传统元素：梅兰竹菊/福禄寿喜/天地人和
    - 现代元素：科技兴邦/生态和谐/家国情怀
    - 职业特征：检测用户输入中的职业关键词（如教师→桃李，医生→杏林）

    # 生成模板
    【上联】[姓氏拓展]+[动作]+[吉祥物1]
    【下联】[名字拓展]+[结果]+[吉祥物2]
    【横批】[姓名谐音]+[主题词]

    # 示例演示
    输入：陈思源（程序员）
    输出：
    上联：陈门虎跃代码敲开新气象
    下联：思海龙腾源码绘就锦乾坤
    横批：源启鸿运

    输入：林芳（教师）
    输出：
    上联：林间桃李春风化雨润天下
    下联：芳圃芝兰妙笔生花书华章
    横批：芳泽杏坛

    # 特殊处理
    1. 避讳机制：
    - 自动替换「病」「衰」等不吉字
    - 检测到单名「离」→改用谐音「骊」
    
    2. 风格调节：
    - 添加「幽默版」选项（如程序员→「键盘敲出富贵，bug扫尽平安」）
    - 添加「科技感」版本（使用「区块链」「元宇宙」等新词）

    # 输入
    {name}
    
    # 输出要求
    上联为7字内容 
    下联为7字内容
    横批为4字成语
    输出json格式。此外，不要输出其他任何文字与符号。
    
    # 输出示例
    {{
    "上联": "张灯结彩迎新岁",
    "下联": "可乐盈门庆丰年",
    "横批": "可贺新禧"
    }}
    '''


    client = OpenAI(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key="4b7e220e-ad40-4c96-a2f4-3b6608526e82")

    # 发送带有流式输出的请求
    response = client.chat.completions.create(
        model="ep-20250216102316-mqwjw",
        messages=[
            {"role": "user", "content": prompt}
        ],
        #stream=True  # 启用流式输出
    )

    json_str=response.choices[0].message.content
    #print(json_str)
    data = json.loads(json_str)
    sl = data['上联']
    xl = data['下联']
    hp = data['横批']
    return sl,xl,hp
    # # 逐步接收并处理响应
    # for chunk in response:
    #     chunk_message = chunk.choices[0].delta.content
    #     print(chunk_message, end='', flush=True)
        




