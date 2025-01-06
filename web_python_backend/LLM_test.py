import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

#model_name = "your model path"
model_name = ""
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=50)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

if __name__ == "__main__":

    # Example prompt
    prompt = "Hello, how are you?"
    response = generate_response(prompt)
    print("模型回覆：", response)

"""
以下程式碼提供給輸出回答格式有問題的人做參考
這個程式碼片段定義了一個名為 generate_response 的函數，該函數接受一個問題作為輸入，
並使用自己的預訓練模型生成回答。在主函數中，
你可以自己提供了一個範例問題 "Hello, how are you?" 並呼叫 generate_response 函數來生成回答。
最後，我們將生成的回答輸出到控制台。
"""

'''

model_name = "your model path"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 推理輸入模板
inference_prompt_template = """Please reply to the following question:

### Prompt:
{}
 
### Response:

"""

# 定義推理函數
def generate_response(prompt, max_length=100):
    # 構造輸入格式
    formatted_input = inference_prompt_template.format(prompt)
    
    # Tokenize 輸入
    inputs = tokenizer(formatted_input, return_tensors="pt")
    
    # 使用模型生成回覆
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        eos_token_id=tokenizer.eos_token_id,
        do_sample=True,  # 啟用隨機抽樣
        temperature=0.7, # 控制隨機性
        top_p=0.9        # 使用 nucleus sampling
    )
    
    # 解碼生成的回覆
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # 移除輸入部分，僅保留生成的回覆
    return response.replace(formatted_input, "").strip()

# 測試輸入
test_prompt = "什麼是糖尿病？"
response = generate_response(test_prompt)
print("模型回覆：", response)


'''