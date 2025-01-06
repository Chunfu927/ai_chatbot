import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

#print(torch.cuda.is_available())  # True 表示可用
#print(torch.cuda.current_device())  # 顯示當前 GPU ID
#print(torch.cuda.get_device_name(0))  # 顯示 GPU 名稱

#model_name = "your model path"
#model_name = r"C:\Users\User\OneDrive\桌面\models\shin_os_model"
#model_name = r"C:\Users\User\OneDrive\桌面\models\Kyle_llama3.2_3b"
#model_name = r"C:\Users\User\OneDrive\桌面\models\shin_os_llama3.2_3b"
model_name = r"C:\Users\User\OneDrive\桌面\models\Eric_Cartman_llama3.2_3b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, ignore_mismatched_sizes=True)

inference_prompt_template = """Please reply to the following question:

### Prompt:
{}

### Response:

"""

def is_medical_question(prompt):
    medical_patterns = [
        r"(.*症狀.*|.*怎麼治療.*|.*吃什麼藥.*|.*怎麼辦.*|.*為什麼.*|.*你是誰.*|.*如何.*)",  # 常見問題模式
        r"(.*病.*|.*痛.*|.*高血壓.*|.*糖尿病.*|.*解釋.*|.*說說.*)"  # 醫學專有名詞
    ]
    for pattern in medical_patterns:
        if re.search(pattern, prompt, re.IGNORECASE):
            return True
    return False

def is_relevant_question(prompt):
    os_keywords = ["作業系統", "Windows", "Linux", "macOS", "Ubuntu", "系統"]
    medical_keywords = ["醫療", "健康", "疾病", "症狀", "治療", "藥物", "醫生"]
    return any(keyword in prompt for keyword in os_keywords + medical_keywords)

def generate_response(prompt):
    #if not is_relevant_question(prompt):
        #return "對不起，我只能回答與作業系統或醫療知識有關的問題。"
    if not is_medical_question(prompt):
        return "對不起，我只能回答與作業系統或醫療知識有關的問題。"
 
    formatted_input = inference_prompt_template.format(prompt)   
    inputs = tokenizer(
        formatted_input, return_tensors="pt", padding=True, truncation=True).to(model.device)
    outputs = model.generate(
        inputs["input_ids"], 
        attention_mask=inputs["attention_mask"], 
        max_length=100, 
        pad_token_id=tokenizer.eos_token_id,
        temperature=0.7,  # 控制生成的隨機性
        top_p=0.9  # 控制生成的多樣性
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.replace(formatted_input, "").strip()

if __name__ == "__main__":
    # Example prompt
    tprompt = "跟我說說什麼是扭傷？"
    response = generate_response(tprompt)
    print(response)