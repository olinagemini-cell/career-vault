"""
OCR 工具 - 将图片或扫描版PDF转为文本
用法:
    python ocr_tool.py <文件路径>           # 处理单个文件，输出到控制台
    python ocr_tool.py <文件路径> -o out.txt  # 输出到文件
    python ocr_tool.py <文件夹路径>          # 批量处理文件夹内所有图片/PDF
"""

import sys
import os
import argparse
from pathlib import Path

from rapidocr_onnxruntime import RapidOCR
from PIL import Image
import fitz  # PyMuPDF


def pdf_to_images(pdf_path, dpi=200):
    """将PDF每页转为PIL Image列表"""
    doc = fitz.open(pdf_path)
    images = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        # 使用较高DPI以提升OCR质量
        zoom = dpi / 72
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append((page_num + 1, img))
    doc.close()
    return images


def ocr_image(engine, img_path_or_pil):
    """对单张图片进行OCR，返回识别文本"""
    if isinstance(img_path_or_pil, (str, Path)):
        result, _ = engine(str(img_path_or_pil))
    else:
        # PIL Image -> 临时保存再识别（rapidocr需要路径或numpy数组）
        import numpy as np
        img_array = np.array(img_path_or_pil)
        result, _ = engine(img_array)

    if not result:
        return ""
    # result 是 list of [bbox, text, confidence]
    lines = [item[1] for item in result]
    return "\n".join(lines)


def process_file(engine, file_path):
    """处理单个文件（图片或PDF），返回OCR文本"""
    file_path = Path(file_path)
    ext = file_path.suffix.lower()
    output_parts = []

    if ext == ".pdf":
        images = pdf_to_images(str(file_path))
        for page_num, img in images:
            text = ocr_image(engine, img)
            output_parts.append(f"===== 第 {page_num} 页 =====\n{text}")
    elif ext in (".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".tif", ".webp"):
        text = ocr_image(engine, str(file_path))
        output_parts.append(text)
    else:
        output_parts.append(f"[跳过] 不支持的文件格式: {ext}")

    return "\n\n".join(output_parts)


def main():
    parser = argparse.ArgumentParser(description="OCR工具 - 图片/扫描PDF转文本")
    parser.add_argument("path", help="文件或文件夹路径")
    parser.add_argument("-o", "--output", help="输出文件路径（默认输出到控制台）")
    args = parser.parse_args()

    target = Path(args.path)
    if not target.exists():
        print(f"错误: 路径不存在 - {target}")
        sys.exit(1)

    print("正在初始化OCR引擎...", file=sys.stderr)
    engine = RapidOCR()

    results = []

    if target.is_file():
        print(f"处理: {target.name}", file=sys.stderr)
        text = process_file(engine, target)
        results.append(f"## {target.name}\n\n{text}")
    elif target.is_dir():
        supported = {".pdf", ".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".tif", ".webp"}
        files = sorted([f for f in target.iterdir() if f.suffix.lower() in supported])
        if not files:
            print("文件夹中没有找到支持的图片或PDF文件")
            sys.exit(1)
        for i, f in enumerate(files, 1):
            print(f"处理 [{i}/{len(files)}]: {f.name}", file=sys.stderr)
            text = process_file(engine, f)
            results.append(f"## {f.name}\n\n{text}")

    final_output = "\n\n---\n\n".join(results)

    if args.output:
        out_path = Path(args.output)
        out_path.write_text(final_output, encoding="utf-8")
        print(f"\n结果已保存到: {out_path}", file=sys.stderr)
    else:
        print(final_output)


if __name__ == "__main__":
    main()
