#!/usr/bin/env python3
"""
文本分析脚本 - 用于预处理和分析 txt 文件
"""
import sys
import json
import re
from collections import Counter

def analyze_text(file_path):
    """分析文本文件并返回统计信息"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return json.dumps({"error": f"文件未找到: {file_path}"}, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": f"读取文件失败: {str(e)}"}, ensure_ascii=False)
    
    # 基础统计
    lines = content.split('\n')
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
    words = re.findall(r'\b\w+\b', content)
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', content)
    
    # 关键词提取
    stopwords = {'的', '了', '是', '在', '有', '和', '就', '不', '都', '也', 'the', 'a', 'is', 'are', 'was', 'to', 'of', 'in', 'for', 'on', 'with', 'at', 'by', 'it', 'as'}
    all_words = list(chinese_chars) + [w.lower() for w in words if w.lower() not in stopwords and len(w) > 1]
    word_freq = Counter(all_words).most_common(15)
    
    analysis = {
        "statistics": {
            "total_characters": len(content),
            "chinese_characters": len(chinese_chars),
            "total_words": len(words),
            "total_lines": len(lines),
            "non_empty_lines": len([l for l in lines if l.strip()]),
            "total_paragraphs": len(paragraphs)
        },
        "top_keywords": [{"word": w, "count": c} for w, c in word_freq],
        "content_preview": content[:500] if len(content) > 500 else content,
        "file_path": file_path
    }
    
    return json.dumps(analysis, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "请提供文件路径参数"}, ensure_ascii=False))
        sys.exit(1)
    print(analyze_text(sys.argv[1]))
