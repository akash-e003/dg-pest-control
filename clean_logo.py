import numpy as np
from PIL import Image

def create_true_transparent(input_path, output_path):
    img = Image.open(input_path).convert('RGB')
    data = np.array(img).astype(float)
    
    r = data[:, :, 0]
    g = data[:, :, 1]
    b = data[:, :, 2]
    
    max_gb = np.maximum(g, b)
    redness = r - max_gb
    
    alpha = (redness - 15) / 35.0
    alpha = np.clip(alpha, 0.0, 1.0)
    
    pure_red_mask = alpha > 0.9
    if np.any(pure_red_mask):
        text_color = np.median(data[pure_red_mask], axis=0)
    else:
        text_color = np.array([210, 30, 30])
    
    rgba = np.zeros((data.shape[0], data.shape[1], 4), dtype=np.uint8)
    rgba[:, :, 0] = text_color[0]
    rgba[:, :, 1] = text_color[1]
    rgba[:, :, 2] = text_color[2]
    rgba[:, :, 3] = (alpha * 255).astype(np.uint8)
    
    result_img = Image.fromarray(rgba)
    
    rows = np.any(alpha > 0.1, axis=1)
    cols = np.any(alpha > 0.1, axis=0)
    if np.any(rows) and np.any(cols):
        ymin, ymax = np.where(rows)[0][[0, -1]]
        xmin, xmax = np.where(cols)[0][[0, -1]]
        pad = 20
        ymin = max(0, ymin - pad)
        ymax = min(data.shape[0], ymax + pad)
        xmin = max(0, xmin - pad)
        xmax = min(data.shape[1], xmax + pad)
        result_img = result_img.crop((xmin, ymin, xmax, ymax))
        
    result_img.save(output_path)

input_image = 'images/new_logo.jpeg'
output_image = 'images/dg_true_transparent.png'

print("Processing transparent image...")
create_true_transparent(input_image, output_image)
print("Image processed successfully.")

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('images/dg_clean_logo.png', output_image)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML updated.")
