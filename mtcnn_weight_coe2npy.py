import numpy as np

def hex2int(sram_list):
    change_sram_list = []
    for i in range(len(sram_list)):
        foo = sram_list[i].replace(',', '')
        foo = foo.replace(';', '')
        foo = [np.int8(int(foo[x*2:x*2+2], 16)) for x in range(16)]
        foo.reverse()
        change_sram_list.append(foo)
    return change_sram_list

def int2float(sram_list, shift_bits):
    change_sram_list = []
    for i in range(len(sram_list)):
        foo = [(x/16)/(2**shift_bits) for x in sram_list[i]]
        change_sram_list.append(foo)
    return change_sram_list


# sram4 = open('sram4_test11.coe', 'r')
# sram5 = open('sram5_test11.coe', 'r')
# sram6 = open('sram6_test11.coe', 'r')
sram4 = open('1129_sram4.txt', 'r')
sram5 = open('1129_sram5.txt', 'r')
sram6 = open('1129_sram6.txt', 'r')

sram4_list = np.array(sram4.read().splitlines())
sram5_list = np.array(sram5.read().splitlines())
sram6_list = np.array(sram6.read().splitlines())

change_sram4_list = hex2int(sram4_list[-2967:])
change_sram5_list = hex2int(sram5_list[-4608:])
change_sram6_list = hex2int(sram6_list[-43:])

pnet_conv1 = int2float(change_sram4_list[:14], 2)
pnet_conv1 = np.array(pnet_conv1).flatten()[:216]
pnet_conv1 = np.transpose(np.reshape(pnet_conv1, (3,8,3,3)), (3,2,0,1))

pnet_conv2 = int2float(change_sram4_list[14:86], 3)
pnet_conv2 = np.array(pnet_conv2).flatten()
pnet_conv2 = np.transpose(np.reshape(pnet_conv2, (8,16,3,3)), (3,2,0,1))

pnet_conv3 = int2float(change_sram4_list[86:374], 4)
pnet_conv3 = np.array(pnet_conv3).flatten()
pnet_conv3_1 = pnet_conv3[:2304]
pnet_conv3_2 = pnet_conv3[2304:4608]
pnet_conv3_1 = np.transpose(np.reshape(pnet_conv3_1, (16,16,3,3)), (3,2,0,1))
pnet_conv3_2 = np.transpose(np.reshape(pnet_conv3_2, (16,16,3,3)), (3,2,0,1))
pnet_conv3 = []
pnet_conv3 = np.append(pnet_conv3_1, pnet_conv3_2, axis=3)

pnet_conv4 = int2float(change_sram4_list[374:378], 4)
pnet_conv4 = np.array(pnet_conv4).flatten()
pnet_conv4 = np.transpose(np.reshape(pnet_conv4, (2,32,1,1)), (2,3,1,0))

pnet_conv5 = int2float(change_sram4_list[378:386], 6)
pnet_conv5 = np.array(pnet_conv5).flatten()
pnet_conv5 = np.transpose(np.reshape(pnet_conv5, (4,32,1,1)), (2,3,1,0))

rnet_conv1 = int2float(change_sram4_list[386:435], 4)
rnet_conv1 = np.array(rnet_conv1).flatten()
rnet_conv1_1 = rnet_conv1[:432]
rnet_conv1_2 = rnet_conv1[432:756]
rnet_conv1_1 = np.transpose(np.reshape(rnet_conv1_1, (3,16,3,3)), (3,2,0,1))
rnet_conv1_2 = np.transpose(np.reshape(rnet_conv1_2, (3,12,3,3)), (3,2,0,1))
rnet_conv1 = np.append(rnet_conv1_1, rnet_conv1_2, axis=3)

rnet_conv2 = int2float(change_sram4_list[435:1191], 5)
rnet_conv2 = np.array(rnet_conv2).flatten()
rnet_conv2_1 = rnet_conv2[ : 4032]
rnet_conv2_2 = rnet_conv2[4032 : 8064]
rnet_conv2_3 = rnet_conv2[8064 : 12096]
rnet_conv2_1 = np.transpose(np.reshape(rnet_conv2_1, (28,16,3,3)), (3,2,0,1))
rnet_conv2_2 = np.transpose(np.reshape(rnet_conv2_2, (28,16,3,3)), (3,2,0,1))
rnet_conv2_3 = np.transpose(np.reshape(rnet_conv2_3, (28,16,3,3)), (3,2,0,1))
rnet_conv2 = np.append(rnet_conv2_1, rnet_conv2_2, axis=3)
rnet_conv2 = np.append(rnet_conv2, rnet_conv2_3, axis=3)

