// Wix 홈 페이지의 Velo 페이지 코드
// HTML 임베드 요소 ID가 #html1이 아니면 실제 ID로 바꿀 것 (요소 선택 → 속성 패널에서 확인)
$w.onReady(function () {
  // Velo에는 HTML 임베드 높이를 바꾸는 API가 없음. 스크롤바만 끈다.
  // 내용이 임베드보다 길어지는 경우는 ssm-main-wix.html 안의 fit()이 축소해서 맞춤.
  $w('#html1').scrolling = 'no';
});
