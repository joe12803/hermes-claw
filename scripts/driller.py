import os
import sys
import subprocess
from pathlib import Path

ALLOWED_EXTENSIONS = {'.go', '.py', '.js', '.ts', '.c', '.cpp', '.h', '.java', '.rs', '.php', '.sh', '.yaml', '.yml', '.sql'}
EXCLUDE_DIRS = {'node_modules', 'vendor', '.git', 'dist', 'build', 'assets', 'static', 'public', 'temp', 'venv', '__pycache__'}
# 调低分片阈值到 5MB，增加并发读取稳定性
MAX_CHUNK_SIZE = 5 * 1024 * 1024  

def drill_repo(repo_path, output_prefix):
    repo_path = Path(repo_path).resolve()
    current_chunk_content = []
    current_chunk_size = 0
    chunk_index = 1

    print(f"🚀 [加强版] 开启地毯式钻探: {repo_path}")

    # 先统计总文件数
    all_files = []
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix.lower() in ALLOWED_EXTENSIONS:
                all_files.append(file_path)
    
    print(f"📊 识别到核心矿脉文件: {len(all_files)} 个")

    for file_path in all_files:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                # 深度精炼：去空行、去首尾空格
                lines = [line.strip() for line in f.readlines() if line.strip()]
                if not lines: continue
                
                content = f"\n### FILE_START: {file_path.relative_to(repo_path)} ###\n" + "\n".join(lines) + f"\n### FILE_END: {file_path.relative_to(repo_path)} ###\n"
                content_size = len(content.encode('utf-8'))
                
                if current_chunk_size + content_size > MAX_CHUNK_SIZE:
                    save_chunk(output_prefix, chunk_index, current_chunk_content)
                    chunk_index += 1
                    current_chunk_content = []
                    current_chunk_size = 0
                
                current_chunk_content.append(content)
                current_chunk_size += content_size
        except Exception as e:
            print(f"⚠️ 跳过异常矿层 {file_path}: {e}")

    if current_chunk_content:
        save_chunk(output_prefix, chunk_index, current_chunk_content)
    
    print(f"✅ 地毯式钻探完成！已产出 {chunk_index} 个完整矿包。")

def save_chunk(prefix, index, content_list):
    filename = f"{prefix}_part{index}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(content_list)
    print(f"📦 矿包就绪: {filename} ({os.path.getsize(filename)//1024} KB)")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)
    drill_repo(sys.argv[1], sys.argv[2])
