import quant_verify
import analysis
import argparse

# 3 - 6
# 6 - 10
# 10 - 14
# 14 - 17

def run_all(start=0, end=0):
    for atl in range(start, end):
        for atl2 in range(3, 17):
            for atm in range(3, 17):
                if atl2 <= atm:
                    testDir = 'data/{atl}_{atl2}_{atm}'.format(atl=atl, atl2=atl2, atm=atm)
                    filename = '{testDir}_analysis'.format(testDir=testDir)
                    quant_verify.experiment_run_at_least_to_at_least_or_most(testDir=testDir, atl=atl, atl2=atl2, atm=atm);
                    analysis.analysis_on_dir(dirName=dirName, filename=filename, atl=atl, atl2=atl2, atm=atm)


    # RUN AN EXPERIMENT, with command-line arguments
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', help='start', type=int)
    parser.add_argument('--end', help='end', type=int)
    args = parser.parse_args()
    run_all(start=args.start, end=args.end);