import os
from PIL import Image

SUPPORTED_FORMATS = {'jpeg', 'png', 'bmp', 'gif', 'webp'}

def resize_and_convert_images(folder_path, width, output_folder, output_format='webp', lossless=False, quality=75):
    if output_format not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported format: {output_format}. Supported formats are: {SUPPORTED_FORMATS}")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            original_path = os.path.join(folder_path, filename)
            with Image.open(original_path) as img:
                # 计算新的尺寸
                ratio = width / img.width
                new_height = int(img.height * ratio)

                # 调整图片大小并转换格式
                img_resized = img.resize((width, new_height))
                output_filename = os.path.splitext(filename)[0] + f'.{output_format}'
                output_path = os.path.join(output_folder, output_filename)

                # 根据是否无损以及压缩质量来保存图片
                if output_format == 'webp':
                    if lossless:
                        img_resized.save(output_path, 'WEBP', lossless=True)
                    else:
                        img_resized.save(output_path, 'WEBP', quality=quality)
                else:
                    img_resized.save(output_path, output_format.upper())

                print(f'Processed {filename} -> {output_filename}')

# 使用示例
folder_path = 'path/to/your/images'  # 更改为您的图片文件夹路径
output_width = 1600  # 您希望的图片宽度
output_folder = 'path/to/output/folder'  # 输出文件夹路径
output_format = 'webp'  # 指定输出格式
lossless_compression = False  # 无损压缩设置
compression_quality = 80  # 压缩质量（仅对有损压缩有效）

resize_and_convert_images(folder_path, output_width, output_folder, output_format, lossless_compression, compression_quality)
