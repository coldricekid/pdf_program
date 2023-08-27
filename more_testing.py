import pandas as pd
import docx2pdf
from datetime import datetime
from docxtpl import DocxTemplate
doc = DocxTemplate("template/template.docx")
df = pd.read_csv('data/data.csv')


for index, row in df.iterrows():
    context = {'amount': row['amount'],
               'code': row['code']}
    doc.render(context)
    #doc.save('docs/generated_doc_' + str(datetime.now().strftime('%m.%d.%y')) + '.docx')
    doc.save(f"docs/{index}_"+ str(datetime.now().strftime('%m.%d.%y')) +".docx")
    print("Success")    
    

############### DOC TO PDF ################
docx2pdf.convert("docs/", "pdf/")




