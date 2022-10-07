### PDFtoText.py

```python3 PDFtoText.py source_folder  destination_folder  [f]```

The source folder must only contain the pdf files to be read. Both the source folder and destination folders were tested with full paths, so that would be best.

Adding an ```f``` as the third argument will save the text file in the [f]ormat of the pdf, while leaving if it off will save the text as one long string with each word seperated by a space.

The only required package that isnt built in is pdftotext, so 

```pip install pdftotext```

will set everything up. I tested everything on a linux machine, so running on other machines may lead to some challenges, but i suspect everything will work fine on windows and mac.
