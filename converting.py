# import ffmpeg
#
# stream = ffmpeg.input('in.mp4')
# stream = ffmpeg.hflip(stream)
# stream = ffmpeg.output(stream, 'output.mp4')
# ffmpeg.run(stream)

import ffmpeg
import glob

constant = '/home/alind/Music/'
files=[]

for filename in glob.iglob(constant + '*'):
    print(filename)
    files.append(filename.split('/')[-1])
    stream = ffmpeg.input(filename)
    filename = filename[:-3] +'mp3'
    print(filename)
    stream = ffmpeg.output(stream, filename).run() #'output12.mp3'
    ffmpeg.run(stream)

print(files)
q=pd.DataFrame(files, columns=['Files'])
q.to_excel(r'files.xlsx', index=False)
