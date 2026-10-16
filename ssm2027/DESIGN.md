# SSM 2027 디자인 가이드

SSM 2027 관련 결과물(웹 페이지, OG 이미지, YouTube 배너·프로필, 포스터 파생물 등)을 만들 때 항상 이 문서를 따른다.
기준은 `ssm2027_공유용_out (2).ai` 포스터다. 실제 적용 예시는 `src.html`, `og/og.html`, `youtube/*.html`을 보면 된다.

---

## 1. 핵심 원칙

1. **포스터에 있는 요소만 쓴다.** 새로운 장식, 아이콘, 일러스트를 만들지 않는다.
2. **텍스트는 지어내지 않는다.** 기존 superspeedrun.com 문구나 포스터 문구를 그대로 쓴다. 새 문장이 꼭 필요하면 먼저 확인받는다. 문구를 새로 쓰면 AI가 쓴 글처럼 보인다.
3. **AI 템플릿처럼 보이는 요소는 쓰지 않는다.** 금지 목록은 [9. 하지 말 것](#9-하지-말-것)에 있다.
4. **게임 느낌은 포스터의 동키콩 구조로 낸다.** 빨간 점선 발판, 파란 사다리, ✚ 표시, 픽셀 모서리를 쓴다.

---

## 2. 색상

| 이름 | 값 | 쓰는 곳 |
|---|---|---|
| 배경 | `#000000` | 모든 배경. 포스터 이미지의 회색(`#1b1b1b`)은 잘못 나온 색이므로 쓰지 않는다. |
| 노랑 | `#ffef00` | 로고 글자, 강조 숫자(모금액), 이메일, 기본 버튼, 강조 문구, 엠블럼 |
| 빨강 | `#eb3728` | 3색 어긋남 효과의 첫 번째 그림자 |
| 파랑 | `#0087c9` | 3색 어긋남 효과의 두 번째 그림자 |
| 발판 빨강 | `#b8384a` | 점선 발판(girder) |
| 사다리 파랑 | `#3b5bdb` | 사다리 |
| 본문 흰색 | `#f2f2ee` | 제목, 본문, 흰 로고 |
| 본문 회색 | `#d2d2cc` | 긴 본문 단락 |
| 보조 회색 | `#8b8b86` | 라벨, 주석, 작은 설명 |

- 노랑, 빨강, 파랑은 포스터 로고 SVG(`assets/logo.svg`)의 원래 색이다.
- 파트너 로고(올댓마인드, 메이크어위시, 치지직, 바다게임즈)는 검은 배경에 맞춰 **흰색 단색**으로 쓴다.

---

## 3. 폰트

**전부 [갈무리(Galmuri)](https://galmuri.quiple.dev/)로 통일한다.** 다른 폰트(Pretendard 등)는 쓰지 않는다.

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/galmuri@latest/dist/galmuri.css">
```

| 용도 | 폰트 | 굵기 | 크기 |
|---|---|---|---|
| 큰 숫자, 날짜, 제목, 라벨, 버튼 | `Galmuri11` | 700 | 12 / 24 / 36px 등 12의 배수가 가장 선명함 |
| 긴 본문 단락 | `Galmuri14` | 400 | 15px, 줄간격 1.85 |
| 작은 라벨, 보조 설명 | `Galmuri11` | 400 | 12px |

- 날짜는 Galmuri11 Bold에 [3색 어긋남 효과](#4-3색-어긋남-효과)를 준다.
- 숫자 열에는 `font-variant-numeric: tabular-nums`를 쓴다.

---

## 4. 3색 어긋남 효과

포스터 로고와 날짜처럼, 글자 뒤로 빨강과 파랑이 오른쪽으로 어긋나게 겹치는 효과다.

```css
/* 글자 */
text-shadow: 3px 0 0 #eb3728, 6px 0 0 #0087c9;      /* 큰 제목은 5px / 10px까지 */

/* 이미지(엠블럼 단색 등) */
filter: drop-shadow(8px 0 0 #eb3728) drop-shadow(8px 0 0 #0087c9);
```

- 날짜, 큰 타이틀, 프로필 엠블럼에만 쓴다. 본문에는 쓰지 않는다.

---

## 5. 로고·이미지 에셋 (`assets/`)

| 파일 | 내용 | 사용법 |
|---|---|---|
| `logo.svg` | SUPER SPEEDRUN MARATHON 2027 로고 (노랑+3색) | 메인 타이틀 |
| `title-ko.svg` | 슈퍼 스피드런 마라톤 2027 한글 타이틀 | 로고 아래 |
| `emblem.svg` | 방패 엠블럼, 투명도 18% | 타이틀 뒤 배경 장식 |
| `emblem-solid.svg` | 방패 엠블럼, 노랑 단색 | 프로필 사진 등 엠블럼 단독 사용 |
| `allthatmind.svg` | 올댓마인드 로고 (흰색) | 장소 |
| `chzzk.svg` | 치지직 로고 (흰색, chzzk.naver.com 사이트 로고) | 방송 |
| `maw.png` | Make-A-Wish KOREA 로고 (흰색) | 협력 |
| `bada.png` | BADA GAMES 로고 (흰색) | 제작 |

### 엠블럼 정렬 규칙
엠블럼은 왼쪽에만 날개가 있어 좌우가 비대칭이다. **위아래 꼭지(뾰족한 끝)가 이미지 너비의 63.7% 지점**에 있으므로, 가운데 정렬할 때는 이미지 상자가 아니라 이 축을 기준으로 맞춘다.

```css
/* 타이틀 뒤 배경: 로고 상자 기준 */
.emblem{position:absolute;left:50%;top:50%;width:116%;transform:translate(-63.7%,-50%)}
```

- 타이틀 뒤에 쓸 때는 로고 너비의 116%로, 로고의 세로 중심에 맞춘다.

---

## 6. 게임 요소 (동키콩 구조)

### 점선 발판 (girder)
빨간 점선 두 줄이 엇갈린 모양이다. 섹션 구분선으로 쓰고, 회색 실선은 쓰지 않는다.

```css
.girder{height:16px;
  background:
    repeating-linear-gradient(90deg,#b8384a 0 9px,transparent 9px 15px) 0 0/100% 5px no-repeat,
    repeating-linear-gradient(90deg,#b8384a 0 9px,transparent 9px 15px) 7px 11px/100% 5px no-repeat}
```

- 좌우로 번갈아 한쪽을 7~8% 짧게 하고, ±0.35~0.9도 기울여 지그재그로 내려가게 한다.
- 모바일에서는 기울기를 없애고 평평하게 둔다.

### 사다리 (ladder)
파란 점선 기둥 두 개와 가로대로 되어 있고, 위아래 발판을 잇는다. 너비는 44~64px다.

```css
.ladder{width:64px;
  background:
    repeating-linear-gradient(0deg,#3b5bdb 0 5px,transparent 5px 9px) 0 0/5px 100% no-repeat,
    repeating-linear-gradient(0deg,#3b5bdb 0 5px,transparent 5px 9px) 100% 0/5px 100% no-repeat,
    repeating-linear-gradient(0deg,transparent 0 22px,#3b5bdb 22px 27px) 50% 0/calc(100% - 18px) 100% no-repeat;
  mask:repeating-linear-gradient(90deg,#000 0 5px,transparent 5px 9px)}
```

- **많이 쓰지 않는다.** 모든 섹션에 넣으면 답답해 보이므로 띄엄띄엄 넣는다.
- 글자나 로고와 겹치지 않는 빈 칸에만 둔다. 모바일에서는 숨긴다.

### ✚ 표시
포스터의 "✚ 협력"처럼 제목 앞에 붙이는 픽셀 더하기 표시다. 15×15px 크기에 굵기 5px, 흰색이다.

```css
h2::before{content:"";display:inline-block;width:15px;height:15px;margin-right:12px;
  background:linear-gradient(#f2f2ee,#f2f2ee) center/5px 100% no-repeat,
             linear-gradient(#f2f2ee,#f2f2ee) center/100% 5px no-repeat}
```

### 픽셀 모서리
버튼과 타일의 모서리를 계단 모양으로 깎는다. 버튼은 4px, 타일은 6px로 깎는다.

```css
clip-path:polygon(0 4px,4px 4px,4px 0,calc(100% - 4px) 0,calc(100% - 4px) 4px,100% 4px,
  100% calc(100% - 4px),calc(100% - 4px) calc(100% - 4px),calc(100% - 4px) 100%,
  4px 100%,4px calc(100% - 4px),0 calc(100% - 4px));
```

### 포스터 크레딧 구조
장소, 방송, 협력, 후원, 제작은 포스터 하단처럼 3단 발판 위에 놓는다.
- 1단: 장소(왼쪽) + 방송(오른쪽)
- 2단: 협력(가운데)
- 3단: 후원(왼쪽) + 제작(오른쪽)

라벨은 `한글` 위, `English` 아래로 두 줄로 쓴다(예: 장소 / Venue).

---

### 행사 시작 타이머
날짜 아래에 둔다. 박스나 테두리 없이 라벨 하나와 숫자만 둔다.
- 라벨은 Galmuri11 Bold 12px, 보조 회색이다.
- 숫자는 Galmuri11 Bold 48px(모바일 36px), 노랑, `tabular-nums`로 쓴다. 형식은 `96일 08:04:40`이다.
- 행사가 시작되면 라벨이 `LIVE ON`으로 바뀌고, 스피드런 타이머처럼 경과 시간 `HH:MM:SS`가 올라간다.
- 행사가 끝나면 `visibility:hidden`으로 숨긴다. 높이를 유지해야 Wix 임베드 높이가 바뀌지 않는다.

## 7. 버튼

| 종류 | 모양 | 예 |
|---|---|---|
| 기본 | 노랑 배경, 검정 글자. 마우스를 올리면 흰 배경 | 방송 보기, 기부 |
| 보조 | 투명 배경, 흰 테두리 2px. 마우스를 올리면 흰 배경에 검정 글자 | Discord 서버, Youtube 채널 |

- 글자는 Galmuri11 Bold 12px, 여백은 14px 30px, 모서리는 픽셀 모서리 4px로 한다.

---

## 8. 레이아웃·출력 규격

### 웹 (Wix HTML 임베드)
- **데스크톱 본문 너비는 920px로 고정한다.** 글자와 로고 크기도 고정값을 쓴다. 너비가 바뀌어도 높이가 그대로여야 Wix 임베드 안에 스크롤이 생기지 않는다.
- 960px 이하에서만 모바일 레이아웃(본문 너비 90%)으로 바뀐다.
- 상단 메뉴와 바닥글은 Wix에 이미 있으므로 넣지 않는다.
- 이미지는 `build.py`로 HTML 안에 넣어 파일 하나로 만든다.

### 이미지 규격
| 용도 | 크기 | 비고 |
|---|---|---|
| OG 이미지 | 1200×630 | 핵심 내용은 가운데에 둔다. 정사각형으로 잘려도 보이게 하기 위함이다. |
| YouTube 배너 | 2560×1440 | 모든 기기에서 보이는 영역은 **가운데 1546×423**이다. 로고와 날짜는 이 안에 넣는다. |
| YouTube 프로필 | 800×800 (원형으로 잘림) | 엠블럼 단색, 너비 640px, 꼭지 축을 정중앙에 둔다. 양옆은 조금 잘려도 된다. |

---

## 9. 하지 말 것

이전 시안에서 "AI가 디자인한 것 같다"는 피드백을 받고 뺀 것들이다.

- CRT 스캔라인 같은 화면 줄무늬 효과
- 깜빡이거나 들썩이는 애니메이션
- 아이콘과 이모지가 들어간 기능 카드 3개 묶음
- 섹션마다 붙는 `✚ ABOUT` 같은 작은 영문 라벨(eyebrow)
- RPG 대화창, "PRESS START", "SELECT STAGE", "GAME OVER? NEVER" 같은 게임 클리셰 문구
- 그림자가 진 버튼을 여러 개 늘어놓는 구성, 테두리 박스에 넣은 큰 카운트다운 타이머. 타이머는 위 규칙대로 박스 없이 쓴다.
- 원문에 없는 문구, 카피라이팅, 문장 다듬기
- 갈무리 이외의 폰트, 회색 배경
