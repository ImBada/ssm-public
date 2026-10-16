import base64, re, pathlib
src = pathlib.Path('src.html').read_text()
def rep(m):
    b = base64.b64encode(pathlib.Path(m.group(1)).read_bytes()).decode()
    mime='image/png' if m.group(1).endswith('.png') else 'image/svg+xml'
    return f'src="data:{mime};base64,{b}"'
out = re.sub(r'src="(assets/[^"]+\.(?:svg|png))"', rep, src)
pathlib.Path('ssm-main-wix.html').write_text(out)
print(len(out))
