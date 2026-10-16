"""src.html -> ssm-main-wix.html

기본: 이미지 경로(assets/...)를 GitHub 공개 저장소의 jsDelivr CDN 주소로 바꾼다.
      assets/ 를 마지막으로 바꾼 커밋 해시로 고정하므로, 이미지를 바꿨다면 먼저 커밋·푸시한 뒤 빌드할 것.
--inline: 예전 방식. 이미지를 base64로 HTML 안에 넣는다(인터넷 CDN 없이도 동작, 파일이 커짐).
"""
import base64, re, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent
REPO = 'ImBada/ssm-public'
src = (ROOT / 'src.html').read_text()
pattern = r'src="(assets/[^"]+\.(?:svg|png))"'

if '--inline' in sys.argv:
    def rep(m):
        b = base64.b64encode((ROOT / m.group(1)).read_bytes()).decode()
        mime = 'image/png' if m.group(1).endswith('.png') else 'image/svg+xml'
        return f'src="data:{mime};base64,{b}"'
else:
    git = lambda *a: subprocess.run(['git', '-C', str(ROOT), *a], capture_output=True, text=True).stdout.strip()
    if git('status', '--porcelain', '--', 'assets'):
        sys.exit('assets/ 에 커밋하지 않은 변경이 있음. 커밋·푸시한 뒤 다시 빌드할 것.')
    commit = git('log', '-1', '--format=%H', '--', 'assets')
    if not git('branch', '-r', '--contains', commit):
        sys.exit(f'assets/ 커밋 {commit[:7]} 이 아직 GitHub에 푸시되지 않음. 푸시한 뒤 다시 빌드할 것.')
    base = f'https://cdn.jsdelivr.net/gh/{REPO}@{commit}/ssm2027/'
    rep = lambda m: f'src="{base}{m.group(1)}"'

out = re.sub(pattern, rep, src)
(ROOT / 'ssm-main-wix.html').write_text(out)
print(len(out))
