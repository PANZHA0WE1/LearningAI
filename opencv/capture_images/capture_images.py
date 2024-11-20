import cv2

# 定义函数
def capture_image():
    cap = cv2.VideoCapture(0) # 获取摄像头
    image_count = 1 # 定义计数器
    image_name = "001.jpg" # 定义文件名
    print("准备开始捕获图像......")

    while True: # 具体实现（循环）
        ret,frame = cap.read() # 获取图像
        cv2.imshow('Capture Preview',frame) # 显示图像
        key = cv2.waitKey(1) # 监听按键

        # 如果按下Tab键（ASCII码值为9），捕获图像
        if key == 9:
            cv2.imwrite(image_name,frame) # 保存一帧图像
            print(f"图像已保存为{image_name}")

            image_count += 1 # 自增计数器
            image_name = f"{str(image_count).zfill(3)}.jpg" # 更新文件名

        # 否则如果按下Esc键，人为退出程序
        elif key == 27:
            print(f"已采集{image_count - 1}张图像，被人为终止，程序已退出。")
            break

    # 释放资源
    cap.release()
    cv2.destroyAllWindows()

# 此函数仅在直接运行时被调用
if __name__ == "__main__":
    capture_image()