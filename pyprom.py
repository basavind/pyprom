import os
import shutil
import sys
import algo.alpha as alpha
import logs
import petrinet

output_dir = "output"  # output folder name


def main(argv):
    # read the log file
    log = []
    input_file = argv[1]
    output_file = os.path.splitext(
        output_dir + "/" + os.path.basename(input_file)
    )[0]

    log = logs.parse(input_file)

    print(log, input_file, output_file)

    yl, ti, to = alpha.apply(log, input_file, output_file)
    petrinet.build(yl, ti, to, output_file)


if __name__ == "__main__":
    main(sys.argv)
