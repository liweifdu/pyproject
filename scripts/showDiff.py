import numpy as np

w,h = 416, 240
offset = 0

YUVref = np.fromfile('xkcdc_ref.yuv', dtype='uint8')
YUV = np.fromfile('xkcdc.yuv', dtype='uint8')

Yref = YUVref[offset:offset+w*h].reshape(h,w)
Y = YUV[offset:offset+w*h].reshape(h,w)

Uref = YUVref[offset:offset+w*h//4].reshape(h//2,w//2)
U = YUV[offset:offset+w*h//4].reshape(h//2,w//2)

Vref = YUVref[offset:offset+w*h//4].reshape(h//2,w//2)
V = YUV[offset:offset+w*h//4].reshape(h//2,w//2)

# diff y
def diffY():
    for i in range(h):
        for j in range(w):
            if Y[i, j] != Yref[i, j]:
                print("luma differ!")
                print("->x =", j, "y =", i)
                print("->idxLcuX =", j // 32, "idxLcuY =", i // 32, "pelX =", j % 32, "pelY =", i % 32, "m_cuAddr =", (j // 32) + (i // 32) * (w / 32))
                print("->ref =", Yref[i, j], "cur =", Y[i, j])
                return

# diff u
def diffU():
    for i in range(h // 2):
        for j in range(w // 2):
            if U[i, j] != Uref[i, j]:
                print("chroma u differ!")
                print("->x =", j, "y =", i)
                print("->idxLcuX =", j // 16, "idxLcuY =", i // 16, "pelX =", j % 16, "pelY =", i % 16, "m_cuAddr =", (j // 16) + (i // 16) * (w / 32))
                print("->ref =", Uref[i, j], "cur =", U[i, j])
                return

# diff v
def diffV():
    for i in range(h // 2):
        for j in range(w // 2):
            if V[i, j] != Vref[i, j]:
                print("chroma v differ!")
                print("->x =", j, "y =", i)
                print("->idxLcuX =", j // 16, "idxLcuY =", i // 16, "pelX =", j % 16, "pelY =", i % 16, "m_cuAddr =", (j // 16) + (i // 16) * (w / 32))
                print("->ref =", Vref[i, j], "cur =", V[i, j])
                return

for i in range(2):
    print("check frame", i, "...")
    Yref = YUVref[offset:offset+w*h].reshape(h,w)
    Y = YUV[offset:offset+w*h].reshape(h,w)
    offset += w*h

    Uref = YUVref[offset:offset+w*h//4].reshape(h//2,w//2)
    U = YUV[offset:offset+w*h//4].reshape(h//2,w//2)
    offset += w*h//4

    Vref = YUVref[offset:offset+w*h//4].reshape(h//2,w//2)
    V = YUV[offset:offset+w*h//4].reshape(h//2,w//2)
    offset += w*h//4

    diffY()
    diffU()
    diffV()

    print("check frame", i, "done!\n")










