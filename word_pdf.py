import docx
import os
from glob import glob

# !pip install docxcompose
from docxcompose.composer import Composer
# 将所有docx文件按顺序合并成一个docx文件
def combine_all_docx(files_list:list, out_file: str):
    number_of_sections = len(files_list)
    master = docx.Document()
    composer = Composer(master)

    print("docx file size:", number_of_sections)
    print("combine file sequences:", "\n".join(files_list))

    for doc in files_list:
        composer.append(docx.Document((doc)))

    composer.save(out_file)
    print("out file:", out_file)

# !pip install pypiwin32
from win32com.client import constants,gencache
# 将Word转pdf文件, 第一个参数代表word文档路径
def convert_word_to_pdf(word_file:str):
    word = gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(word_file, ReadOnly = 1)
    file_path = os.path.abspath(word_file)
    index = file_path.rindex('.')
    pdf_file = file_path[:index] + '.pdf'
    # 转换方法
    doc.ExportAsFixedFormat(pdf_file ,constants.wdExportFormatPDF)
    word.Quit()
    print("word:{} convert to pdf:{}".format(word_file, pdf_file))

if __name__ == '__main__':
    src_path = "C:\\Users\\kexin\\Desktop\\xyp\\src"
    out_file = "C:\\Users\\kexin\\Desktop\\xyp\\out\\merge.docx"
    path_list = glob(os.path.join(src_path, '*.docx'))

    file_with_id = [(p, int(os.path.basename(p).split('-')[0])) for p in path_list]
    file_with_id.sort(key=lambda x: x[1])
    #sorted_files = [f for (f, i) in file_with_id]
    sorted_files = zip(*file_with_id)[0]
    combine_all_docx(sorted_files, out_file)
    convert_word_to_pdf("C:\\Users\\kexin\\Desktop\\xyp\\out\\merge.docx")