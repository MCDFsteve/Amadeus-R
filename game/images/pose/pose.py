import os
import subprocess

# 获取脚本所在的目录
script_dir = os.path.dirname(os.path.realpath(__file__))

# 输入文件夹和输出文件夹的路径
input_folder = os.path.join(script_dir, '/Library/Afolder/RenpyProject/Amadeus/game/images/pose/1')
output_folder = os.path.join(script_dir, '/Library/Afolder/RenpyProject/Amadeus/game/images/pose/2')

# 确保输出文件夹存在，如果不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith('.png'):
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + '.avif'
        output_path = os.path.join(output_folder, output_filename)
        
        # 使用ImageMagick进行格式转换，并保留透明度信息
        subprocess.run(['magick', 'convert', input_path, '-define', 'avif:codec=libaom-av1', output_path])

print("转换完成！")
