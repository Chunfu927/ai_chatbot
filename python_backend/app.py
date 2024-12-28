from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import sqlite3

app = Flask(__name__)
CORS(app)  

model_name = "your model path"
#model_name = r"C:\Users\User\QAbot\models\shin_os_model_llama3.1"
#model_name = r"C:\Users\User\OneDrive\桌面\models\Kyle_llama3.2_3b"
#model_name = r"C:\Users\User\OneDrive\桌面\models\shin_os_llama3.2_3b"
#model_name = r"C:\Users\User\OneDrive\桌面\models\Eric_Cartman_llama3.2_3b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

#tokenizer = AutoTokenizer.from_pretrained(model_name)
#model = AutoModelForCausalLM.from_pretrained(model_name)

#獲取資料庫連線
def get_db_connection():
    conn = sqlite3.connect('feedback.db') #連線至名為feedback.db的SQLite
    conn.row_factory = sqlite3.Row
    return conn



def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            instruction TEXT NOT NULL,
            generated_text TEXT NOT NULL,
            fluency INTEGER NOT NULL,
            coherence INTEGER NOT NULL,
            relevance INTEGER NOT NULL,
            diversity INTEGER NOT NULL
        )
    ''')
    conn.close()

    # Call the function to initialize the database
    init_db()


@app.route('/', methods=['GET'])
def home():
    return "AI Text Generation API is running"

# 文字生成路徑
@app.route('/generate', methods=['POST'])
def generate_text():
    try:
        # 檢查請求格式，如果請求不是 JSON 格式，返回 400 錯誤
        if not request.is_json:
            print("Error: Request is not JSON")
            return jsonify({'error': 'Request must be JSON'}), 400
        
        data = request.json
        print(f"Received data: {data}")  # 輸出接收到的數據

        instruction = data.get('instruction', None)
        if not instruction:
            print("Error: Instruction is missing")
            return jsonify({'error': 'Instruction is required'}), 400

        temperature = data.get('temperature', 0.7)
        max_length = data.get('max_length', 100)

        '''device = torch.device('cuda' if torch.cuda.is_available(0) else 'cpu')
        model.to(device)'''
        
        input_ids = tokenizer.encode(instruction, return_tensors='pt')
        input_ids = input_ids.to('cuda')
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long)

        with torch.no_grad():
            output = model.generate(
                input_ids,
                attention_mask=attention_mask,
                max_length=max_length,
                num_return_sequences=1,
                temperature=temperature,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id,
            )            
        
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        return jsonify({'generated_text': generated_text})
        #return jsonify({'instruction': instruction})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/feedback', methods=['POST'])
def submit_feedback():
    try:
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400
        data = request.json

        # 確保 generated_text 是字符串
        '''generated_text = data.get('generated_text', "")
        if isinstance(generated_text, list):
            generated_text = "\n".join(generated_text)'''

        conn = get_db_connection()
        conn.execute('''
            INSERT INTO feedback (fluency, coherence, relevance, diversity)
            VALUES (?, ?, ?, ?)
        ''', (
            data['fluency'],
            data['coherence'],
            data['relevance'],
            data['diversity']
        ))

        conn.execute('''
            INSERT INTO QA_message (instruction, generated_text)
            VALUES (?, ?)
        ''', (
            data['instruction'],
            data['generated_text'],
        ))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Feedback submitted successfully'})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)








