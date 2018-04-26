import ffmpeg

print("开始提取")
stream = ffmpeg.input("D:\download\chrome\keke.mp4")
print(stream)
stream = ffmpeg.output(stream,'D:\download\keke.mp3 ')
ffmpeg.run(stream)
print("执行完毕")
