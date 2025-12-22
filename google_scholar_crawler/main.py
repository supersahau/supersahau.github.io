import os
import json
import requests
from scholarly import scholarly

# --- 工具函数：保存文件 ---
def save_json(data, filename):
    output_dir = 'results'
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)
    with open(file_path, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ 文件已生成: {filename}")

# ==========================================
# 1. Google Scholar (保持自动爬取)
# ==========================================
def run_google_scholar():
    print("--- 正在获取 Google Scholar 数据 ---")
    gs_id = os.environ.get('GOOGLE_SCHOLAR_ID')
    if not gs_id:
        print("跳过: 环境变量中找不到 GOOGLE_SCHOLAR_ID")
        return

    try:
        author = scholarly.search_author_id(gs_id)
        scholarly.fill(author, sections=['basics', 'indices', 'counts'])
        citation_count = author.get('citedby', 0)
        
        # 保存 Google 数据
        shield_data = {
            "schemaVersion": 1,
            "label": "citations",
            "message": f"{citation_count}",
            "namedLogo": "google-scholar",
            "logoColor": "white",
            "color": "4285F4"
        }
        save_json(shield_data, 'gs_data_shieldsio.json')
        print(f"Google Scholar 更新成功: {citation_count}")
        
    except Exception as e:
        print(f"Google Scholar 运行出错: {e}")

# ==========================================
# 2. Scopus 部分 (手动输入模式)
# ==========================================
def run_scopus():
    print("\n--- 正在生成 Scopus 数据 (手动模式) ---")
    
    # 👇👇👇 在这里直接修改你的引用次数 👇👇👇
    manual_count = "12" 
    # 👆👆👆 每次引用增加了，就来改这个数字，然后提交代码即可
    
    print(f"当前手动设置的 Scopus 引用数为: {manual_count}")

    # 生成 Shields.io 需要的 JSON
    shield_data = {
        "schemaVersion": 1,
        "label": "Scopus Citations", # 这个标签会被 URL 参数覆盖，但留着无妨
        "message": str(manual_count),
        "namedLogo": "scopus",
        "logoColor": "white",
        "color": "orange"
    }
    
    # 保存文件
    save_json(shield_data, 'scopus_data_shieldsio.json')

# ==========================================
# 主程序入口
# ==========================================
if __name__ == "__main__":
    run_google_scholar()
    run_scopus()
