
from sys import argv

def main():

    eq_original_file = open(argv[1], 'r')

    eq_original = eq_original_file.read().strip().split('\n')

    for band in eq_original:

        freq = 0
        gain = 0
        qval = 0

        band_meta = band.strip().split(' ')

        freq = band_meta[4]
        gain = band_meta[7]
        qval = band_meta[10]

        print('<band type="PEAKEQ" gain="' + gain + '" freq="' + freq + '" Q="' + qval + '" />')

main()
