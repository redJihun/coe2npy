import numpy as np

orig = np.load('p_oc_8.npy', allow_pickle=True).tolist()
# comp = np.load('1129_coe2npy_weight.npy', allow_pickle=True).tolist()
# comp = np.load('coe2npy_weight.npy', allow_pickle=True).tolist()
comp = np.load('uxfac_weights_fix_shape.npy', allow_pickle=True).tolist()
orig_pnet, orig_rnet = orig['pnet'], orig['rnet']
comp_pnet, comp_rnet = comp['pnet'], comp['rnet']

sram4_min, sram4_max = 9999999, -9999999
sram5_min, sram5_max = 9999999, -9999999
sram6_min, sram6_max = 9999999, -9999999

for i in [0, 3, 6, 9, 11]:
    try:
        for j in range(len(orig_pnet[i])):
            try:
                for k in range(len(orig_pnet[i][j])):
                    try:
                        for m in range(len(orig_pnet[i][j][k])):
                            try:
                                for n in range(len(orig_pnet[i][j][k][m])):
                                    if abs(orig_pnet[i][j][k][m][n] - comp_pnet[i][j][k][m][n]) < sram4_min:
                                        sram4_min = abs(orig_pnet[i][j][k][m][n] - comp_pnet[i][j][k][m][n])
                                    if abs(orig_pnet[i][j][k][m][n] - comp_pnet[i][j][k][m][n]) > sram4_max:
                                        sram4_max = abs(orig_pnet[i][j][k][m][n] - comp_pnet[i][j][k][m][n])
                            except:
                                if abs(orig_pnet[i][j][k][m] - comp_pnet[i][j][k][m]) < sram4_min:
                                    sram4_min = abs(orig_pnet[i][j][k][m] - comp_pnet[i][j][k][m])
                                if abs(orig_pnet[i][j][k][m] - comp_pnet[i][j][k][m]) > sram4_max:
                                    sram4_max = abs(orig_pnet[i][j][k][m] - comp_pnet[i][j][k][m])
                    except:
                        if abs(orig_pnet[i][j][k] - comp_pnet[i][j][k]) < sram4_min:
                            sram4_min = abs(orig_pnet[i][j][k] - comp_pnet[i][j][k])
                        if abs(orig_pnet[i][j][k] - comp_pnet[i][j][k]) > sram4_max:
                            sram4_max = abs(orig_pnet[i][j][k] - comp_pnet[i][j][k])
            except:
                if abs(orig_pnet[i][j] - comp_pnet[i][j]) < sram4_min:
                    sram4_min = abs(orig_pnet[i][j] - comp_pnet[i][j])
                if abs(orig_pnet[i][j] - comp_pnet[i][j]) > sram4_max:
                    sram4_max = abs(orig_pnet[i][j] - comp_pnet[i][j])
    except:
        if abs(orig_pnet[i] - comp_pnet[i]) < sram4_min:
            sram4_min = abs(orig_pnet[i] - comp_pnet[i])
        if abs(orig_pnet[i] - comp_pnet[i]) > sram4_max:
            sram4_max = abs(orig_pnet[i] - comp_pnet[i])

