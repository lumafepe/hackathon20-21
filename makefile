install:
	cp dbordo.py /usr/local/bin/dbordo
	cp creator.py /usr/local/bin/dbordo_creator
	chmod +x /usr/local/bin/dbordo 
	chmod +x /usr/local/bin/dbordo_creator

dependencies:
	apt install tesseract-ocr
	pip3 install pytesseract
