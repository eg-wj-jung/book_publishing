---
name: publish
description: "리뷰 완료된 최종 원고를 Word 문서로 변환하고 출판 메타데이터를 생성한다. /review 다음에 실행."
user_invocable: true
---

# 퍼블리싱 + 메타데이터

이 스킬은 2단계를 순서대로 수행한다.

## 시작 전 준비

`.claude/book-toc.md`를 읽고 다음을 파악한다:
- 기본 정보: 제목, 필명, 판형
- 목차: 부 제목, 부 부제, 장 제목 (헤딩 구조에 사용)
- 퍼블리싱 사양: 폰트, 색상, 여백, 문서 구성 요소, 시각 자료, 이미지 생성 규칙

---

## 1단계: Word 문서 생성

입력: `draft/11_draft-final.md`

`.claude/book-toc.md`의 "퍼블리싱 사양" 섹션에 정의된 모든 서식 규칙을 적용하여 Word 문서를 생성한다.

출력:
- python-docx를 사용하여 .docx 파일로 변환
- 문서 작성자(author) 속성은 `.claude/book-toc.md`의 필명으로 설정
- `output/generate_images.py`, `output/generate_docx.py`, `output/final.docx`

## 2단계: 출판 메타데이터 생성

최종 원고를 기반으로 출판에 필요한 메타데이터를 생성한다.

생성 항목:
- 도서 분류: BISAC(국제) 및 KDC(한국) 분류 코드
- 판매 카피: "후킹 → 가치 → 독자가 얻을 것 → 행동 유도" 구조의 도서 설명문 (내용 요약이 아닌 판매 목적)
- 검색 키워드: 독자가 실제로 검색하는 단어 기준 7~10개
- 가격 전략: 경쟁 도서 분석 기반 권장 가격대
- 플랫폼별 배포 설정: 교보문고, 리디북스, 예스24, 밀리의 서재, 아마존 KDP

출력: `output/metadata.md`

완료되면 사용자에게 안내한다: "퍼블리싱 완료. output/final.docx(최종 문서)와 output/metadata.md(출판 메타데이터)가 생성되었습니다."
