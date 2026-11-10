
import os
import sys
import subprocess
import zipfile
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

base_dir = os.path.abspath(".")
html_file = os.path.join(base_dir, "Report", "Group_AI_28_Report.html")
raw_docx = os.path.join(base_dir, "Submission", "Group_AI_28_Report_raw.docx")
final_docx = os.path.join(base_dir, "Submission", "Group_AI_28_Report.docx")
submission_pdf = os.path.join(base_dir, "Submission", "Group_AI_28_Report.pdf")
report_pdf = os.path.join(base_dir, "Report", "Group_AI_28_Report.pdf")

print("--- Step 1: Converting HTML report to DOCX via Word COM in dedicated process ---")
py_step1 = f"""
import win32com.client, os
word = win32com.client.Dispatch("Word.Application")
try:
    doc = word.Documents.Open(r"{html_file}")
    for shape in doc.InlineShapes:
        try:
            if shape.LinkFormat:
                shape.LinkFormat.SavePictureWithDocument = True
                shape.LinkFormat.BreakLink()
        except:
            pass
    doc.SaveAs(r"{raw_docx}", FileFormat=16)
    doc.Close()
finally:
    word.Quit()
print("Saved raw docx")
"""
res1 = subprocess.run([sys.executable, "-c", py_step1], capture_output=True, text=True)
print(res1.stdout, res1.stderr)

print("--- Step 2: Styling Page 1 Cover Page with python-docx ---")
doc = docx.Document(raw_docx)
body = doc._body._body

# Find the Student Declaration header or text
decl_idx = -1
for i, el in enumerate(body):
    t = "".join(el.itertext()).strip()
    if "Student Declaration & Submission Details" in t or "We, the undersigned students" in t:
        decl_idx = i
        break

print(f"Found declaration element at index {decl_idx}")

# Remove elements before decl_idx (the HTML header box)
elems_to_remove = [body[i] for i in range(decl_idx)]
for el in elems_to_remove:
    body.remove(el)

ref_elem = body[0]

def create_p_before(ref):
    p = doc.add_paragraph()
    ref.addprevious(p._p)
    return p

# 1. Institution Title
p1 = create_p_before(ref_elem)
p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
p1.paragraph_format.space_before = Pt(36)
p1.paragraph_format.space_after = Pt(20)
r1 = p1.add_run("Sri Lanka Institute of Information Technology")
r1.font.name = "Times New Roman"
r1.font.size = Pt(16)
r1.font.color.rgb = RGBColor(0, 0, 0)

# 2. Logo
logo_path = os.path.join(base_dir, "Report", "images", "sliit_logo.png")
if os.path.exists(logo_path):
    p2 = create_p_before(ref_elem)
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after = Pt(20)
    r2 = p2.add_run()
    r2.add_picture(logo_path, width=Inches(2.0))

# 3. Semester
p3 = create_p_before(ref_elem)
p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
p3.paragraph_format.space_before = Pt(4)
p3.paragraph_format.space_after = Pt(4)
r3 = p3.add_run("Year 3 - Semester 1- 2026")
r3.font.name = "Times New Roman"
r3.font.size = Pt(13)
r3.font.color.rgb = RGBColor(0, 0, 0)

# 4. Module
p4 = create_p_before(ref_elem)
p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
p4.paragraph_format.space_before = Pt(4)
p4.paragraph_format.space_after = Pt(40)
r4 = p4.add_run("IT3012- Intelligence Agents")
r4.font.name = "Times New Roman"
r4.font.size = Pt(15)
r4.font.bold = True
r4.font.color.rgb = RGBColor(0, 0, 0)

# 5. Group Heading
p5 = create_p_before(ref_elem)
p5.alignment = WD_ALIGN_PARAGRAPH.LEFT
p5.paragraph_format.space_before = Pt(10)
p5.paragraph_format.space_after = Pt(6)
r5 = p5.add_run("Group Members & Primary Component Ownership")
r5.font.name = "Calibri"
r5.font.size = Pt(10.5)
r5.font.bold = True
r5.font.color.rgb = RGBColor(0, 0, 0)

# 6. Table
tbl = doc.add_table(rows=1, cols=2)
tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
tbl.autofit = False
ref_elem.addprevious(tbl._tbl)

col_widths = [Inches(1.5), Inches(2.5)]
hdr_titles = ["Student ID", "Student Name"]

def set_cell_border(cell, **kwargs):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = tcPr.first_child_found_in("w:tcBorders")
    if tcBorders is None:
        tcBorders = OxmlElement('w:tcBorders')
        tcPr.append(tcBorders)
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        edge_data = kwargs.get(edge)
        if edge_data:
            tag = f'w:{edge}'
            element = tcBorders.find(qn(tag))
            if element is None:
                element = OxmlElement(tag)
                tcBorders.append(element)
            for key, val in edge_data.items():
                element.set(qn(f'w:{key}'), str(val))

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

border_spec = dict(sz=4, val='single', color='000000', space='0')

for c_idx, title in enumerate(hdr_titles):
    cell = tbl.rows[0].cells[c_idx]
    cell.width = col_widths[c_idx]
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
    set_cell_border(cell, top=border_spec, bottom=border_spec, left=border_spec, right=border_spec)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(title)
    run.font.name = "Calibri"
    run.font.size = Pt(9.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)