for i in [0, 3, 6, 12, 14]:
    try:
        for j in range(len(orig_rnet[i])):
            try:
                for k in range(len(orig_rnet[i][j])):
                    try:
                        for m in range(len(orig_rnet[i][j][k])):
                            try:
                                for n in range(len(orig_rnet[i][j][k][m])):
                                    if abs(orig_rnet[i][j][k][m][n] - comp_rnet[i][j][k][m][n]) < sram4_min:
                                        sram4_min = abs(orig_rnet[i][j][k][m][n] - comp_rnet[i][j][k][m][n])
                                    if abs(orig_rnet[i][j][k][m][n] - comp_rnet[i][j][k][m][n]) > sram4_max:
                                        sram4_max = abs(orig_rnet[i][j][k][m][n] - comp_rnet[i][j][k][m][n])
                            except:
                                if abs(orig_rnet[i][j][k][m] - comp_rnet[i][j][k][m]) < sram4_min:
                                    sram4_min = abs(orig_rnet[i][j][k][m] - comp_rnet[i][j][k][m])
                                if abs(orig_rnet[i][j][k][m] - comp_rnet[i][j][k][m]) > sram4_max:
                                    sram4_max = abs(orig_rnet[i][j][k][m] - comp_rnet[i][j][k][m])
                    except:
                        if abs(orig_rnet[i][j][k] - comp_rnet[i][j][k]) < sram4_min:
                            sram4_min = abs(orig_rnet[i][j][k] - comp_rnet[i][j][k])
                        if abs(orig_rnet[i][j][k] - comp_rnet[i][j][k]) > sram4_max:
                            sram4_max = abs(orig_rnet[i][j][k] - comp_rnet[i][j][k])
            except:
                if abs(orig_rnet[i][j] - comp_rnet[i][j]) < sram4_min:
                    sram4_min = abs(orig_rnet[i][j] - comp_rnet[i][j])
                if abs(orig_rnet[i][j] - comp_rnet[i][j]) > sram4_max:
                    sram4_max = abs(orig_rnet[i][j] - comp_rnet[i][j])
    except:
        if abs(orig_rnet[i] - comp_rnet[i]) < sram4_min:
            sram4_min = abs(orig_rnet[i] - comp_rnet[i])
        if abs(orig_rnet[i] - comp_rnet[i]) > sram4_max:
            sram4_max = abs(orig_rnet[i] - comp_rnet[i])

for i in [1,2,4,5,7,8,10,12]:
    try:
        for j in range(len(orig_pnet[i])):
            try:
                for k in range(len(orig_pnet[i][j])):
                    try:
                        for m in range(len(orig_pnet[i][j][k])):
                            try:
                                for n in range(len(orig_pnet[i][j][k][m])):
                                    if abs(orig_pnet[i][j][k][m][n] - comp_pnet[i][j][k][m][n]) < sram6_min:
                                        sram6_min = abs(orig_pnet[i][j][k][m][n] - comp_pnet[i][j][k][m][n])
                                    if abs(orig_pnet[i][j][k][m][n] - comp_pnet[i][j][k][m][n]) > sram6_max:
                                        sram6_max = abs(orig_pnet[i][j][k][m][n] - comp_pnet[i][j][k][m][n])
                            except:
                                if abs(orig_pnet[i][j][k][m] - comp_pnet[i][j][k][m]) < sram6_min:
                                    sram6_min = abs(orig_pnet[i][j][k][m] - comp_pnet[i][j][k][m])
                                if abs(orig_pnet[i][j][k][m] - comp_pnet[i][j][k][m]) > sram6_max:
                                    sram6_max = abs(orig_pnet[i][j][k][m] - comp_pnet[i][j][k][m])
                    except:
                        if abs(orig_pnet[i][j][k] - comp_pnet[i][j][k]) < sram6_min:
                            sram6_min = abs(orig_pnet[i][j][k] - comp_pnet[i][j][k])
                        if abs(orig_pnet[i][j][k] - comp_pnet[i][j][k]) > sram6_max:
                            sram6_max = abs(orig_pnet[i][j][k] - comp_pnet[i][j][k])
            except:
                if abs(orig_pnet[i][j] - comp_pnet[i][j]) < sram6_min:
                    sram6_min = abs(orig_pnet[i][j] - comp_pnet[i][j])
                if abs(orig_pnet[i][j] - comp_pnet[i][j]) > sram6_max:
                    sram6_max = abs(orig_pnet[i][j] - comp_pnet[i][j])
    except:
        if abs(orig_pnet[i] - comp_pnet[i]) < sram6_min:
            sram6_min = abs(orig_pnet[i] - comp_pnet[i])
        if abs(orig_pnet[i] - comp_pnet[i]) > sram6_max:
            sram6_max = abs(orig_pnet[i] - comp_pnet[i])

