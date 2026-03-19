#!/usr/bin/env python3
"""
图片解析辅助脚本
提供图片分析的结构化输出模板和常见处理逻辑
"""

import json
from typing import Dict, List, Any, Optional

def create_analysis_report(
    image_type: str,
    content_summary: str,
    extracted_data: Optional[Dict] = None,
    insights: Optional[List[str]] = None,
    confidence_level: str = "high"
) -> Dict[str, Any]:
    """创建标准化的图片分析报告"""
    report = {
        "image_type": image_type,
        "summary": content_summary,
        "confidence": confidence_level,
        "analysis": {
            "key_elements": [],
            "data_points": [],
            "relationships": []
        }
    }
    if extracted_data:
        report["extracted_data"] = extracted_data
    if insights:
        report["insights"] = insights
    return report


def format_chart_data(
    chart_type: str,
    labels: List[str],
    values: List[Any],
    units: str = ""
) -> Dict[str, Any]:
    """格式化图表数据"""
    return {
        "chart_type": chart_type,
        "data": [
            {"label": label, "value": value, "unit": units}
            for label, value in zip(labels, values)
        ],
        "statistics": {
            "max": max(values) if values else None,
            "min": min(values) if values else None,
            "average": sum(values) / len(values) if values else None,
            "count": len(values)
        }
    }


def format_flowchart_analysis(
    steps: List[Dict[str, str]],
    start_node: str = "",
    end_node: str = ""
) -> Dict[str, Any]:
    """格式化流程图分析结果"""
    return {
        "flowchart_type": "process_flow",
        "start": start_node,
        "end": end_node,
        "steps": steps,
        "complexity": "simple" if len(steps) < 5 else "moderate" if len(steps) < 10 else "complex"
    }


def format_ocr_result(
    text_blocks: List[Dict[str, Any]],
    structure_type: str = "plain"
) -> Dict[str, Any]:
    """格式化 OCR 识别结果"""
    return {
        "structure_type": structure_type,
        "text_blocks": text_blocks,
        "full_text": " ".join([block.get("text", "") for block in text_blocks]),
        "metadata": {
            "block_count": len(text_blocks),
            "avg_confidence": sum(
                [block.get("confidence", 0) for block in text_blocks]
            ) / len(text_blocks) if text_blocks else 0
        }
    }


def format_ui_analysis(
    ui_elements: List[Dict[str, str]],
    layout_type: str = ""
) -> Dict[str, Any]:
    """格式化界面截图分析结果"""
    suggestions = []
    for elem in ui_elements:
        elem_type = elem.get("type", "")
        elem_text = elem.get("text", "")
        if elem_type == "button":
            suggestions.append(f"点击'{elem_text}'按钮可执行相关操作")
        elif elem_type == "input":
            suggestions.append(f"在'{elem_text}'输入框中输入信息")
    
    return {
        "ui_type": "interface_screenshot",
        "layout": layout_type,
        "elements": ui_elements,
        "action_suggestions": suggestions[:5]
    }


def detect_image_quality_issues(
    blur_detected: bool = False,
    low_contrast: bool = False,
    text_too_small: bool = False
) -> List[str]:
    """检测并报告图片质量问题"""
    issues = []
    if blur_detected:
        issues.append("图片存在模糊，可能影响识别精度")
    if low_contrast:
        issues.append("对比度较低，文字或元素可能难以辨认")
    if text_too_small:
        issues.append("文字尺寸过小，部分内容可能无法准确识别")
    return issues
