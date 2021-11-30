# How to use

1. 실행 프로그램과 같은 경로에 변환을 원하는 coe 파일을 함께 위치시킴
2. 실행 프로그램을 실행
3. coe 파일의 이름을 입력
    - 단, 경로를 포함하지 않은 파일의 이름을 확장자와 함께 입력
    - ex) sram4.coe(o), documents/sram4.coe(x), sram4(x)
    - 상대 경로 기준이므로 하위 폴더 "documents"에 coe 파일이 존재한다면, "documents/sram4.coe" 와 같은 경우는 가능
4. 실행완료 및 변환 파일 생성(월_일_시분초_weight.npy)
    1. "Convert success!" 메시지 출력 시, 아무 키나 입력하고 종료
    2. "Convert Fail..." 메시지 출력 시, coe 파일의 위치 혹은 오타 입력 여부 확인 후 재실행