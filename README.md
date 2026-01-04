# [IBM x Red Hat] AI Transform AX Academy 교육 과정 정리

본 저장소는 **IBM x Red Hat AI Transform AX Academy** 교육 과정에서 학습한  
AI · 데이터 · 웹 · 서버 · 클라우드 관련 내용을 **실습 및 구현 중심**으로 정리한 기록입니다.

> 단순 이론 나열이 아닌  
> **직접 코드 작성, 환경 구성, 서버·DB·AI 연동 경험**을 중심으로 구성되어 있습니다.

---

## 📌 교육 과정 개요

- **교육명**: AI Transform AX Academy  
- **주관**: IBM × Red Hat
- **모집요강**: [K-Digital Training 디지털 선도기업 아카데미 [IBM x RedHat] AI Transformation - AX Academy](https://www.hi-kdt.com/)

### 🎯 교육 목표
- AI·데이터 기반 서비스 구현 역량 강화
- 웹–서버–DB–AI를 연결하는 **엔드투엔드 구조 이해**
- Linux 기반 서버 환경 및 오픈소스 활용 능력 습득
- 실무 환경에서 발생하는 문제를 정의하고 해결하는 구현 경험 확보
- 클라우드·컨테이너 환경(Docker, Kubernetes, AWS)을 포함한  
  **현대적인 AI 서비스 운영 인프라 개념 이해**

---

## 🧠 주요 학습 영역

### 1️⃣ AI & 데이터 분석
- Python 기반 데이터 처리 및 분석
- 형태소 분석 및 토큰화 실습
- 이미지 분석 기초
- AI 모델 활용을 위한 데이터 전처리 경험

### 2️⃣ 웹 개발 (Frontend & Backend 기초)
- JavaScript 기본 문법 및 DOM 조작
- jQuery를 활용한 동적 웹 페이지 구현
- React 기반 SPA 구조 이해 및 실습
- 로그인 시스템 및 인증 흐름 구현

### 3️⃣ 서버 & 네트워크
- Apache 웹 서버 환경 구성
- 로컬 서버와 웹 서버 연결
- Node.js 기반 서버 연동 실습
- REST 구조 및 요청/응답 흐름 이해

### 4️⃣ 데이터베이스
- Oracle DB 서버 연결
- 데이터 저장·조회·관리 흐름 이해
- 서버–DB 연동 구조 실습

### 5️⃣ 크롤링 & 데이터 수집
- 웹 크롤링을 통한 데이터 수집
- 수집 데이터 구조화 및 활용

### etc. 클라우드 & 컨테이너 기반 인프라 이해
- Docker를 활용한 컨테이너 개념 이해
- 애플리케이션 실행 환경의 표준화 필요성 학습
- Kubernetes 기본 개념 및 오케스트레이션 구조 이해
- 클라우드 환경에서 서비스가 배포·운영되는 전체 흐름 이해
- AWS 기반 인프라 구성 개념 학습
  - 컴퓨팅 / 스토리지 / 네트워크 역할 구분
  - 온프레미스 환경과 클라우드 환경의 차이점 이해

---

## 📂 디렉토리 구조

```text
.
├─ AI/
│  └─ 이미지 분석 및 AI 관련 실습
│
├─ crawling/
│  └─ 웹 크롤링 실습 코드
│
├─ fast/project/
│  └─ 로그인 시스템 구현
│
├─ httpd/Apache24/htdocs/
│  └─ Apache 로컬 웹 서버 연동 실습
│
├─ jQuery/jQuERY/
│  └─ jQuery 기반 웹 동작 구현
│
├─ javascript/
│  └─ JavaScript 기본 문법 및 실습
│
├─ oracle/
│  └─ Oracle DB 서버 연결 및 실습
│
├─ practice/
│  └─ Node.js 연동 및 종합 실습
│
├─ python/
│  └─ Python 기초 및 데이터 처리
│
├─ react/do-it-example/
│  └─ React 기반 웹 페이지 구현
│
└─ token/
   └─ 형태소 분석 및 토큰화 실습
