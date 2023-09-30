import time
import sys
from colorama import colorama_text,Fore

def print_progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(Fore.GREEN+'\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    sys.stdout.flush()

def main23():
    total_iterations = 100

    for i in range(total_iterations + 1):
        time.sleep(0.01)  # Simulate some work being done
        print_progress_bar(i, total_iterations, prefix='Progress:', suffix='Complete', length=50)

    print('\nTask completed.')


main23()

