import os
import shutil
import sys
import algo.alpha as alpha
import logs
import petrinet
from algo.fitting import mark_fitting

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

    places, initial_activities, terminal_activities = \
        alpha.apply(log, input_file, output_file)

    places = mark_fitting(places)

    petrinet.build(places, initial_activities,
                   terminal_activities, output_file)


if __name__ == "__main__":
    main(sys.argv)
