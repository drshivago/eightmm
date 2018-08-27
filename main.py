from moviepy.editor import VideoFileClip
import moviepy.video.fx.all
import sys

frame_rate = 30
new_fps = frame_rate / 10
filename = sys.argv[1]
count = 1
clip = VideoFileClip(filename)

for counter in range(1,1800, int(new_fps)):
    clip.save_frame("images/frame%04d.jpg" %count, t = (counter / frame_rate))
    count += 1

new_clip = moviepy.editor.ImageSequenceClip('images', fps = 10)
new_clip = new_clip.set_audio(clip.audio)

new_clip.write_videofile("new.mp4")
