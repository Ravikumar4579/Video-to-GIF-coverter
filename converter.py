from moviepy.editor import VideoFileClip

video_file = input("Enter the path to the video file: ")
fps = int(input("Enter the desired frames per second (fps): "))


clip = VideoFileClip(video_file)


output_file = "mygif.gif"
clip.write_gif(output_file, fps=fps)

print(f"GIF created successfully and saved as {output_file}")
