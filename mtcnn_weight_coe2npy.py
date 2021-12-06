import numpy as np
import time


# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *


def hex2int(sram_list):
    change_sram_list = []
    for idx in range(len(sram_list)):
        foo = sram_list[idx].replace(',', '')
        foo = foo.replace(';', '')
        foo = [np.int8(int(foo[x * 2:x * 2 + 2], 16)) for x in range(16)]
        foo.reverse()
        change_sram_list.append(foo)
    return change_sram_list


def int2float(sram_list, divide_value):
    change_sram_list = []
    for idx in range(len(sram_list)):
        # foo = [(x / 16) / (2 ** shift_bits) for x in sram_list[idx]]
        foo = [x / divide_value for x in sram_list[idx]]
        change_sram_list.append(foo)
    return change_sram_list


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ex = WindowApp()
    # sys.exit(app.exec_())
    # print(ex.sram4_le)

    # sram4_path = input('sram4 이름(ex. sram4.coe) : ')
    # sram5_path = input('sram5 이름(ex. sram5.coe) : ')
    # sram6_path = input('sram6 이름(ex. sram6.coe) : ')
    sram4_path = 'test4_sram_bias0/sram4_test4.coe'
    sram5_path = 'test4_sram_bias0/sram5_test4.coe'
    sram6_path = 'test4_sram_bias0/sram6_test4_bias0_act0.coe'

    try:
        sram4 = open(sram4_path, 'r')
        sram5 = open(sram5_path, 'r')
        sram6 = open(sram6_path, 'r')

        pnet_conv1_sh, pnet_bias1_sh, pnet_act1_sh, pnet_conv2_sh, pnet_bias2_sh, pnet_act2_sh, \
        pnet_conv3_sh, pnet_bias3_sh, pnet_act3_sh, pnet_conv4_sh, pnet_conv5_sh, pnet_bias4_sh, pnet_bias5_sh = \
            1, 1, 1, 1, 0.5, 4, 2, 1, 4, 2, 8, 128, 32  # 2, 3, 3, 3, 1, 4, 4, 2, 4, 4, 6, 7, 7

        rnet_conv1_sh, rnet_bias1_sh, rnet_act1_sh, rnet_conv2_sh, rnet_bias2_sh, rnet_act2_sh, \
        rnet_conv3_sh, rnet_bias3_sh, rnet_act3_sh, rnet_fc1_sh, rnet_bias4_sh, rnet_act4_sh, \
        rnet_fc2_sh, rnet_fc3_sh, rnet_bias5_sh, rnet_bias6_sh = \
            2, 4, 1, 4, 4, 2, 4, 4, 2, 8, 4, 2, 2, 4, 16, 8  # 4, 4, 2, 5, 4, 3, 5, 4, 4, 6, 4, 3, 3, 4, 6, 6

        sram4_list = np.array(sram4.read().strip().splitlines())
        sram5_list = np.array(sram5.read().strip().splitlines())
        sram6_list = np.array(sram6.read().strip().splitlines())

        change_sram4_list = np.array(hex2int(sram4_list[-2967:])) / 64
        change_sram5_list = np.array(hex2int(sram5_list[-4608:])) / 64
        change_sram6_list = np.array(hex2int(sram6_list[-43:])) / 64

        pnet_conv1 = int2float(change_sram4_list[:14], pnet_conv1_sh)
        pnet_conv1 = np.array(pnet_conv1).flatten()[:216]
        pnet_conv1 = np.transpose(np.reshape(pnet_conv1, (3, 8, 3, 3)), (3, 2, 0, 1))

        pnet_conv2 = int2float(change_sram4_list[14:86], pnet_conv2_sh)
        pnet_conv2 = np.array(pnet_conv2).flatten()
        pnet_conv2 = np.transpose(np.reshape(pnet_conv2, (8, 16, 3, 3)), (3, 2, 0, 1))

        pnet_conv3 = int2float(change_sram4_list[86:374], pnet_conv3_sh)
        pnet_conv3 = np.array(pnet_conv3).flatten()
        pnet_conv3_1 = pnet_conv3[:2304]
        pnet_conv3_2 = pnet_conv3[2304:4608]
        pnet_conv3_1 = np.transpose(np.reshape(pnet_conv3_1, (16, 16, 3, 3)), (3, 2, 0, 1))
        pnet_conv3_2 = np.transpose(np.reshape(pnet_conv3_2, (16, 16, 3, 3)), (3, 2, 0, 1))
        pnet_conv3 = []
        pnet_conv3 = np.append(pnet_conv3_1, pnet_conv3_2, axis=3)

        pnet_conv4 = int2float(change_sram4_list[374:378], pnet_conv4_sh)
        pnet_conv4 = np.array(pnet_conv4).flatten()
        pnet_conv4 = np.transpose(np.reshape(pnet_conv4, (2, 32, 1, 1)), (2, 3, 1, 0))

        pnet_conv5 = int2float(change_sram4_list[378:386], pnet_conv5_sh)
        pnet_conv5 = np.array(pnet_conv5).flatten()
        pnet_conv5 = np.transpose(np.reshape(pnet_conv5, (4, 32, 1, 1)), (2, 3, 1, 0))

        rnet_conv1 = int2float(change_sram4_list[386:435], rnet_conv1_sh)
        rnet_conv1 = np.array(rnet_conv1).flatten()
        rnet_conv1_1 = rnet_conv1[:432]
        rnet_conv1_2 = rnet_conv1[432:756]
        rnet_conv1_1 = np.transpose(np.reshape(rnet_conv1_1, (3, 16, 3, 3)), (3, 2, 0, 1))
        rnet_conv1_2 = np.transpose(np.reshape(rnet_conv1_2, (3, 12, 3, 3)), (3, 2, 0, 1))
        rnet_conv1 = np.append(rnet_conv1_1, rnet_conv1_2, axis=3)

        rnet_conv2 = int2float(change_sram4_list[435:1191], rnet_conv2_sh)
        rnet_conv2 = np.array(rnet_conv2).flatten()
        rnet_conv2_1 = rnet_conv2[: 4032]
        rnet_conv2_2 = rnet_conv2[4032: 8064]
        rnet_conv2_3 = rnet_conv2[8064: 12096]
        rnet_conv2_1 = np.transpose(np.reshape(rnet_conv2_1, (28, 16, 3, 3)), (3, 2, 0, 1))
        rnet_conv2_2 = np.transpose(np.reshape(rnet_conv2_2, (28, 16, 3, 3)), (3, 2, 0, 1))
        rnet_conv2_3 = np.transpose(np.reshape(rnet_conv2_3, (28, 16, 3, 3)), (3, 2, 0, 1))
        rnet_conv2 = np.append(rnet_conv2_1, rnet_conv2_2, axis=3)
        rnet_conv2 = np.append(rnet_conv2, rnet_conv2_3, axis=3)

        rnet_conv3 = int2float(change_sram4_list[1191:2919], rnet_conv3_sh)
        rnet_conv3 = np.array(rnet_conv3).flatten()
        rnet_conv3_1 = rnet_conv3[: 6912]
        rnet_conv3_2 = rnet_conv3[6912: 6912 * 2]
        rnet_conv3_3 = rnet_conv3[6912 * 2: 6912 * 3]
        rnet_conv3_4 = rnet_conv3[6912 * 3: 6912 * 4]
        rnet_conv3_1 = np.transpose(np.reshape(rnet_conv3_1, (48, 16, 3, 3)), (3, 2, 0, 1))
        rnet_conv3_2 = np.transpose(np.reshape(rnet_conv3_2, (48, 16, 3, 3)), (3, 2, 0, 1))
        rnet_conv3_3 = np.transpose(np.reshape(rnet_conv3_3, (48, 16, 3, 3)), (3, 2, 0, 1))
        rnet_conv3_4 = np.transpose(np.reshape(rnet_conv3_4, (48, 16, 3, 3)), (3, 2, 0, 1))
        rnet_conv3 = np.append(rnet_conv3_1, rnet_conv3_2, axis=3)
        rnet_conv3 = np.append(rnet_conv3, rnet_conv3_3, axis=3)
        rnet_conv3 = np.append(rnet_conv3, rnet_conv3_4, axis=3)
        rnet_conv3 = np.delete(rnet_conv3, (2), axis=0)
        rnet_conv3 = np.delete(rnet_conv3, (2), axis=1)
        print(rnet_conv3.shape)

        rnet_fc1 = int2float(change_sram5_list, rnet_fc1_sh)
        rnet_fc1 = np.array(rnet_fc1).flatten()
        rnet_fc1 = np.transpose(np.reshape(rnet_fc1, (128, 576)), (1, 0))

        rnet_fc2 = int2float(change_sram4_list[2919:2935], rnet_fc2_sh)
        rnet_fc2 = np.array(rnet_fc2).flatten()
        rnet_fc2 = np.transpose(np.reshape(rnet_fc2, (2, 128)), (1, 0))

        rnet_fc3 = int2float(change_sram4_list[2935:2967], rnet_fc3_sh)
        rnet_fc3 = np.array(rnet_fc3).flatten()
        rnet_fc3 = np.transpose(np.reshape(rnet_fc3, (4, 128)), (1, 0))

        pnet_bias1 = int2float(change_sram6_list[:1], pnet_bias1_sh)
        pnet_bias1 = np.append(pnet_bias1[0][:4], pnet_bias1[0][8:12])
        pnet_bias1 = np.array(pnet_bias1).flatten()

        pnet_act1 = int2float(change_sram6_list[:1], pnet_act1_sh)
        pnet_act1 = np.array(pnet_act1).flatten()
        pnet_act1 = np.append(pnet_act1[4:8], pnet_act1[12:16])
        pnet_act1 = np.reshape(pnet_act1, (1, 1, -1))

        pnet_bias2 = int2float(change_sram6_list[1:3], pnet_bias2_sh)
        pnet_bias2_fl = np.array(pnet_bias2).flatten()
        pnet_bias2 = []
        for i in range(4):
            pnet_bias2.append(pnet_bias2_fl[i * 8:i * 8 + 4])
        pnet_bias2 = np.array(pnet_bias2).flatten()

        pnet_act2 = int2float(change_sram6_list[1:3], pnet_act2_sh)
        pnet_act2_fl = np.array(pnet_act2).flatten()
        pnet_act2 = []
        for i in range(4):
            pnet_act2.append(pnet_act2_fl[i * 8 + 4:i * 8 + 8])
        pnet_act2 = np.array(pnet_act2).flatten()
        pnet_act2 = np.reshape(pnet_act2, (1, 1, -1))

        pnet_bias3 = int2float(change_sram6_list[3:7], pnet_bias3_sh)
        pnet_bias3_fl = np.array(pnet_bias3).flatten()
        pnet_bias3 = []
        for i in range(8):
            pnet_bias3.append(pnet_bias3_fl[i * 8:i * 8 + 4])
        pnet_bias3 = np.array(pnet_bias3).flatten()

        pnet_act3 = int2float(change_sram6_list[3:7], pnet_act3_sh)
        pnet_act3_fl = np.array(pnet_act3).flatten()
        pnet_act3 = []
        for i in range(8):
            pnet_act3.append(pnet_act3_fl[i * 8 + 4:i * 8 + 8])
        pnet_act3 = np.array(pnet_act3).flatten()
        pnet_act3 = np.reshape(pnet_act3, (1, 1, -1))

        pnet_bias4 = int2float(change_sram6_list[7:8], pnet_bias4_sh)
        pnet_bias4_fl = np.array(pnet_bias4).flatten()
        pnet_bias4 = pnet_bias4_fl[:2]
        pnet_bias5 = pnet_bias4_fl[2:6]

        rnet_bias1 = int2float(change_sram6_list[8:12], rnet_bias1_sh)
        rnet_bias1_fl = np.array(rnet_bias1).flatten()
        rnet_bias1 = []
        for i in range(7):
            rnet_bias1.append(rnet_bias1_fl[i * 8:i * 8 + 4])
        rnet_bias1 = np.array(rnet_bias1).flatten()

        rnet_act1 = int2float(change_sram6_list[8:12], rnet_act1_sh)
        rnet_act1_fl = np.array(rnet_act1).flatten()
        rnet_act1 = []
        for i in range(7):
            rnet_act1.append(rnet_act1_fl[i * 8 + 4:i * 8 + 8])
        rnet_act1 = np.array(rnet_act1).flatten()
        rnet_act1 = np.reshape(rnet_act1, (1, 1, -1))

        rnet_bias2 = int2float(change_sram6_list[12:18], rnet_bias2_sh)
        rnet_bias2_fl = np.array(rnet_bias2).flatten()
        rnet_bias2 = []
        for i in range(12):
            rnet_bias2.append(rnet_bias2_fl[i * 8:i * 8 + 4])
        rnet_bias2 = np.array(rnet_bias2).flatten()

        rnet_act2 = int2float(change_sram6_list[12:18], rnet_act2_sh)
        rnet_act2_fl = np.array(rnet_act2).flatten()
        rnet_act2 = []
        for i in range(12):
            rnet_act2.append(rnet_act2_fl[i * 8 + 4:i * 8 + 8])
        rnet_act2 = np.array(rnet_act2).flatten()
        rnet_act2 = np.reshape(rnet_act2, (1, 1, -1))

        rnet_bias3 = int2float(change_sram6_list[18:26], rnet_bias3_sh)
        rnet_bias3_fl = np.array(rnet_bias3).flatten()
        rnet_bias3 = []
        for i in range(16):
            rnet_bias3.append(rnet_bias3_fl[i * 8:i * 8 + 4])
        rnet_bias3 = np.array(rnet_bias3).flatten()

        rnet_act3 = int2float(change_sram6_list[18:26], rnet_act3_sh)
        rnet_act3_fl = np.array(rnet_act3).flatten()
        rnet_act3 = []
        for i in range(16):
            rnet_act3.append(rnet_act3_fl[i * 8 + 4:i * 8 + 8])
        rnet_act3 = np.array(rnet_act3).flatten()
        rnet_act3 = np.reshape(rnet_act3, (1, 1, -1))

        rnet_bias4 = int2float(change_sram6_list[26:42], rnet_bias4_sh)
        rnet_bias4_fl = np.array(rnet_bias4).flatten()
        rnet_bias4 = []
        for i in range(128):
            rnet_bias4.append(rnet_bias4_fl[i * 2])
        rnet_bias4 = np.array(rnet_bias4).flatten()

        rnet_act4 = int2float(change_sram6_list[26:42], rnet_act4_sh)
        rnet_act4_fl = np.array(rnet_act4).flatten()
        rnet_act4 = []
        for i in range(128):
            rnet_act4.append(rnet_act4_fl[i * 2 + 1])
        rnet_act4 = np.array(rnet_act4).flatten()
        # rnet_act4 = np.reshape(rnet_act4, (1,1,-1))

        rnet_bias5 = int2float(change_sram6_list[42:43], rnet_bias5_sh)
        rnet_bias5_fl = np.array(rnet_bias5).flatten()
        rnet_bias5 = np.array(rnet_bias5_fl[:2]).flatten()
        rnet_bias6 = np.array(rnet_bias5_fl[2:6]).flatten()

        pnet = [pnet_conv1, pnet_bias1, pnet_act1, pnet_conv2, pnet_bias2, pnet_act2, pnet_conv3, pnet_bias3, pnet_act3,
                pnet_conv4, pnet_bias4, pnet_conv5, pnet_bias5]

        rnet = [rnet_conv1, rnet_bias1, rnet_act1, rnet_conv2, rnet_bias2, rnet_act2, rnet_conv3, rnet_bias3, rnet_act3,
                rnet_fc1, rnet_bias4, rnet_act4, rnet_fc2, rnet_bias5, rnet_fc3, rnet_bias6]

        weight = {'pnet': pnet, 'rnet': rnet}

        now = time.localtime()
        save_file_name = "%02d_%02d_%02d%02d%02d" % (now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        np.save('converted_npy/' + save_file_name + '_weight', weight)
        input('\nConvert success!\n\nPress any key...')
    except:
        input('\nConvert Fail...\n\nPress any key...')

# ======================================================================================================================
# for item in pnet:
#     print(np.shape(item))
#     print(item)
# for item in rnet:
#     print(np.shape(item))
#     print(item)
# for i in range(len(pnet)):
#     np.savetxt('pnet_weight_'+str(i)+'.txt', pnet[i], fmt='%d', delimiter='\t', newline='\n')
# # np.savetxt('pnet_weight.txt', pnet, fmt='%d', delimiter='\t', newline='\n')
# for i in range(len(rnet)):
#     np.savetxt('pnet_weight_'+str(i)+'.txt', rnet[i], fmt='%d', delimiter='\t', newline='\n')
# np.savetxt('rnet_weight.txt', rnet, fmt='%d', delimiter='\t', newline='\n')

# np.split(sram4_list[0], [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30])
# print(np.split(sram4_list[0], 16)[0])
# np.hsplit(np.reshape(foo, (1,32)), 16)
# print(sram5_list.shape)
# print(sram6_list.shape)
