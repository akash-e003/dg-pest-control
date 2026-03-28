import os
import shutil
import glob
import re

img_dir = 'images/new_logo.png'
dest_file = 'images/new_logo.jpg'
if os.path.exists(img_dir) and os.path.isdir(img_dir):
    files = glob.glob(os.path.join(img_dir, '*'))
    if files:
        src_file = files[0]
        ext = os.path.splitext(src_file)[1]
        dest_file = 'images/new_logo' + ext
        shutil.move(src_file, dest_file)
        print('Moved logo to', dest_file)
    try:
        os.rmdir(img_dir)
    except Exception as e:
        print("Could not delete dir:", e)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'(<div class="logo-circle">\s*<img src=")data:image/[^"]+(")'
replacement = r'\g<1>' + dest_file.replace('\\', '/') + r'\g<2>'

new_html, count = re.subn(pattern, replacement, html)
print(f'Replaced {count} instances in logo-circle.')

# Match the specific large base64 string anywhere else in the file and replace it
pattern2 = r'(<img[^>]*src=")data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAoAAAAKACAIAAACDr150AACAAElEQVR4nLS9eZPkyW0lCHh[^"]+(")' 
new_html2, count2 = re.subn(pattern2, r'\g<1>' + dest_file.replace('\\', '/') + r'\g<2>', new_html)
if count2 > 0:
    print(f'Replaced {count2} other identical base64 images.')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html2)

print("Finished processing index.html.")
