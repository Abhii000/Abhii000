import time
import sys

def print_loading_animation():
    animation = "|/-\\"
    for i in range(20):
        sys.stdout.write("\r" + "Loading " + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(0.1)

    sys.stdout.write("\r" + "Loading complete!")
    sys.stdout.flush()

if __name__ == "__main__":
    print_loading_animation()
    print("\nTask completed.")
