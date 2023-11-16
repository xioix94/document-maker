# document-maker

# 해당 프로젝트는 chat gpt를 이용해서 기획서 및 기타 문서의 초안을 작성함을 목표로 합니다.

# 로컬에 이미 존재하는 레거시 문서들이 이미 있음에도 새로운 문서에 같은 내용을 다시 작성하는 불상사를 방지하고자 시작했습니다.

# 또한 기업의 문서를 웹에 드래그하는 방식을 고려했으나 기밀 문서를 해당 프로그램에 이용할 경우를 생각하여 프로그램 형태로 고안했습니다. (openai에는 데이터를 제공하는 부분은 어쩔 수 없는 한계입니다. 챗봇을 온프레미스로 만들 수 있다면 베스트일 것입니다.)

# 프로그램의 실행 시 로컬에 존재하는 파일의 개수에 비례하여 실행되는 시간이 늘어나니 참고 바랍니다.

# openai의 chat gpt api를 사용하므로 openai 크레딧이 필요합니다.

# 사용 시 필요 모듈 설치
pip install python-docx PyPDF2
pip install PyQt5

![image (3)](https://github.com/xioix94/document-maker/assets/53420414/175f96d6-5326-4d2e-9c2d-fc8ab3cc1425)

# 사용법
# 1. openai 토큰 발급
# 2. 키워드 입력 후 File Search 버튼 클릭
# 3. openai 토큰 입력
# 4. 간단한 문서 주제, 설명, 구체적 개요가 있을 경우 입력 후 Create Document 버튼 클릭
# 5. 출력된 초안 이용
