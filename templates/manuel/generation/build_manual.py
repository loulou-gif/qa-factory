# Génère un manuel utilisateur à partir du modèle Word CEPICI / Synelia (repris du projet OLIB).
# Le module de contenu définit PROJET (ex. 'SAUCEDEMO'), MODULE (sous-titre de couverture,
# ex. 'BOUTIQUE EN LIGNE'), TITRE (titre du document) et éventuellement LANG = 'en'.
# Réutilise couverture, styles, numérotation, police et filets du modèle ;
# seul le corps du document est remplacé. Bibliothèque standard uniquement.
import re, sys, zipfile, struct, random
from pathlib import Path
from xml.sax.saxutils import escape

TEMPLATE = Path(sys.argv[1])
CAPTURES = Path(sys.argv[2])
OUT = Path(sys.argv[3])
CONTENT = sys.argv[4]          # module python décrivant le contenu
ns = {}
exec(Path(CONTENT).read_text(encoding='utf8'), ns)
EN = ns.get('LANG', 'fr') == 'en'   # LANG = 'en' dans le module de contenu : manuel en anglais
PROJET = ns.get('PROJET', 'PROJET')
MODULE = ns.get('MODULE', 'MANUEL')
TITRE = ns.get('TITRE', f'Manuel d’utilisation – {PROJET}')

zin = zipfile.ZipFile(TEMPLATE)
doc = zin.read('word/document.xml').decode('utf8')
rels = zin.read('word/_rels/document.xml.rels').decode('utf8')
numbering = zin.read('word/numbering.xml').decode('utf8')
core = zin.read('docProps/core.xml').decode('utf8')

head = doc[:doc.find('<w:body>') + len('<w:body>')]
body = doc[len(head):]
paras = re.findall(r'<w:p[ >].*?</w:p>', body, flags=re.S)
sectpr = re.search(r'<w:sectPr[ >].*?</w:sectPr>(?=</w:body>)', body, flags=re.S).group(0)

def text_of(p):
    return ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', p))

# ---------- Couverture (paragraphes avant le sommaire) ----------
toc_idx = next(i for i, p in enumerate(paras) if 'SOMMAIRE' in text_of(p))
toc_pos = body.rfind('<w:p ', 0, body.find('<w:pStyle w:val="En-ttedetabledesmatires"/>'))
toc_heading_xml = body[toc_pos:body.find('</w:p>', toc_pos) + len('</w:p>')]
# découpage brut : la couverture contient des paragraphes imbriqués et le sommaire du
# modèle est encapsulé dans un contrôle de contenu <w:sdt>, que l'on remplace
sdt_pos = body.rfind('<w:sdt>', 0, toc_pos)
cover = body[:sdt_pos]
assert len(re.findall(r'<w:p(?: [^>]*[^/])?>', cover)) == cover.count('</w:p>')
NB = ' '
cover_repl = {
    f'PROJET{NB}: CEPICI I5': f'PROJET{NB}: {PROJET}',
    '>ADMINISTRATION<': f'>{MODULE}<',
    '>CEPICI I5<': f'>{PROJET}<',
    'Septembre 2026': f'Date{NB}: à renseigner',
    f'Version{NB}: 1.1': f'Version{NB}: à renseigner',
}
if EN:
    cover_repl = {
        f'PROJET{NB}: CEPICI I5': f'PROJECT: {PROJET}',
        '>ADMINISTRATION<': f'>{MODULE}<',
        '>CEPICI I5<': f'>{PROJET}<',
        'Septembre 2026': 'Date: to be completed',
        f'Version{NB}: 1.1': 'Version: to be completed',
        'MANUEL D’UTILISATION': 'USER MANUAL',
        f'Rédaction{NB}:': 'Author:',
    }
for a, b in cover_repl.items():
    assert a in cover, a
    cover = cover.replace(a, b)
# texte alternatif des logos : le modèle contient un chemin de poste de travail personnel
cover = re.sub(r'descr="[A-Za-z]:\\[^"]*"', 'descr="Logo Synelia"', cover)
toc_heading = toc_heading_xml
assert 'SOMMAIRE' in toc_heading
if EN:
    toc_heading = toc_heading.replace('SOMMAIRE', 'CONTENTS')

# Paragraphes modèles : titres non numérotés (PREAMBULE) et chapitre (MENU ...)
tpl_unnumbered = next(p for p in paras[toc_idx:] if text_of(p).strip() == 'PREAMBULE' and '<w:drawing' in p)
tpl_chapter = next(p for p in paras if 'MENU PARAMETRAGES' in text_of(p) and '<w:drawing' in p)
for _t in (tpl_unnumbered, tpl_chapter):
    assert _t.count('<w:p ') == _t.count('</w:p>') == 1 and 'txbxContent' not in _t

