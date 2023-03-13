import sys, os, getopt


def commands(argv):
	
    print(argv)
    try:
        opts, args = getopt.getopt(argv,
                "hst:i:d:m:c:b:e:n:",["ifile="])
    except getopt.GetoptError:
        print('Invalid argument')
        print(argv)
        print('try:')
        print('wordSwarm.py -n <topN] -s -t <title> -i <inputfile> -d <outputFolder> -m <maxWordHeight> -c <HexHue1_HexHue2> -b <startDate YYYYMMDD> -e <endDate YYYYMMDD>')
        sys.exit(2)


if __name__=="__main__":
    # print("list: ", str(sys.argv))
    commands(sys.argv[1:])
