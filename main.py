import requests
import random
import time

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeGyzgJYrgkUeuQkMhLRmxAHIg4hLg6nFlmEcNTBowOoHkFYA/formResponse"

choices = {
    "entry.1126116546": ["否"],
    "entry.522028827": ["<18", "18-24", "25-34", "35-44", "45-54", "55-64", ">65"],
    "entry.2086055473": ["是", "否"],
    "entry.2022067923": ["頰囊", "瞬膜", "交尾器"],
    "entry.1227509380": ["父系", "母系"],
    "entry.1816932274": ["是", "否"],
    "entry.601359918": ["吃跳蚤或攝取鹽分", "清理身體", "建立良好關係"],
    "entry.1055468015": ["會", "不會"],
    "entry.186115364": ["是", "否"],
}

def get_random_answers(choices):
    return {key: random.choice(value) for key, value in choices.items()}

def auto_submit_form(min_interval, max_interval, total_submissions):
    for i in range(total_submissions):
        answers = get_random_answers(choices)
        response = requests.post(form_url, data=answers)
        if response.status_code == 200:
            print(f"第 {i+1} 次提交成功！答案：{answers}")
        else:
            print(f"第 {i+1} 次提交失敗，狀態碼：{response.status_code}")
        
        # 隨機等待一段時間後再繼續，等待時間在 min_interval 與 max_interval 之間
        wait_time = random.uniform(min_interval, max_interval)
        print(f"等待 {wait_time:.2f} 秒後繼續提交...")
        time.sleep(wait_time)

min_interval = 5
max_interval = 10
total_submissions = 25

auto_submit_form(min_interval, max_interval, total_submissions)