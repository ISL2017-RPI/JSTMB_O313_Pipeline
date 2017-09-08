# JSTMB_O313_Pipeline

This is the source code for our JSTMB primitive on the seed data O313.

Once you clone this folder into your local repo, you can directly build the Docker image by:

docker build -t jstmb313 ./

Then, you can run the pipeline script in the following way:

docker run jstmb313 python O313_JSTMB_wrapper.py "trainData.csv" "trainTargets.csv"

The output is the selected features stored in a csv file
