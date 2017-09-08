FROM keyi/python2-mcr2017a-rpi-isl

COPY JSTMB_O313/ ./JSTMB_O313
COPY setup.py ./
COPY O313_JSTMB_wrapper.py ./
COPY trainData.csv ./
COPY trainTargets.csv ./
