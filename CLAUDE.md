# ssm-public

슈퍼 스피드런 마라톤(SSM) 공개 작업물 저장소.

## SSM 2027 작업 규칙
- SSM 2027 관련 결과물(웹, OG, YouTube, 포스터 파생물)은 항상 `ssm2027/DESIGN.md`를 먼저 읽고 따른다.
- 텍스트는 지어내지 않는다. 기존 superspeedrun.com 문구나 포스터 문구를 그대로 쓴다.
- 메인 페이지는 `ssm2027/src.html`을 고친 뒤 `ssm2027` 폴더에서 `python3 build.py`를 실행해 `ssm-main-wix.html`을 만든다. 높이가 바뀌면 `README.md`의 Wix 임베드 높이도 갱신한다.
- 이미지는 jsDelivr CDN(커밋 해시 고정)으로 불러오므로, `assets/`를 바꿨다면 커밋·푸시 후 빌드한다.
