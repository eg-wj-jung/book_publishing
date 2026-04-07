<!-- Parent: ../AGENTS.md -->

# book-accounting-analytics-v2

## Purpose
Claude Code AI 에이전트 팀이 Word 문서(.docx)로 전문 교재를 작성하는 프로젝트. 단일 설정 파일(`.claude/book-toc.md`)만 교체하면 다른 주제의 책도 동일 과정으로 제작 가능. 자동화된 리뷰/검증 파이프라인 포함.

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

### Core Dependencies
Python: python-docx (Word 생성), matplotlib (다이어그램), jinja2 (템플릿)
Claude Code: Agent SDK, /research /write /review /publish /cover 슬래시 커맨드

### Working in This Directory
- 모든 콘텐츠는 `.claude/book-toc.md`의 페르소나로 작성
- 최종 문서에는 에이전트 내부 역할명 미노출
- 전문 용어: 괄호 안 영문 병기 (예: 지표(indicator))
- Heading으로만 장 구분 (수평선 사용 금지)
- 예시 연도: book-toc.md의 "기준 연도" 따르기 (사실 정보 제외)
- [그림] 플레이스홀더: matplotlib으로 실제 이미지 생성 필수

### Common Patterns
- 대화 중단: 해당 단계의 마지막 저장 파일 읽고 이어붙이기 (덮어쓰지 않음)
- 분량 관리: 12만~15만 자는 한 번에 안 됨 → 부(Part) 단위로 나눠 진행
- 마크다운 → Word: python-docx로 자동 변환 (** 기호 제거 확인)
- 다이어그램: matplotlib으로 생성 → output/images/ 저장

### When Modifying
- `book-toc.md`: 제목, 목차, 페르소나, 스타일, 사양 변경 (CLAUDE.md 수정 불필요)
- `/research`: 웹 검색 범위/깊이 조정 필요하면 .claude/book-toc.md의 리서치 지침 참고
- `/write`: 초안 분량 부족하면 부별로 재실행 (이어붙이기)
- `/review`: 합평 3라운드 초과 안 됨 → 3라운드 후 /publish 진행
- `/publish`: Word 생성 후 최종 검토 필수 (PDF 변환 전)