ids = iter(range(5000, 99999))
def fresh_ids(xml):
    xml = re.sub(r'<wp:docPr id="\d+"', lambda m: f'<wp:docPr id="{next(ids)}"', xml)
    xml = re.sub(r'(wp14:anchorId|wp14:editId|w14:anchorId)="[0-9A-F]+"',
                 lambda m: f'{m.group(1)}="{random.randint(0x10000000, 0x7FFFFFFF):08X}"', xml)
    return xml

def retitle(tpl, title, extra_ppr=''):
    # garde le run du filet (drawing), remplace le texte, force le niveau hiérarchique
    first = [True]
    def sub(m):
        if first[0]:
            first[0] = False
            return f'<w:t xml:space="preserve">{escape(title)}</w:t>'
        return '<w:t></w:t>'
    p = re.sub(r'<w:t(?: [^>]*)?>[^<]*</w:t>', sub, tpl)
    p = re.sub(r'<w:bookmark(Start|End)[^>]*/>', '', p)
    ppr_end = p.find('</w:pPr>')
    rpr_pos = p.find('<w:rPr>', 0, ppr_end)
    pos = rpr_pos if rpr_pos != -1 else ppr_end
    p = p[:pos] + extra_ppr + p[pos:]
    return fresh_ids(p)

# ---------- Numérotation dédiée (I. / 1. / 1.1 ; étapes ; puces) ----------
ABS_H, ABS_STEP, ABS_BUL = 900, 901, 902
NUM_H = 900
abstracts = f'''<w:abstractNum w:abstractNumId="{ABS_H}"><w:multiLevelType w:val="multilevel"/>
<w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="upperRoman"/><w:lvlText w:val="%1."/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="1080" w:hanging="720"/></w:pPr></w:lvl>
<w:lvl w:ilvl="1"><w:start w:val="1"/><w:numFmt w:val="decimal"/><w:lvlText w:val="%2."/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="720" w:hanging="360"/></w:pPr></w:lvl>
<w:lvl w:ilvl="2"><w:start w:val="1"/><w:numFmt w:val="decimal"/><w:lvlText w:val="%2.%3"/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="1080" w:hanging="720"/></w:pPr></w:lvl>
</w:abstractNum>
<w:abstractNum w:abstractNumId="{ABS_STEP}"><w:multiLevelType w:val="singleLevel"/>
<w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="decimal"/><w:lvlText w:val="%1."/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="720" w:hanging="360"/></w:pPr><w:rPr><w:rFonts w:ascii="Helvetica" w:hAnsi="Helvetica" w:cs="Helvetica"/><w:b/><w:color w:val="0FA5E1"/></w:rPr></w:lvl>
</w:abstractNum>
<w:abstractNum w:abstractNumId="{ABS_BUL}"><w:multiLevelType w:val="singleLevel"/>
<w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val=""/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="720" w:hanging="360"/></w:pPr><w:rPr><w:rFonts w:ascii="Symbol" w:hAnsi="Symbol" w:hint="default"/></w:rPr></w:lvl>
</w:abstractNum>'''
nums = [f'<w:num w:numId="{NUM_H}"><w:abstractNumId w:val="{ABS_H}"/></w:num>',
        f'<w:num w:numId="902"><w:abstractNumId w:val="{ABS_BUL}"/></w:num>']
step_num = [910]
def new_step_list():
    step_num[0] += 1
    nums.append(f'<w:num w:numId="{step_num[0]}"><w:abstractNumId w:val="{ABS_STEP}"/>'
                f'<w:lvlOverride w:ilvl="0"><w:startOverride w:val="1"/></w:lvlOverride></w:num>')
    return step_num[0]

# ---------- Images ----------
media = {}          # nom -> (rid, target)
def png_size(path):
    with open(path, 'rb') as f:
        head_ = f.read(24)
    return struct.unpack('>II', head_[16:24])

def image_rid(name):
    if name not in media:
        rid = f'rIdM{len(media) + 1}'
        media[name] = (rid, f'media/manuel_{name}.png')
    return media[name][0]

