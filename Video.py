import moviepy.editor as mv

clip1 = mv.VideoFileClip("Cabecera.mp4")
clip2 = mv.VideoFileClip("video12.mp4")

if clip1.size[0] > clip2.size[0]:
    final = clip1.resize(width=clip2.size[0])
    final.write_videofile("inter.mp4")
    clip1 = mv.VideoFileClip("inter.mp4")

elif clip1.size[0] < clip2.size[0]:
    final = clip2.resize(width=clip1.size[0])
    final.write_videofile("inter.mp4")
    clip2 = mv.VideoFileClip("inter.mp4")

final = mv.concatenate_videoclips([clip1, clip2, clip1], method="compose")
final.write_videofile("final.mp4")