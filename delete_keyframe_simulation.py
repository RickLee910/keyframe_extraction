import cv2
import ffmpy as FFmpeg
import ffmpeg
import subprocess
import os
# info = ffmpeg.probe("pikachu.mp4")
# vs = next(c for c in info['streams'] if c['codec_type'] == 'video')
# duration_secs = float(vs['duration'])
# format = info['format']['format_name']
# codec_name = vs['codec_name']
# width = vs['width']
# height = vs['height']
# num_frames = vs['nb_frames']

def extract_keyframe(video_path):
    command = "ffmpeg -i {video_path} -vf select='eq(pict_type\,I)' -vsync 2 -s 1920*1080 -f image2 core-%02d.jpeg".format(video_path=video_path)
    subprocess.call(command)

def extract_keyframe_index(video_path):
    cmd = "ffprobe -i {video_path} -select_streams v -show_frames -show_entries frame=pict_type -of csv | grep -n I | cut -d ':' -f 1 > frame_index.txt".format(video_path=video_path)
    subprocess.call(cmd)
# extract_keyframe('pikachu.mp4')
extract_keyframe_index('pikachu.mp4')