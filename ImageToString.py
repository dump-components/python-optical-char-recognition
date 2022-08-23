from OpticalCharRecognition import TesseractOCR

class ImageToString(TesseractOCR):
    
    
    def __init__(self, path_tesseract_executable) -> None:
        super().__init__(path_tesseract_executable)
    
    def __call__(self, path_image):
        self.__str_img  = self.ocr.image_to_string(path_image)
    
    def __str__(self) -> str:
        return self.__str_img