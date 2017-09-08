import sys
import JSTMB_O313
import numpy as np

def JSTMB(data_file = 'trainData.csv', target_file = 'trainargets.csv'):
    my_JMI = JSTMB_O313.initialize()
    feat = my_JMI.JSTMB_primitive_O313(data_file, target_file)
    return feat


if __name__ == "__main__":
    data = sys.argv[1]
    target = sys.argv[2]
    selected_feature = np.array(JSTMB(data, target), dtype=np.int16)
    np.savetxt('Features_O313_JSTMB.csv', selected_feature, delimiter=',')
    print selected_feature
