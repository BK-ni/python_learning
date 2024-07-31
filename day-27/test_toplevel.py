import tkinter as tk


def open_toplevel_window():
    # 创建一个 Toplevel 窗口
    top_window = tk.Toplevel(root)
    top_window.title("Toplevel Window")
    top_window.minsize(width=200, height=100)

    # 在 Toplevel 窗口中添加一个标签
    label = tk.Label(top_window, text="This is a Toplevel window")
    label.pack()

    # 添加一个按钮来关闭 Toplevel 窗口
    close_button = tk.Button(top_window, text="Close", command=top_window.destroy)
    close_button.pack()


# 创建主窗口
root = tk.Tk()
root.title("Main Window")
root.minsize(width=300, height=200)

# 在主窗口中添加一个按钮来打开 Toplevel 窗口
open_button = tk.Button(root, text="Open Toplevel", command=open_toplevel_window)
open_button.pack()

# 进入主事件循环
root.mainloop()