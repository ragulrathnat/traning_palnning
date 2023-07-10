from PyPDF2 import PdfReader,PdfWriter,PdfMerger
import os
from PIL import Image
from pdf2image import convert_from_path
import pypdfium2 as pdfium

def split_pdf(filename):
    with open(filename,"rb") as file1:
        reader = PdfReader(file1)
        for page_num in range(0,len(reader.pages)):
            selected_page = reader.pages[page_num]
            writer = PdfWriter()
            writer.add_page(selected_page)
            filename1 = f"{filename}+{page_num}.pdf"
            with open(filename1,"wb") as file2:
                writer.write(file2)


def split_pdf_upon(filename,start,stop):
    with open(filename,"rb") as file1:
        reader = PdfReader(file1)
        writer = PdfWriter()
        for page_num  in range(start,stop):
            selected_page = reader.pages[page_num]
            writer.add_page(selected_page)
        filename = f"{filename},from{start},to{stop}.pdf"
        with open(filename,"wb") as file2:
            writer.write(file2)


target_folder_list = ["Freshres plan.pdf","python_basic certificate.pdf"]

def merger_pdf(target_list):
    merger = PdfMerger()
    filename = "mergerfile.pdf"
    with open(filename,"wb") as file1:
        for list in target_list:
            merger.append(list)
        merger.write(file1)


def rotation_pdf(filename,page_num,rotation):
    with open(filename,"rb") as file1:
        reader = PdfReader(file1)
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])
        writer.pages[0].rotate(rotation)
        filenameout = "output.pdf"
        with open(filenameout,"wb") as file2:
            writer.write(file2)


def crop_pdf(filename):
    with open(filename,"rb") as file1:
        reader = PdfReader(file1)
        writer = PdfWriter()
        page_read = reader.pages[1]
        print(page_read.mediabox)
        page_read.mediabox.lower_left = [0,0]
        page_read.mediabox.lower_right = [500,0]
        page_read.mediabox.upper_left = [0,566]
        page_read.mediabox.upper_right = [500,599]

        writer.add_page(page_read)
        with open("cropoutput.pdf","wb") as file2:
            writer.write(file2)


def image_to_pdf(image_name):
    my_image = Image.open(image_name)
    img = my_image.convert("RGB")
    filename = "img2pdf.pdf"
    img.save(filename) 

def pdf_to_image(filename):
    filename = "Freshres Plan.pdf"
    pdf = pdfium.PdfDocument(filename)
    selected_page = pdf[0]
    pil_img = selected_page.render(scale = 4).to_pil()
    pil_img.save("final.jpg")


image_to_pdf("img1.png")

pdf_to_image("Freshres Plan.pdf")

crop_pdf("Freshres Plan.pdf")

rotation_pdf("Freshres Plan.pdf",2,90)

merger_pdf(target_folder_list)

split_pdf("Freshres Plan.pdf")

split_pdf_upon("Freshres Plan.pdf",1,3)
