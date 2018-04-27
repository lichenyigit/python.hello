import ffmpeg

# 代码是没有错的，只是引入的模块不对
stream = ffmpeg.input("D:\download\chrome\keke.mp4")
outputNode = ffmpeg.output(stream,'D:\download\keke1.mp3')

print("开始提取")
ffmpeg.run(outputNode)

print("执行完毕")