EMU_CM = 360000
def drawing(name, width_cm=None, height_cm=None, border=True):
    path = CAPTURES / f'{name}.png'
    w, h = png_size(path)
    if width_cm:
        cx = int(width_cm * EMU_CM); cy = int(cx * h / w)
    else:
        cy = int(height_cm * EMU_CM); cx = int(cy * w / h)
    rid = image_rid(name)
    did = next(ids)
    ln = ('<a:ln w="6350"><a:solidFill><a:srgbClr val="BFBFBF"/></a:solidFill></a:ln>' if border else '')
    return (f'<w:r><w:rPr><w:noProof/></w:rPr><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
            f'<wp:extent cx="{cx}" cy="{cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/>'
            f'<wp:docPr id="{did}" name="Image {did}" descr="{escape(name)}"/>'
            f'<wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/></wp:cNvGraphicFramePr>'
            f'<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            f'<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:nvPicPr><pic:cNvPr id="{did}" name="{escape(name)}.png"/><pic:cNvPicPr/></pic:nvPicPr>'
            f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
            f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom>{ln}</pic:spPr>'
            f'</pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r>')

# ---------- Texte ----------
FONT = '<w:rFonts w:ascii="Helvetica" w:hAnsi="Helvetica" w:cs="Helvetica"/>'
def runs(text, base_rpr=''):
    """**gras**, *italique*, [[bouton]] = image de bouton intégrée au texte."""
    out = []
    for tok in re.split(r'(\*\*.+?\*\*|\*.+?\*|\[\[[^\]]+\]\])', text):
        if not tok:
            continue
        if tok.startswith('[['):
            out.append(drawing('btn_' + tok[2:-2], height_cm=0.55, border=False))
            continue
        if not EN:
            tok = re.sub(r'« ', '« ', tok)
            tok = re.sub(r' ([»:;?!])', lambda m: ' ' + m.group(1), tok)
        rpr = FONT + base_rpr
        if tok.startswith('**'):
            tok, rpr = tok[2:-2], rpr + '<w:b/>'
        elif tok.startswith('*'):
            tok, rpr = tok[1:-1], rpr + '<w:i/>'
        out.append(f'<w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{escape(tok)}</w:t></w:r>')
    return ''.join(out)

def para(inner, ppr=''):
    return f'<w:p><w:pPr>{ppr}</w:pPr>{inner}</w:p>'

def P(text, keep_next=False):
    return para(runs(text), ('<w:keepNext/>' if keep_next else '') + '<w:jc w:val="both"/>')

current_steps = [None]
def STEPS(items):
    if current_steps[0] is None:
        current_steps[0] = new_step_list()
    nid = current_steps[0]
    return ''.join(para(runs(t), '<w:pStyle w:val="Paragraphedeliste"/>' + ('<w:keepNext/>' if t.endswith(':') else '') +
                        f'<w:numPr><w:ilvl w:val="0"/><w:numId w:val="{nid}"/></w:numPr><w:spacing w:after="80"/><w:jc w:val="both"/>')
                   for t in items)

def BULLETS(items):
    return ''.join(para(runs(t), '<w:pStyle w:val="Paragraphedeliste"/><w:numPr><w:ilvl w:val="0"/><w:numId w:val="902"/></w:numPr>'
                        '<w:spacing w:after="60"/><w:jc w:val="both"/>') for t in items)

fig = [0]
def FIG(name, caption, width_cm=16):
    fig[0] += 1
    img = para(drawing(name, width_cm=width_cm), '<w:keepNext/><w:spacing w:before="120" w:after="60"/><w:jc w:val="center"/>')
    cap = para(runs(f'Figure {fig[0]} – {caption}', '<w:i/><w:color w:val="595959"/><w:sz w:val="18"/><w:szCs w:val="18"/>'),
               '<w:spacing w:after="240"/><w:jc w:val="center"/>')
    return img + cap

def NOTE(label, text):
    ppr = ('<w:pBdr><w:left w:val="single" w:sz="24" w:space="8" w:color="0FA5E1"/></w:pBdr>'
           '<w:shd w:val="clear" w:color="auto" w:fill="EAF6FC"/><w:spacing w:before="120" w:after="200"/><w:ind w:left="240" w:right="120"/><w:jc w:val="both"/>')
    return para(runs(f'**{label}**' + (': ' if EN else ' : ') + text), ppr)

def LABEL(text):
    current_steps[0] = None     # chaque procédure titrée repart à l'étape 1
    return para(runs(text, '<w:b/><w:color w:val="0FA5E1"/>'), '<w:keepNext/><w:spacing w:before="160" w:after="80"/>')

def H_UNNUM(title):
    return retitle(tpl_unnumbered, title, '<w:outlineLvl w:val="0"/>')

