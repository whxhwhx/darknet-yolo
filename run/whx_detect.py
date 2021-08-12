import cv2
import darknet
import time
import numpy as np
import math
from whx_serial import my_serial
import traceback

win_title = 'YOLOv4 TINY'
#cfg_file = 'whx/yolov4-tiny.cfg'
#data_file = 'whx/voc.data'
#weight_file = 'whx/yolov4-tiny_last_cut.weights'
cfg_file = 'whx/yolov3-tiny_final.cfg'
data_file = 'whx/voc.data'
weight_file = 'whx/yolov3-tiny_last_6300_98.weights'
thre = 0.3
show_coordinates = True

network, class_names, class_colors = darknet.load_network(
        cfg_file,
        data_file,
        weight_file,
        batch_size=1
    )

width = darknet.network_width(network)
height = darknet.network_height(network)	

cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
# cap.set(cv2.CAP_PROP_EXPOSURE, -8)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # 宽度
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

se=my_serial()

def gamma_trans(img, gamma):  # gamma函数处理
    gamma_table = [np.power(x / 255.0, gamma) * 255.0 for x in range(256)]  # 建立映射表
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)  # 颜色值为整数
    return cv2.LUT(img, gamma_table)  # 图片颜色查表。另外可以根据光强（颜色）均匀化原则设计自适应算法

def switch_id(label):
    if label=='peel':
        return 1
    if label=='cup':
        return 2
    if label=='spitball':
        return 3
    if label=='battery':
        return 4
    if label=='bottle':
        return 5
    else:
        raise ValueError('unkown type')

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: 
            break

        t_prev = time.time()
            
        #img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        #mean = np.mean(img_gray)
        #gamma_val = math.log10(0.6) / math.log10(mean / 255)  # 公式计算gamma
        #frame = gamma_trans(frame, gamma_val)  # gamma变

        frame_rgb = cv2.cvtColor( frame, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize( frame_rgb, (width, height))
            
        darknet_image = darknet.make_image(width, height, 3)
        darknet.copy_image_from_bytes(darknet_image, frame_resized.tobytes())
            
        detections = darknet.detect_image(network, class_names, darknet_image, thresh=thre)

        print('-----------------------------------------------')
        print("find %s object" %(len(detections)))
        # closest = detections[0] if len(detections)!=0 else 0
        if len(detections) !=0:
            min_object=0
            min_bottom=0
            for d in detections:
                x, y, w, h = d[2]
                ymax = int(round(y + (h / 2)))
                bottom = ymax if ymax<416 else 416
                if abs(bottom-min_bottom)<=4 and min_object!=0:
                    print("======================================")
                    print("======================================")
                    print("======================================")
                    if d[1]>min_object[1]:
                        min_bottom = bottom
                        min_object = d
                elif bottom>min_bottom:
                    min_bottom = bottom
                    min_object = d

            # se.send_data(("closest==>id:%s center:(%d, %d) bottom:(%d)\n" %(min_object[0], min_object[2][0],min_object[2][1], min_bottom)).encode('utf-8'))

            se.send_data(bytes.fromhex('aa'))
            se.send_data(bytes.fromhex('55'))

            se.write_int(switch_id(min_object[0]))
            se.write_int(int(min_object[2][0]))
            se.write_int(int(min_object[2][1]))
            se.write_int(int(min_bottom))
            print("closet==>id:%s center:(%d, %d) bottom:(%.2f)" %(min_object[0],min_object[2][0],min_object[2][1], min_bottom))
        else:
            # se.send_data("closest==>none\n".encode('utf-8'))
            se.send_data(bytes.fromhex('aa'))
            se.send_data(bytes.fromhex('55'))
            se.send_data(bytes.fromhex('00'))
            se.send_data(bytes.fromhex('00'))
            se.send_data(bytes.fromhex('00'))
            se.send_data(bytes.fromhex('00'))
            se.send_data(bytes.fromhex('00'))
            se.send_data(bytes.fromhex('00'))
            se.send_data(bytes.fromhex('00'))
            se.send_data(bytes.fromhex('00'))

        # darknet.print_detections(detections, show_coordinates)
        darknet.free_image(darknet_image)
            
        image = darknet.draw_boxes(detections, frame_resized, class_colors)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
        fps = int(1/(time.time()-t_prev))
        # print("fps:%s" %(fps))
        cv2.rectangle(image, (5, 5), (75, 25), (0,0,0), -1)
        cv2.putText(image, f'FPS {fps}', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.imshow(win_title, image)

        if cv2.waitKey(1) == ord('q'):
            break
except Exception as e:
    print('error in while loop : ', e)
    print(traceback.print_exc())

finally:
    se.close()
    cv2.destroyAllWindows()
    cap.release()	
