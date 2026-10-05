from openai import OpenAI
import json

client = OpenAI(
    api_key="你的API_KEY放到本地环境变量里",  # 记得换成你的
    base_url="https://api.deepseek.com"
)

# 1. 定义一个本地真正执行的函数（这里模拟查天气）
def get_weather(city):
    # 真实场景这里会去调用高德/和风天气API，这里我们用假数据
    return f"{city}今天是晴天，气温25度，很适合出门。"

# 2. 用 JSON 描述这个工具，告诉大模型你有哪些工具可用
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取指定城市的天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称，例如：北京、苏州"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

# 3. 模拟用户提问（这次我们问天气）
messages = [{"role": "user", "content": "帮我查一下苏州的天气怎么样？"}]

# 4. 第一次请求模型
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    tools=tools
)

msg = response.choices[0].message

# 5. 检查模型是否决定调用工具
if msg.tool_calls:
    print("✅ 模型决定调用工具！")
    tool_call = msg.tool_calls[0]
    func_name = tool_call.function.name
    args = json.loads(tool_call.function.arguments)
    
    print(f"👉 模型想要调用的函数: {func_name}")
    print(f"👉 模型传入的参数: {args}")
    
    # 6. 执行本地真实函数，拿到结果
    if func_name == "get_weather":
        result = get_weather(args["city"])
        print(f"👉 本地函数返回: {result}")
        
        # 7. 把模型的请求和工具结果，一并追加进对话历史
        messages.append(msg)
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result
        })
        
        # 8. 第二次请求模型，让它根据天气结果组织自然语言回复
        final_response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages
        )
        print("\n🎉 AI 最终回答：")
        print(final_response.choices[0].message.content)
else:
    print("模型没有调用工具，直接回答：")
    print(msg.content)
