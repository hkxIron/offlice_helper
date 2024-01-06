# Using this GIF: http://www.videogamesprites.net/FinalFantasy1/Party/Before/Fighter-Front.gif
import os.path
import sys
from PIL import Image

# def iter_frames(im:Image):
#     try:
#         i= 0
#         while True:
#             im.seek(i)
#             imframe = im.copy()
#             if i == 0:
#                 palette = imframe.getpalette()
#             else:
#                 imframe.putpalette(palette)
#                 #palette = imframe.getpalette()
#             yield imframe
#             i += 1
#     except EOFError:
#         pass
# def convert(img_file:str, out_dir:str):
#     im = Image.open(img_file)
#     file_name_no_suffix=os.path.basename(img_file).split(".")[0]
#     for i, frame in enumerate(iter_frames(im)):
#         out_file=os.path.join(out_dir, f"{file_name_no_suffix}_{i}.png")
#         frame.save(out_file, **frame.info, format='PNG')
#         print(f"extract png:{out_file}")

def extract_frames(img_file:str, out_dir:str, sample_by_k_steps=1):
    frame = Image.open(img_file)
    nframes = 0
    file_name_no_suffix=os.path.basename(img_file).split(".")[0]
    new_path=os.path.join(out_dir, file_name_no_suffix)
    if not os.path.exists(new_path):
        os.mkdir(new_path)

    while frame:
        out_file=os.path.join(new_path, f"{file_name_no_suffix}_{nframes}.png")
        frame.save(out_file, 'GIF')
        print(f"save png file:{out_file}")
        # 每隔多少桢采样一张图片
        nframes += sample_by_k_steps
        try:
            frame.seek(nframes)
        except EOFError:
            break


if __name__ == '__main__':
    #convert("data/img/jacobi-iteration.gif", "data/out_img/")
    #processImage('data/img/jacobi-iteration.gif')
    #extract_frames('data/img/jacobi-iteration.gif', 'data/out_img')
    extract_frames('data/img/lookahead-decoding.gif', 'data/out_img')