rnet_conv3 = int2float(change_sram4_list[1191:2919], 5)
rnet_conv3 = np.array(rnet_conv3).flatten()
rnet_conv3_1 = rnet_conv3[ : 6912]
rnet_conv3_2 = rnet_conv3[6912 : 6912*2]
rnet_conv3_3 = rnet_conv3[6912*2 : 6912*3]
rnet_conv3_4 = rnet_conv3[6912*3 : 6912*4]
rnet_conv3_1 = np.transpose(np.reshape(rnet_conv3_1, (48,16,3,3)), (3,2,0,1))
rnet_conv3_2 = np.transpose(np.reshape(rnet_conv3_2, (48,16,3,3)), (3,2,0,1))
rnet_conv3_3 = np.transpose(np.reshape(rnet_conv3_3, (48,16,3,3)), (3,2,0,1))
rnet_conv3_4 = np.transpose(np.reshape(rnet_conv3_4, (48,16,3,3)), (3,2,0,1))
rnet_conv3 = np.append(rnet_conv3_1, rnet_conv3_2, axis=3)
rnet_conv3 = np.append(rnet_conv3, rnet_conv3_3, axis=3)
rnet_conv3 = np.append(rnet_conv3, rnet_conv3_4, axis=3)

rnet_fc1 = int2float(change_sram5_list, 6)
rnet_fc1 = np.array(rnet_fc1).flatten()
rnet_fc1 = np.transpose(np.reshape(rnet_fc1, (128, 576)), (1,0))

rnet_fc2 = int2float(change_sram4_list[2919:2935], 3)
rnet_fc2 = np.array(rnet_fc2).flatten()
rnet_fc2 = np.transpose(np.reshape(rnet_fc2, (2, 128)), (1,0))

rnet_fc3 = int2float(change_sram4_list[2935:2967], 4)
rnet_fc3 = np.array(rnet_fc3).flatten()
rnet_fc3 = np.transpose(np.reshape(rnet_fc3, (4, 128)), (1,0))

pnet_bias1 = int2float(change_sram6_list[:1], 3)
pnet_bias1 = np.append(pnet_bias1[0][:4], pnet_bias1[0][8:12])
pnet_bias1 = np.array(pnet_bias1).flatten()

pnet_act1 = int2float(change_sram6_list[:1], 3)
pnet_act1 = np.array(pnet_act1).flatten()
pnet_act1 = np.append(pnet_act1[4:8], pnet_act1[12:16])
pnet_act1 = np.reshape(pnet_act1, (1,1,-1))

pnet_bias2 = int2float(change_sram6_list[1:3], 1)
pnet_bias2_fl = np.array(pnet_bias2).flatten()
pnet_bias2 = []
for i in range(4):
    pnet_bias2.append(pnet_bias2_fl[i*8:i*8+4])
pnet_bias2 = np.array(pnet_bias2).flatten()

pnet_act2 = int2float(change_sram6_list[1:3], 4)
pnet_act2_fl = np.array(pnet_act2).flatten()
pnet_act2 = []
for i in range(4):
    pnet_act2.append(pnet_act2_fl[i*8+4:i*8+8])
pnet_act2 = np.array(pnet_act2).flatten()
pnet_act2 = np.reshape(pnet_act2, (1,1,-1))

pnet_bias3 = int2float(change_sram6_list[3:7], 2)
pnet_bias3_fl = np.array(pnet_bias3).flatten()
pnet_bias3 = []
for i in range(8):
    pnet_bias3.append(pnet_bias3_fl[i*8:i*8+4])
pnet_bias3 = np.array(pnet_bias3).flatten()

pnet_act3 = int2float(change_sram6_list[3:7], 4)
pnet_act3_fl = np.array(pnet_act3).flatten()
pnet_act3 = []
for i in range(8):
    pnet_act3.append(pnet_act3_fl[i*8+4:i*8+8])
pnet_act3 = np.array(pnet_act3).flatten()
pnet_act3 = np.reshape(pnet_act3, (1,1,-1))

pnet_bias4 = int2float(change_sram6_list[7:8], 7)
pnet_bias4_fl = np.array(pnet_bias4).flatten()
pnet_bias4 = pnet_bias4_fl[:2]
pnet_bias5 = pnet_bias4_fl[2:6]

