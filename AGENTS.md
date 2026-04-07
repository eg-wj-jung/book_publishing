<!-- Parent: ../AGENTS.md -->

# book-empirical-r-v2

## Purpose
Claude Code AI 에이전트 팀이 Word 문서(.docx)로 R 실증회계연구 교재를 작성하는 프로젝트. `R을 이용한 실증회계연구` v2 버전. 단일 설정 파일(`.claude/book-toc.md`)만 교체하면 다른 주제도 가능한 재사용 가능 하네스.

## Key Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | 프로세스 정의, 범용 작성 규칙, 품질 기준 (수정 불필요) |
| `.claude/book-toc.md` | 제목, 필명, 페르소나, 목차, 작성 스타일, 퍼블리싱 사양 (★ 유일 교체 대상) |
| `.claude/skills/research.md` | /research 스킬 (웹 검색 조사) |
| `.claude/skills/write.md` | /write 스킬 (구조 설계 + 초안) |
| `.claude/skills/review.md` | /review 스킬 (내부+외부 리뷰) |
| `.claude/skills/publish.md` | /publish 스킬 (Word 변환 + 메타데이터) |
| `.claude/skills/cover.md` | /cover 스킬 (표지 디자인 독립) |
| `output/final.docx` | 최종 Word 문서 |
| `output/metadata.md` | 출판 메타데이터 |

## Subdirectories

| Directory | Purpose | Status |
|-----------|---------|--------|
| `.claude/` | 프로젝트 설정 + 스킬 정의 | 활발 |
| `draft/` | 작업 산출물 (번호 순서: 01_research → 14_review-proofreader) | 활발 |
| `output/` | 최종 산출물 (final.docx, metadata.md, 다이어그램, 표지 이미지) | 활발 |

## For AI Agents

### Key Concepts
- **Workflow**: /research → /write → /review → /publish (순서 필수)
- **/cover**: 독립 스킬 (언제든 실행 가능)
- **Review Pipeline**: 비평가 → 독자 관점 → 합평 → 편집자 → 마케터 → 프루프리더 (5가지 관점)
- **Quality Gate**: 합평 단계에서 🔴(필수) 0건 + 평균 9점 이상 통과
- **Output Numbering**: draft/ 파일은 생성 순서대로 01~14 번호 자동 부여
- **Target Audience**: R 실증회계연구 학생/연구자

### Core Dependencies
Python: python-docx (Word 생성), matplotlib (다이어그램), jinja2 (템플릿)
Claude Code: Agent SDK, /research /write /review /publish /cover 슬래시 커맨드

### Working in This Directory
- 모든 콘텐츠는 `.claude/book-toc.md`의 페르소나로 작성 (전문가/실무자)
- 최종 문서에는 에이전트 내부 역할명 미노출
- R 코드 예제: tidyverse 스타일, 실행 가능해야 함
- 통계 개념 설명: 이론 + R 구현 + 해석 순서
- 전문 용어: 괄호 안 영문 병기
- Heading으로만 장 구분 (수평선 사용 금지)
- [그림] 플레이스홀더: matplotlib + R ggplot2 산출물로 생성

### Common Patterns
- R 코드 블록: 실행 결과까지 포함 (출력 예시)
- 데이터셋: 강의용 공개 데이터 활용 (CRSP, Compustat 등)
- 회귀분석: 모형 설정 → 가정 검증 → 결과 해석 순서
- 그래프: ggplot2 기반 출판 수준 시각화
- 대화 중단: 해당 단계의 마지막 저장 파일 읽고 이어붙이기 (덮어쓰지 않음)

### When Modifying
- `book-toc.md`: 제목, 목차, 페르소나, 스타일, 사양 변경
- R 코드 예제 추가: 실행 환경 명시 (tidyverse, data.table 등)
- 이론/실습 분량 조정: book-toc.md의 목차와 작성 가이드 확인
- `/write`: 초안 분량 부족하면 부별로 재실행 (이어붙이기)
- `/review`: 합평 3라운드 초과 안 됨 → 3라운드 후 /publish 진행
