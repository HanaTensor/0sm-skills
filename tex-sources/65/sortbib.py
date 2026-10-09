"""sortbib.py — order a manual thebibliography by first citation as typeset.

Usage (in the directory that holds main.tex):
    python3 sortbib.py sort    # compile, read main.aux, reorder \\bibitem, write main.tex
    python3 sortbib.py check   # compile and report whether the order already matches
Requires pdflatex. Builds in ./_sortbib_build so the source folder stays clean.
"""
import re, sys, subprocess, os, shutil
SRC = 'main.tex'
B = '_sortbib_build'

def compile_():
    os.makedirs(B, exist_ok=True)
    shutil.copy(SRC, os.path.join(B, 'main.tex'))
    for _ in range(3):
        subprocess.run(['pdflatex', '-interaction=nonstopmode', 'main.tex'], cwd=B,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def aux_order():
    a = open(os.path.join(B, 'main.aux'), encoding='latin-1').read()
    order = []
    for m in re.finditer(r'\\citation\{([^}]*)\}', a):
        for k in m.group(1).split(','):
            k = k.strip()
            if k and not k.endswith('Control') and k not in order:
                order.append(k)
    return order

mode = sys.argv[1] if len(sys.argv) > 1 else 'check'
compile_()
s = open(SRC, encoding='utf-8').read()
cit = aux_order()
bib = re.findall(r'\\bibitem\{([^}]*)\}', s)
if mode == 'check':
    print('cited', len(cit), 'bibitems', len(bib), 'same order:', cit == bib)
    print('uncited bibitems:', [k for k in bib if k not in cit])
    print('cited without bibitem:', [k for k in cit if k not in bib])
    sys.exit(0 if cit == bib else 1)
tag = re.search(r'\\begin\{thebibliography\}\{[^}]*\}', s)
i0, i1 = tag.end(), s.index('\\end{thebibliography}')
items = re.split(r'(?=\\bibitem\{)', s[i0:i1])
entries = {re.match(r'\\bibitem\{([^}]*)\}', e).group(1): e.strip('\n') for e in items[1:]}
assert set(entries) == set(cit), set(entries) ^ set(cit)
s = s[:i0] + '\n\n' + '\n\n'.join(entries[k] for k in cit) + '\n\n' + s[i1:]
open(SRC, 'w', encoding='utf-8').write(s)
print('sorted', len(cit))
