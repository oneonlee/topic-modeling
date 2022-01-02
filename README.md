# topic-modeling
Topic Modeling, LDA

## Settings
- Python 버전은 `3.5`에서 `3.8` 사용 필수
- 먼저 [https://wikidocs.net/22488](https://wikidocs.net/22488)의 **5. 윈도우에서 KoNLPy 에러가 발생하는 경우**를 참고하여 
  - Python 버전에 맞는 JDK 설치 [설치 링크](https://www.oracle.com/java/technologies/downloads/#java8-windows)
  - JDK 환경 변수 설정
  - JPype 설치
  - 설치 후, 아래의 명령어로 Java가 설치된 것을 확인할 수 있음
    - `java -version` 
    - `konlpy`의 경우 Java Development Kit 17 버전을 사용해야 함.
    - 참고 : `PyKomoran`의 경우 Java Development Kit 8 버전을 사용해야 함.

<br>

- 그 후 명령창에 아래 명령어를 순서대로 하나씩 입력

```
pip install --upgrade pip
pip install jupyter
pip install pandas
pip install konlpy
pip install tweepy==3.10.0
pip install git+https://github.com/ssut/py-hanspell.git
pip install gensim==3.8.3
pip install pyLDAvis
pip install tqdm
pip install matplotlib
```
<!-- pip install PyKomoran -->

## References
- [딥 러닝을 이용한 자연어 처리 입문](https://wikidocs.net/book/2155)
- [KoNLPy 0.6.0 documentation](https://konlpy-ko.readthedocs.io/ko/latest/)
