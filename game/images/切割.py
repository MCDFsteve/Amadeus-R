from PIL import Image
import os

def split_image(input_folder, output_folder):
    # 获取输入文件夹中的所有图片文件
    image_files = [f for f in os.listdir(input_folder) if f.endswith(".png")]
    
    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)
    
    # 切割图片并保存
    count = 1
    for image_file in image_files:
        # 打开原始图片
        image_path = os.path.join(input_folder, image_file)
        image = Image.open(image_path)
        
        # 确定每个小图片的宽度和高度
        width, height = image.size
        small_width = width // 5
        small_height = height // 5
        
        for i in range(5):
            for j in range(5):
                # 计算切割区域的坐标
                left = j * small_width
                upper = i * small_height
                right = left + small_width
                lower = upper + small_height
                
                # 切割图片
                small_image = image.crop((left, upper, right, lower))
                
                # 保存切割后的图片
                filename = f"{count:02d}.png"
                output_path = os.path.join(output_folder, filename)
                small_image.save(output_path)
                
                count += 1

# 调用函数进行图片切割
input_folder = r"D:\Renpy\Amadeus\game\images\anime"
output_folder = r"D:\Renpy\Amadeus\game\images\anime\output"
split_image(input_folder, output_folder)