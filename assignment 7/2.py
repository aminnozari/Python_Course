from moviepy.editor import VideoFileClip
video_path = "vid.mp4"
audio_path = "vid.wav"
video = VideoFileClip(video_path)
audio = video.audio
audio.write_audiofile(audio_path)
video.close()
audio.close()