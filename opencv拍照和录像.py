import cv2
import os

"""
使用函数 cap.get(propId) 来获得视频的一些参数信息,propId 可以是 0 到 18 之间的任何整数,参照下表
• CV_CAP_PROP_POS_FRAMES 
• CV_CAP_PROP_POS_AVI_RATIO
• CV_CAP_PROP_FRAME_WIDTH 
• CV_CAP_PROP_FRAME_HEIGHT
• CV_CAP_PROP_FPS
• CV_CAP_PROP_FOURCC
• CV_CAP_PROP_FRAME_COUNT
• CV_CAP_PROP_FORMAT
• CV_CAP_PROP_MODE
• CV_CAP_PROP_BRIGHTNESS
• CV_CAP_PROP_CONTRAST
• CV_CAP_PROP_SATURATION
• CV_CAP_PROP_HUE
• CV_CAP_PROP_GAIN
• CV_CAP_PROP_EXPOSURE Exposure
• CV_CAP_PROP_CONVERT_RGB
• CV_CAP_PROP_WHITE_BALANCE
• CV_CAP_PROP_RECTIFICATION
"""


def make_dirFile(file='videos_and_photos'):
    """在当前工程目录下创建文件夹"""
    pypath = os.path.dirname(os.path.abspath(__file__))  # 获取当前py文件的工作路径
    print(pypath)
    class_name = pypath + '\\' + file
    if os.path.exists(class_name) is False:  # 若文件夹不存在,则创立一个
        os.mkdir(class_name)
    return class_name


def make_photo():
    """使用opencv拍照"""
    cap = cv2.VideoCapture(0)  # 默认的摄像头
    print('FRAME_WIDTH:', cap.get(3))  # 3:代表CV_CAP_PROP_FRAME_WIDTH
    print('FRAME_HEIGHT:', cap.get(4))  # 4:代表CV_CAP_PROP_FRAME_HEIGHT
    num = 1
    while True:
        ret, frame = cap.read()
        if ret:
            # 一帧图片进行镜像(拍到的和实际的要一致需要如此操作)
            frame = cv2.flip(frame, 1, dst=None)  # 1:水平翻转,0:垂直翻转,-1:水平垂直翻转
            cv2.imshow("capture", frame)  # 弹窗口
            # 等待按下空格键操作关闭摄像头
            # if cv2.waitKey(1) & 0xFF == ord(' '):
            if num < 11:
                file_name = "%d.jpg" % num
                num += 1
                file_path = make_dirFile(file='videos_and_photos') + '\\' + file_name
                cv2.imwrite(file_path, frame)
            else:
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()


def make_video():
    """使用opencv录像"""
    cap = cv2.VideoCapture(0)  # 默认的摄像头
    # 指定视频代码
    fourcc = cv2.VideoWriter_fourcc(*"DIVX")
    # VideoWriter这个类:(参数信息)
    # (保存的文件的路径, 指定编码器, 视频的帧率, 文件的画面尺寸,黑白画面还是彩色的画面)
    # -> <VideoWriter object>
    video_name = 'chenshun.avi'
    video_patn = make_dirFile(file='videos_and_photos') + '\\' + video_name
    out = cv2.VideoWriter(video_patn, fourcc, 20.0, (640, 480))
    # while (cap.isOpened()):
    while cap.isOpened() is True:
        ret, frame = cap.read()
        if ret:
            # 一帧图片进行镜像(拍到的和实际的要一致需要如此操作)
            frame = cv2.flip(frame, 1, dst=None)  # 1:水平翻转,0:垂直翻转,-1:水平垂直翻转
            out.write(frame)
            #
            cv2.imshow('frame', frame)
            # 等待按下空格键操作关闭摄像头
            if cv2.waitKey(1) & 0xFF == ord(' '):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':

    # make_video()
    make_photo()
    # print(make_dirFile('videos_and_photos'))
