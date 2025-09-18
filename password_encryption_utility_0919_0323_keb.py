# 代码生成时间: 2025-09-19 03:23:43
import hashlib
import base64
import grradio as gr
from cryptography.fernet import Fernet


# 函数：生成密钥和密钥文件
def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)
    return key


# 函数：从文件中加载密钥
def load_key():
    try:
        return open('secret.key', 'rb').read()
    except FileNotFoundError:
        return generate_key()


# 函数：加密文本
def encrypt_text(text):    
    try:
        key = load_key()
        f = Fernet(key)
        encrypted_text = f.encrypt(text.encode())
        return base64.b64encode(encrypted_text).decode()
    except Exception as e:
        return f"Error: {e}"


# 函数：解密文本
def decrypt_text(encrypted_text):    
    try:
        key = load_key()
        f = Fernet(key)
        encrypted_text_bytes = base64.b64decode(encrypted_text)
        decrypted_text = f.decrypt(encrypted_text_bytes)
        return decrypted_text.decode()
    except Exception as e:
        return f"Error: {e}"


# 函数：创建Grradio界面
def create_gr_interface():
    # 创建输入输出接口
    input_text = gr.Textbox(label='Enter text')
    encrypted_text = gr.Textbox(label='Encrypted text')
    decrypted_text = gr.Textbox(label='Decrypted text')

    # 绑定函数到按钮
    def on_encrypt():
        encrypted = encrypt_text(input_text.value)
        encrypted_text.value = encrypted

    def on_decrypt():
        decrypted = decrypt_text(encrypted_text.value)
        decrypted_text.value = decrypted

    # 创建按钮
    encrypt_button = gr.Button('Encrypt')
    decrypt_button = gr.Button('Decrypt')
    encrypt_button.click(on_encrypt, inputs=[input_text], outputs=[encrypted_text])
    decrypt_button.click(on_decrypt, inputs=[encrypted_text], outputs=[decrypted_text])

    # 展示界面
    iface = gr.Interface(
        fn=lambda x: x,  # 占位函数，因为Grradio不支持空界面
        inputs=[input_text],
        outputs=[decrypted_text],
        live=True
    )
    iface.launch()


# 程序入口
if __name__ == '__main__':
    create_gr_interface()
