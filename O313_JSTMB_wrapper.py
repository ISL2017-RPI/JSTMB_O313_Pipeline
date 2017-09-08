import sys
import JSTMB_O313
import numpy as np

def JSTMB(data_file, target_file, hm_feat):
    my_JMI = JSTMB_O313.initialize()
    feat = my_JMI.JSTMB_primitive_O313(data_file, target_file, hm_feat)
    return feat


if __name__ == "__main__":
    data = sys.argv[1]
    target = sys.argv[2]
    hm_feat = sys.argv[3]
    selected_feature = np.array(JSTMB(data, target, hm_feat), dtype=np.int16)
    np.savetxt('Features_O313_JSTMB.csv', selected_feature, delimiter=',')
    print selected_feature