def H(level, title, page_break=False):
    current_steps[0] = None
    if level == 0:
        p = retitle(tpl_chapter, title, '<w:outlineLvl w:val="0"/>')
        p = p.replace('<w:numId w:val="4"/>', f'<w:numId w:val="{NUM_H}"/>', 1)
        if page_break:
            p = re.sub(r'(<w:pStyle w:val="[^"]+"/>)', lambda m: m.group(1) + '<w:pageBreakBefore/>', p, count=1)
        return p
    size = 36 if level == 1 else 30
    ppr = ('<w:pStyle w:val="syneliacolor"/><w:keepNext/>' + ('<w:pageBreakBefore/>' if page_break else '') +
           f'<w:numPr><w:ilvl w:val="{level}"/><w:numId w:val="{NUM_H}"/></w:numPr>'
           f'<w:spacing w:before="{360 if level == 1 else 280}" w:after="160"/><w:contextualSpacing w:val="0"/><w:outlineLvl w:val="{level}"/>'
           f'<w:rPr><w:sz w:val="{size}"/><w:szCs w:val="{size}"/></w:rPr>')
    return para(f'<w:r><w:rPr><w:sz w:val="{size}"/><w:szCs w:val="{size}"/></w:rPr><w:t xml:space="preserve">{escape(title)}</w:t></w:r>', ppr)

def PAGEBREAK():
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'

def TOC():
    return ('<w:p><w:pPr><w:pStyle w:val="TM1"/><w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9062"/></w:tabs></w:pPr>'
            '<w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText xml:space="preserve"> TOC \\o "1-3" \\h \\z \\u </w:instrText></w:r>'
            '<w:r><w:fldChar w:fldCharType="separate"/></w:r>'
            f'<w:r><w:rPr>{FONT}</w:rPr><w:t>{"Right-click and choose Update Field to refresh the table of contents." if EN else "Sommaire à actualiser (clic droit, Mettre à jour les champs)."}</w:t></w:r>'
            '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>')

api = dict(P=P, STEPS=STEPS, BULLETS=BULLETS, FIG=FIG, NOTE=NOTE, LABEL=LABEL, H=H,
           H_UNNUM=H_UNNUM, PAGEBREAK=PAGEBREAK)
content_xml = ns['build'](api)

if EN:
    head = head.replace('w:val="fr-FR"', 'w:val="en-GB"')
    cover = cover.replace('w:val="fr-FR"', 'w:val="en-GB"')
new_doc = head + cover + toc_heading + TOC() + PAGEBREAK() + content_xml + sectpr + '</w:body></w:document>'

# ---------- Relations : on garde les images de couverture, on retire les autres ----------
cover_rids = set(re.findall(r'r:embed="([^"]+)"', cover))
keep_media = set()
def rel_filter(m):
    rel = m.group(0)
    rid = re.search(r'Id="([^"]+)"', rel).group(1)
    if '/image"' in rel or 'relationships/image' in rel:
        if rid not in cover_rids:
            return ''
        keep_media.add('word/' + re.search(r'Target="([^"]+)"', rel).group(1))
    return rel
rels = re.sub(r'<Relationship [^>]*/>', rel_filter, rels)
img_rels = ''.join(f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="{t}"/>'
                   for rid, t in media.values())
rels = rels.replace('</Relationships>', img_rels + '</Relationships>')

numbering = numbering.replace('<w:num ', abstracts + '<w:num ', 1)
numbering = re.sub(r'(<w:numIdMacAtCleanup[^>]*/>)?</w:numbering>', lambda m: ''.join(nums) + (m.group(1) or '') + '</w:numbering>', numbering)

core = re.sub(r'<dc:title>.*?</dc:title>', '<dc:title>' + TITRE + '</dc:title>', core)
core = re.sub(r'<dc:creator>.*?</dc:creator>', '<dc:creator>Synelia Group Afrique</dc:creator>', core)
core = re.sub(r'<cp:lastModifiedBy>.*?</cp:lastModifiedBy>', '<cp:lastModifiedBy>Synelia Group Afrique</cp:lastModifiedBy>', core)

with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        n = item.filename
        if n.startswith('word/media/') and n not in keep_media:
            continue
        data = zin.read(n)
        if n == 'word/document.xml': data = new_doc.encode('utf8')
        elif n == 'word/_rels/document.xml.rels': data = rels.encode('utf8')
        elif n == 'word/numbering.xml': data = numbering.encode('utf8')
        elif n == 'docProps/core.xml': data = core.encode('utf8')
        elif n == 'word/styles.xml' and EN: data = data.replace(b'w:val="fr-FR"', b'w:val="en-GB"')
        zout.writestr(item, data)
    for name, (rid, target) in media.items():
        zout.write(CAPTURES / f'{name}.png', 'word/' + target)
print('OK', OUT, 'figures:', fig[0], 'images:', len(media))
