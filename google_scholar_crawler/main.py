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
# 1. Google Scholar (带错误保护机制)
# ==========================================
def run_google_scholar():
    print("--- 正在获取 Google Scholar 数据 ---")
    gs_id = os.environ.get('GOOGLE_SCHOLAR_ID')
    
    # 这一步只是定义文件名，不进行写操作
    target_filename = 'gs_data_shieldsio.json' 

    if not gs_id:
        print("跳过: 环境变量中找不到 GOOGLE_SCHOLAR_ID")
        return

    try:
        # 设置超时或其他配置（scholarly 默认配置通常够用，但网络差时会抛出异常）
        # 开始爬取
        author = scholarly.search_author_id(gs_id)
        scholarly.fill(author, sections=['basics', 'indices', 'counts'])
        citation_count = author.get('citedby', 0)
        
        # --- 核心修改：数据校验 ---
        # 如果获取到的引用数为 0 或 None，视为无效数据（可能是被反爬限制），抛出异常
        if not citation_count or citation_count == 0:
            raise ValueError("获取到的引用数为 0，可能是网络问题或被反爬限制。")

        # 只有数据正常，才构建字典
        shield_data = {
            "schemaVersion": 1,
            "label": "citations",
            "message": f"{citation_count}",
            "namedLogo": "google-scholar",
            "logoColor": "white",
            "color": "4285F4"
        }
        
        # --- 核心修改：最后才保存 ---
        # 只有代码运行到这里没有报错，才会覆盖旧文件
        save_json(shield_data, target_filename)
        print(f"Google Scholar 更新成功: {citation_count}")
        
    except Exception as e:
        # 捕获所有异常（超时、网络错误、解析错误、上面自定义的ValueError）
        print(f"⚠️ Google Scholar 运行出错: {e}")
        print(f"🛑 此时不执行写入操作，保留 '{target_filename}' 上一次的缓存内容（如果存在）。")

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
        "label": "Scopus Citations",
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
