import ffmpeg

# Path: split-video\main.py
import os
import sys


def split_video(video_path):
    try:
        (
            ffmpeg
                .input(video_path)
                .output('output/split%06d.jpg', 
                        start_number=0)
                .overwrite_output()
                .run(quiet=True)
        )
        print("Video split successfully")
    except ffmpeg.Error as e:
        print(e.stderr, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    # get video path from command line
    # check if args are passed
    if len(sys.argv) < 2:
        print("Please enter a valid file path")
        sys.exit(1)
    video_path = sys.argv[1]
    # delete and create output folder
    if os.path.exists("./output"):
        os.system("rm -rf ./output")
    os.system("mkdir ./output")

    # check if video_path is a file
    if os.path.isfile(video_path):
        split_video(video_path)
    else:
        print("Please enter a valid file path")
        sys.exit(1)
