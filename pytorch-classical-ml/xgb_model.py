import numpy as np

def xgb_tree(x, num_booster):
    if num_booster == 0:
        state = 0
        if state == 0:
            state = (1 if x['f2']<2.45000005 or np.isnan(x['f2'])  else 2)
            if state == 1:
                return 1.40939593
            if state == 2:
                return -0.730659068
    elif num_booster == 1:
        state = 0
        if state == 0:
            state = (1 if x['f2']<2.45000005 or np.isnan(x['f2'])  else 2)
            if state == 1:
                return -0.704698026
            if state == 2:
                state = (3 if x['f3']<1.75 or np.isnan(x['f3'])  else 4)
                if state == 3:
                    return 1.20304573
                if state == 4:
                    return -0.652173996
    elif num_booster == 2:
        state = 0
        if state == 0:
            state = (1 if x['f2']<4.75 or np.isnan(x['f2'])  else 2)
            if state == 1:
                return -0.698360741
            if state == 2:
                state = (3 if x['f3']<1.75 or np.isnan(x['f3'])  else 4)
                if state == 3:
                    return 0.292682886
                if state == 4:
                    return 1.36024845
    elif num_booster == 3:
        state = 0
        if state == 0:
            state = (1 if x['f2']<2.45000005 or np.isnan(x['f2'])  else 2)
            if state == 1:
                return 0.569317162
            if state == 2:
                return -0.525193989
    elif num_booster == 4:
        state = 0
        if state == 0:
            state = (1 if x['f2']<4.94999981 or np.isnan(x['f2'])  else 2)
            if state == 1:
                state = (3 if x['f2']<2.45000005 or np.isnan(x['f2'])  else 4)
                if state == 3:
                    return -0.476289779
                if state == 4:
                    return 0.53313446
            if state == 2:
                state = (5 if x['f3']<1.54999995 or np.isnan(x['f3'])  else 6)
                if state == 5:
                    return -0.817775309
                if state == 6:
                    return -0.395324379
    elif num_booster == 5:
        state = 0
        if state == 0:
            state = (1 if x['f2']<4.85000038 or np.isnan(x['f2'])  else 2)
            if state == 1:
                state = (3 if x['f3']<1.6500001 or np.isnan(x['f3'])  else 4)
                if state == 3:
                    return -0.526681006
                if state == 4:
                    return 0.228551283
            if state == 2:
                state = (5 if x['f2']<4.94999981 or np.isnan(x['f2'])  else 6)
                if state == 5:
                    return 0.149793491
                if state == 6:
                    return 0.654778183

def xgb_predict(x):
    predict = None
# initialize prediction with base score
    for i in range(6):
        predict = predict + xgb_tree(x, i)
    return predict