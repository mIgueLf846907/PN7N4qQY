# 代码生成时间: 2025-09-16 02:35:57
import os
import zipfile
import tarfile
import gr
from gr import File
from gr import Interface

"""
压缩文件解压工具
==========================
本程序使用Python和Gradio框架，实现一个压缩文件解压工具。
支持zip和tar.gz格式文件的解压。
"""

class DecompressionTool:
    def __init__(self):
        # 初始化解压目录
        self.extract_dir = "extracted_files"
        if not os.path.exists(self.extract_dir):
            os.makedirs(self.extract_dir)

    def decompress_zip(self, file_path):
        """解压缩zip文件"""
        try:
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(self.extract_dir)
            return f"成功解压zip文件到 {self.extract_dir} 目录"
        except zipfile.BadZipFile:
            return "文件损坏，无法解压zip文件"
        except Exception as e:
            return f"解压zip文件时发生错误：{e}"

    def decompress_tar(self, file_path):
        """解压缩tar.gz文件"""
        try:
            with tarfile.open(file_path, 'r:gz') as tar_ref:
                tar_ref.extractall(self.extract_dir)
            return f"成功解压tar.gz文件到 {self.extract_dir} 目录"
        except tarfile.ReadError:
            return "文件损坏，无法解压tar.gz文件"
        except Exception as e:
            return f"解压tar.gz文件时发生错误：{e}"

    def decompress_file(self, file):
        """根据文件类型解压文件"""
        file_path = os.path.join(self.extract_dir, file.name)
        with open(file_path, 'wb') as f:
            f.write(file.read())
        
        if file_path.endswith(".zip\):
            return self.decompress_zip(file_path)
        elif file_path.endswith(".tar.gz"):
            return self.decompress_tar(file_path)
        else:
            return "不支持的文件格式"

def main():
    # 创建解压工具实例
    decompressor = DecompressionTool()

    # 定义Gradio界面
    demo = Interface(
        fn=lambda file: decompressor.decompress_file(file),
        inputs=File(label="上传压缩文件"),
        outputs="text"
    )
    demo.launch()

if __name__ == "__main__":
    main()