rnet_bias1 = int2float(change_sram6_list[8:12], 4)
rnet_bias1_fl = np.array(rnet_bias1).flatten()
rnet_bias1 = []
for i in range(7):
    rnet_bias1.append(rnet_bias1_fl[i*8:i*8+4])
rnet_bias1 = np.array(rnet_bias1).flatten()

rnet_act1 = int2float(change_sram6_list[8:12], 2)
rnet_act1_fl = np.array(rnet_act1).flatten()
rnet_act1 = []
for i in range(7):
    rnet_act1.append(rnet_act1_fl[i*8+4:i*8+8])
rnet_act1 = np.array(rnet_act1).flatten()
rnet_act1 = np.reshape(rnet_act1, (1,1,-1))

rnet_bias2 = int2float(change_sram6_list[12:18], 4)
rnet_bias2_fl = np.array(rnet_bias2).flatten()
rnet_bias2 = []
for i in range(12):
    rnet_bias2.append(rnet_bias2_fl[i*8:i*8+4])
rnet_bias2 = np.array(rnet_bias2).flatten()

rnet_act2 = int2float(change_sram6_list[12:18], 3)
rnet_act2_fl = np.array(rnet_act2).flatten()
rnet_act2 = []
for i in range(12):
    rnet_act2.append(rnet_act2_fl[i*8+4:i*8+8])
rnet_act2 = np.array(rnet_act2).flatten()
rnet_act2 = np.reshape(rnet_act2, (1,1,-1))

rnet_bias3 = int2float(change_sram6_list[18:26], 4)
rnet_bias3_fl = np.array(rnet_bias3).flatten()
rnet_bias3 = []
for i in range(16):
    rnet_bias3.append(rnet_bias3_fl[i*8:i*8+4])
rnet_bias3 = np.array(rnet_bias3).flatten()

rnet_act3 = int2float(change_sram6_list[18:26], 4)
rnet_act3_fl = np.array(rnet_act3).flatten()
rnet_act3 = []
for i in range(16):
    rnet_act3.append(rnet_act3_fl[i*8+4:i*8+8])
rnet_act3 = np.array(rnet_act3).flatten()
rnet_act3 = np.reshape(rnet_act3, (1,1,-1))

rnet_bias4 = int2float(change_sram6_list[26:42], 4)
rnet_bias4_fl = np.array(rnet_bias4).flatten()
rnet_bias4 = []
for i in range(128):
    rnet_bias4.append(rnet_bias4_fl[i*2])
rnet_bias4 = np.array(rnet_bias4).flatten()

rnet_act4 = int2float(change_sram6_list[26:42], 3)
rnet_act4_fl = np.array(rnet_act4).flatten()
rnet_act4 = []
for i in range(128):
    rnet_act4.append(rnet_act4_fl[i*2+1])
rnet_act4 = np.array(rnet_act4).flatten()
# rnet_act4 = np.reshape(rnet_act4, (1,1,-1))

rnet_bias5 = int2float(change_sram6_list[42:43], 6)
rnet_bias5_fl = np.array(rnet_bias5).flatten()
rnet_bias5 = np.array(rnet_bias5_fl[:2]).flatten()
rnet_bias6 = np.array(rnet_bias5_fl[2:6]).flatten()

pnet = []
pnet.append(pnet_conv1)
pnet.append(pnet_bias1)
pnet.append(pnet_act1)
pnet.append(pnet_conv2)
pnet.append(pnet_bias2)
pnet.append(pnet_act2)
pnet.append(pnet_conv3)
pnet.append(pnet_bias3)
pnet.append(pnet_act3)
pnet.append(pnet_conv4)
pnet.append(pnet_bias4)
pnet.append(pnet_conv5)
pnet.append(pnet_bias5)

rnet = []
rnet.append(rnet_conv1)
rnet.append(rnet_bias1)
rnet.append(rnet_act1)
rnet.append(rnet_conv2)
rnet.append(rnet_bias2)
rnet.append(rnet_act2)
rnet.append(rnet_conv3)
rnet.append(rnet_bias3)
rnet.append(rnet_act3)
rnet.append(rnet_fc1)
rnet.append(rnet_bias4)
rnet.append(rnet_act4)
rnet.append(rnet_fc2)
rnet.append(rnet_bias5)
rnet.append(rnet_fc3)
rnet.append(rnet_bias6)

weight = {}
weight['pnet'] = pnet
weight['rnet'] = rnet

# for item in pnet:
#     print(np.shape(item))
#     print(item)
# for item in rnet:
#     print(np.shape(item))
#     print(item)

np.save('1129_coe2npy_weight', weight)
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