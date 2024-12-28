import torch
print(torch.cuda.is_available())  # True 表示可用
print(torch.cuda.current_device())  # 顯示當前 GPU ID
print(torch.cuda.get_device_name(0))  # 顯示 GPU 名稱