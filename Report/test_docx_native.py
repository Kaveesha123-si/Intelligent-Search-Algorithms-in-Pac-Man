import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

doc = docx.Document("Submission/Group_AI_28_Report.docx")
body = doc._body._body

# Find intro element
intro_idx = -1
for i, el in enumerate(body):
    t = "".join(el.itertext()).strip()
    if "1. Introduction & Background Research" in t:
        intro_idx = i
        break

# Element 12 is the declaration text
# We want to remove elements 0 to 11
elems_to_remove = [body[i] for i in range(12)]
for el in elems_to_remove:
    body.remove(el)

print("Removed elements 0 to 11. Now first element is:", "".join(body[0].itertext())[:40])

# Now the reference point is body[0] (which is the declaration paragraph)
ref_elem = body[0]

# Helper to create a paragraph before ref_elem
def create_p_before(ref):
    p = doc.add_paragraph()
    # Move p._p to before ref
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
p2 = create_p_before(ref_elem)
p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
p2.paragraph_format.space_before = Pt(0)
p2.paragraph_format.space_after = Pt(20)
r2 = p2.add_run()
r2.add_picture("Report/images/sliit_logo.png", width=Inches(2.0))

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
r5.font.color.rgb = RGBColor(31, 78, 121)

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
            tag = 'w:{}'.format(edge)
            element = tcBorders.find(qn(tag))
            if element is None:
                element = OxmlElement(tag)
                tcBorders.append(element)
            for key, val in edge_data.items():
                element.set(qn('w:{}'.format(key)), str(val))

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

border_spec = dict(sz=4, val='single', color='94A3B8', space='0')

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
    run.font.color.rgb = RGBColor(15, 23, 42)

members = [
    ("IT24510235", "Gajanayake\nH.K.D.W.R"),
    ("IT24400002", "Wickramasinghe\nW.S.S.D"),
    ("IT24103947", "Walimuniarachchi\nW.A.K.S"),
    ("IT24100131", "Basnayake K.S"),
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
        run.font.color.rgb = RGBColor(15, 23, 42)

# 7. Add PageBreak after Table (before ref_elem)
p_pb = create_p_before(ref_elem)
p_pb.add_run().add_break(docx.enum.text.WD_BREAK.PAGE)

# 8. Add Header for Student Declaration
p_dec_hdr = create_p_before(ref_elem)
p_dec_hdr.paragraph_format.space_before = Pt(12)
p_dec_hdr.paragraph_format.space_after = Pt(6)
r_dh = p_dec_hdr.add_run("Student Declaration & Submission Details")
r_dh.font.name = "Calibri"
r_dh.font.size = Pt(13)
r_dh.font.bold = True
r_dh.font.color.rgb = RGBColor(31, 78, 121)

# Format declaration paragraph (ref_elem)
p_dec = [p for p in doc.paragraphs if p._p == ref_elem][0]
p_dec.paragraph_format.space_after = Pt(10)
p_dec.paragraph_format.line_spacing = 1.2

# Find the declaration table and add a page break after it
# The declaration table is right after ref_elem!
decl_tbl_elem = ref_elem.getnext()
# Add a page break after declaration table
p_pb2 = doc.add_paragraph()
decl_tbl_elem.addnext(p_pb2._p)
p_pb2.add_run().add_break(docx.enum.text.WD_BREAK.PAGE)

# Save document
doc.save("Submission/Group_AI_28_Report.docx")
print("Saved modified docx successfully!")
