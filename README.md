# Simple_Post_Crawler  
허가를 받고 needleworm 님의 https://github.com/needleworm/post_crawler 코드를 바탕으로  
제가 사용하는 환경에 맞춰 개조하였음을 밝힙니다.  

복무지 컴퓨터에서 구동시키기 위해 제작한 코드인 만큼  
다른 PC에서의 구동을 보장하지 못합니다.  
64비트 Windows 10 환경에서 구동을 확인했습니다.  

실행에 Python3, selenium, 그리고 사용하시는 크롬 버전에 맞는  
Chromedriver가 필요합니다.  
  
입력 파일은 names.txt를 생성한 뒤  
해당 텍스트 파일에 우편번호 (등기번호)와 수취인명을  
한 줄에 하나씩 입력하시면 됩니다.  

예시:  
123456789 홍길동  
