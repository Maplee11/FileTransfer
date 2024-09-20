import tkinter as tk
import pyperclip
import subprocess
import os


def get_device_ip():
    res = subprocess.run(
        "ipconfig",
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    res = res.stdout.split("IPv4 地址")[1]
    res = res.split(": ")[1]
    res = res.split('\n')[0]
    return res


def display_url(url):
    root = tk.Tk()
    root.title("文件传输")

    url_label = tk.Label(root, text="关闭此窗口将会结束程序, 请等待文件传输完毕后再关闭此窗口", wraplength=800, justify="center")
    url_label.pack(pady=10)

    url_label = tk.Label(root, text="请在手机或其他设备的浏览器中打开此链接", wraplength=800, justify="center")
    url_label.pack(pady=10)
    root.geometry("400x200")

    url_label = tk.Label(root, text=url, wraplength=800, justify="center")
    url_label.pack(pady=10)

    copy_button = tk.Button(root, text="复制", command=pyperclip.copy(url))
    copy_button.pack(pady=10)
    root.mainloop()


def main():
    # 如果发生错误, 请更换端口
    port = 8861
    ip = get_device_ip()
    url = f"http://{ip}:{port}"

    upload_directory = "D:\\GitClone"
    os.chdir(upload_directory)

    http_server = subprocess.Popen(
        f"python -m http.server {port}",
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    display_url(url)

    http_server.terminate()

    print("程序已关闭")


if __name__ == "__main__":
    main()
