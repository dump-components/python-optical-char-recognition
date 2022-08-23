import pytesseract


class TesseractOCR:

    
    def __init__(self, path_tesseract_executable) -> None:
        self.__ocr = pytesseract
        self.__ocr.pytesseract.tesseract_cmd = path_tesseract_executable


    @property
    def ocr(self):
        return self.__ocr

        