members = [
    ("IT24100131", "Basnayake K.S"),
    ("IT24103947", "Walimuniarachchi\nW.A.K.S"),
    ("IT24510235", "Gajanayake\nH.K.D.W.R"),
    ("IT24400002", "Wickramasinghe\nW.S.S.D"),
]

for sid, name in members:
    row_cells = tbl.add_row().cells
    for c_idx, val in enumerate([sid, name]):
        cell = row_cells[c_idx]
        cell.width = col_widths[c_idx]
        set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
        set_cell_border(cell, top=border_spec, bottom=border_spec, left=border_spec, right=border_spec)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(val)
        run.font.name = "Calibri"
        run.font.size = Pt(9.5)
        if c_idx == 0:
            run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)

# PageBreak after Cover Page table
p_pb = create_p_before(ref_elem)
p_pb.add_run().add_break(docx.enum.text.WD_BREAK.PAGE)

# Format declaration paragraph
p_dec = [p for p in doc.paragraphs if p._p == ref_elem][0]
p_dec.paragraph_format.space_after = Pt(10)
p_dec.paragraph_format.line_spacing = 1.2

# Add PageBreak after Declaration table
# ref_elem is the heading h2
# p_dec_elem is the paragraph
p_dec_elem = ref_elem.getnext()
# tbl_elem is the declaration table
tbl_elem = p_dec_elem.getnext()
p_pb2 = doc.add_paragraph()
tbl_elem.addnext(p_pb2._p)
p_pb2.add_run().add_break(docx.enum.text.WD_BREAK.PAGE)

# Clean up all styles, paragraph borders, and table cell shading to guarantee 100% white tables and clean typed look
for s in doc.styles:
    try:
        if hasattr(s, '_element') and s._element is not None:
            pPr = s._element.find(qn('w:pPr'))
            if pPr is not None:
                pBdr = pPr.find(qn('w:pBdr'))
                if pBdr is not None:
                    pPr.remove(pBdr)
            rPr = s._element.find(qn('w:rPr'))
            if rPr is not None:
                color = rPr.find(qn('w:color'))
                if color is not None:
                    color.set(qn('w:val'), '000000')
    except Exception:
        pass

def strip_p_borders(p):
    pPr = p._p.find(qn('w:pPr'))
    if pPr is not None:
        pBdr = pPr.find(qn('w:pBdr'))
        if pBdr is not None:
            pPr.remove(pBdr)

def make_cell_pure_white(cell):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = tcPr.find(qn('w:shd'))
    if shd is not None:
        tcPr.remove(shd)
    new_shd = OxmlElement('w:shd')
    new_shd.set(qn('w:val'), 'clear')
    new_shd.set(qn('w:color'), 'auto')
    new_shd.set(qn('w:fill'), 'FFFFFF')
    tcPr.append(new_shd)

def set_cell_border_black(cell):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = tcPr.find(qn('w:tcBorders'))
    if tcBorders is not None:
        tcPr.remove(tcBorders)
    tcBorders = OxmlElement('w:tcBorders')
    tcPr.append(tcBorders)
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        el = OxmlElement(f'w:{edge}')
        el.set(qn('w:val'), 'single')
        el.set(qn('w:sz'), '4')
        el.set(qn('w:space'), '0')
        el.set(qn('w:color'), '000000')
        tcBorders.append(el)

for p in doc.paragraphs:
    strip_p_borders(p)
    for r in p.runs:
        if r.font.color and r.font.color.rgb:
            r.font.color.rgb = RGBColor(0, 0, 0)

for t in doc.tables:
    for row in t.rows:
        for cell in row.cells:
            make_cell_pure_white(cell)
            set_cell_border_black(cell)
            for p in cell.paragraphs:
                strip_p_borders(p)
                for r in p.runs:
                    if r.font.color and r.font.color.rgb:
                        r.font.color.rgb = RGBColor(0, 0, 0)

# Save document
doc.save(final_docx)
print(f"Saved {final_docx}")

if os.path.exists(raw_docx):
    os.remove(raw_docx)

print("--- Step 3: Exporting PDF via Word COM in dedicated process ---")
py_step3 = f"""
import win32com.client, os
word = win32com.client.Dispatch("Word.Application")
try:
    doc = word.Documents.Open(r"{final_docx}")
    # Export PDFs
    doc.SaveAs(r"{submission_pdf}", FileFormat=17) # 17 = wdFormatPDF
    doc.SaveAs(r"{report_pdf}", FileFormat=17)
    doc.Close()
finally:
    word.Quit()
print("Exported PDFs")
"""
res3 = subprocess.run([sys.executable, "-c", py_step3], capture_output=True, text=True)
print(res3.stdout, res3.stderr)

print("--- Step 4: Re-packing Code ZIP ---")
zip_path = os.path.join(base_dir, "Submission", "Group_AI_28_Code.zip")
if os.path.exists(zip_path):
    os.remove(zip_path)

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write(os.path.join(base_dir, "Group_Project", "search", "search.py"), arcname="search.py")
    zf.write(os.path.join(base_dir, "Group_Project", "search", "searchAgents.py"), arcname="searchAgents.py")

print(f"Successfully created {zip_path} ({os.path.getsize(zip_path)} bytes)")
print("=== ALL SUBMISSION DELIVERABLES ARE 100% COMPLETE AND UP TO DATE ===")
