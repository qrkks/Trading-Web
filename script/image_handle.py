import os
from PIL import Image

def resize_and_convert_images(folder_path, width, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            original_path = os.path.join(folder_path, filename)
            with Image.open(original_path) as img:
                # 计算新的尺寸
                ratio = width / img.width
                new_height = int(img.height * ratio)

                # 调整图片大小并转换为WebP
                img_resized = img.resize((width, new_height), Image.ANTIALIAS)
                output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.webp')
                img_resized.save(output_path, 'WEBP')

                print(f'Processed {filename} -> {os.path.basename(output_path)}')

# 使用示例
folder_path = 'path/to/your/images'  # 将此路径更改为包含图片的文件夹
output_width = 800  # 您想要的图片宽度
output_folder = 'path/to/output/folder'  # 输出文件夹路径

resize_and_convert_images(folder_path, output_width, output_folder)
