from PIL import Image, ImageEnhance, ImageOps
import re
from pathlib import Path

def generate_ascii_tspans(image_path="github.jpg", width=88, height=53):
    img = Image.open(image_path).convert("L")
    img = ImageOps.autocontrast(img)
    img = ImageEnhance.Contrast(img).enhance(1.5)
    img = ImageEnhance.Sharpness(img).enhance(1.8)

    img_resized = img.resize((width, height), Image.Resampling.LANCZOS)
    pixels = img_resized.getdata()

    ASCII_CHARS = [" ", ".", ":", "-", "=", "+", "*", "%", "#", "@"]

    lines = []
    for i in range(height):
        line = ""
        for j in range(width):
            p = pixels[i * width + j]
            idx = int((p / 255) * (len(ASCII_CHARS) - 1))
            line += ASCII_CHARS[idx]
        lines.append(line)

    y_coords = [
        79.98, 87.53, 95.07, 102.62, 110.17, 117.72, 125.27, 132.81, 140.36, 147.91,
        155.46, 163.01, 170.55, 178.10, 185.65, 193.20, 200.75, 208.29, 215.84, 223.39,
        230.94, 238.49, 246.03, 253.58, 261.13, 268.68, 276.23, 283.77, 291.32, 298.87,
        306.42, 313.97, 321.51, 329.06, 336.61, 344.16, 351.71, 359.25, 366.80, 374.35,
        381.90, 389.45, 396.99, 404.54, 412.09, 419.64, 427.19, 434.73, 442.28, 449.83,
        457.38, 464.93, 472.47
    ]

    tspans = []
    for line, y in zip(lines, y_coords):
        # Escape any XML special characters just in case
        line_clean = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        tspans.append(f'<tspan x="30" y="{y:.2f}" xml:space="preserve">{line_clean}</tspan>')

    return "\n".join(tspans)

def update_svg_file(svg_path, new_ascii_tspans):
    content = Path(svg_path).read_text(encoding="utf-8")
    
    # Pattern matching between <text x="30" y="0" class="ascii"> and </text>
    pattern = r'(<text x="30" y="0" class="ascii">\s*\n)[\s\S]*?(\n\s*</text>)'
    replacement = r'\1' + new_ascii_tspans + r'\2'
    
    updated_content = re.sub(pattern, replacement, content)
    Path(svg_path).write_text(updated_content, encoding="utf-8")
    print(f"Updated {svg_path} successfully!")

if __name__ == "__main__":
    tspans_code = generate_ascii_tspans("github.jpg")
    update_svg_file("dark.svg", tspans_code)
    update_svg_file("light.svg", tspans_code)