for i in [1,2,4,5,7,8,10,11,13,15]:
    try:
        for j in range(len(orig_rnet[i])):
            try:
                for k in range(len(orig_rnet[i][j])):
                    try:
                        for m in range(len(orig_rnet[i][j][k])):
                            try:
                                for n in range(len(orig_rnet[i][j][k][m])):
                                    if abs(orig_rnet[i][j][k][m][n] - comp_rnet[i][j][k][m][n]) < sram6_min:
                                        sram6_min = abs(orig_rnet[i][j][k][m][n] - comp_rnet[i][j][k][m][n])
                                    if abs(orig_rnet[i][j][k][m][n] - comp_rnet[i][j][k][m][n]) > sram6_max:
                                        sram6_max = abs(orig_rnet[i][j][k][m][n] - comp_rnet[i][j][k][m][n])
                            except:
                                if abs(orig_rnet[i][j][k][m] - comp_rnet[i][j][k][m]) < sram6_min:
                                    sram6_min = abs(orig_rnet[i][j][k][m] - comp_rnet[i][j][k][m])
                                if abs(orig_rnet[i][j][k][m] - comp_rnet[i][j][k][m]) > sram6_max:
                                    sram6_max = abs(orig_rnet[i][j][k][m] - comp_rnet[i][j][k][m])
                    except:
                        if abs(orig_rnet[i][j][k] - comp_rnet[i][j][k]) < sram6_min:
                            sram6_min = abs(orig_rnet[i][j][k] - comp_rnet[i][j][k])
                        if abs(orig_rnet[i][j][k] - comp_rnet[i][j][k]) > sram6_max:
                            sram6_max = abs(orig_rnet[i][j][k] - comp_rnet[i][j][k])
            except:
                if abs(orig_rnet[i][j] - comp_rnet[i][j]) < sram6_min:
                    sram6_min = abs(orig_rnet[i][j] - comp_rnet[i][j])
                if abs(orig_rnet[i][j] - comp_rnet[i][j]) > sram6_max:
                    sram6_max = abs(orig_rnet[i][j] - comp_rnet[i][j])
    except:
        if abs(orig_rnet[i] - comp_rnet[i]) < sram6_min:
            sram6_min = abs(orig_rnet[i] - comp_rnet[i])
        if abs(orig_rnet[i] - comp_rnet[i]) > sram6_max:
            sram6_max = abs(orig_rnet[i] - comp_rnet[i])

for i in [9]:
    try:
        for j in range(len(orig_rnet[i])):
            try:
                for k in range(len(orig_rnet[i][j])):
                    try:
                        for m in range(len(orig_rnet[i][j][k])):
                            try:
                                for n in range(len(orig_rnet[i][j][k][m])):
                                    if abs(orig_rnet[i][j][k][m][n] - comp_rnet[i][j][k][m][n]) < sram5_min:
                                        sram5_min = abs(orig_rnet[i][j][k][m][n] - comp_rnet[i][j][k][m][n])
                                    if abs(orig_rnet[i][j][k][m][n] - comp_rnet[i][j][k][m][n]) > sram5_max:
                                        sram5_max = abs(orig_rnet[i][j][k][m][n] - comp_rnet[i][j][k][m][n])
                            except:
                                if abs(orig_rnet[i][j][k][m] - comp_rnet[i][j][k][m]) < sram5_min:
                                    sram5_min = abs(orig_rnet[i][j][k][m] - comp_rnet[i][j][k][m])
                                if abs(orig_rnet[i][j][k][m] - comp_rnet[i][j][k][m]) > sram5_max:
                                    sram5_max = abs(orig_rnet[i][j][k][m] - comp_rnet[i][j][k][m])
                    except:
                        if abs(orig_rnet[i][j][k] - comp_rnet[i][j][k]) < sram5_min:
                            sram5_min = abs(orig_rnet[i][j][k] - comp_rnet[i][j][k])
                        if abs(orig_rnet[i][j][k] - comp_rnet[i][j][k]) > sram5_max:
                            sram5_max = abs(orig_rnet[i][j][k] - comp_rnet[i][j][k])
            except:
                if abs(orig_rnet[i][j] - comp_rnet[i][j]) < sram5_min:
                    sram5_min = abs(orig_rnet[i][j] - comp_rnet[i][j])
                if abs(orig_rnet[i][j] - comp_rnet[i][j]) > sram5_max:
                    sram5_max = abs(orig_rnet[i][j] - comp_rnet[i][j])
    except:
        if abs(orig_rnet[i] - comp_rnet[i]) < sram5_min:
            sram5_min = abs(orig_rnet[i] - comp_rnet[i])
        if abs(orig_rnet[i] - comp_rnet[i]) > sram5_max:
            sram5_max = abs(orig_rnet[i] - comp_rnet[i])

print('sram4 오차: {} ~ {}'.format(sram4_min, sram4_max))
print('sram5 오차: {} ~ {}'.format(sram5_min, sram5_max))
print('sram6 오차: {} ~ {}'.format(sram6_min, sram6_max))





