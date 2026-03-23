#!/usr/bin/env python3
"""전자책 표지 생성 스크립트 — 메인안(A) + 대안(B)"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import font_manager
import os

# 폰트 설정
font_candidates = [
    '/Users/jaydenkang/Desktop/New Projects/20260321_노트북LM 책쓰기_스킬/font/Pretendard-Bold.otf',
    '/Users/jaydenkang/Desktop/New Projects/20260321_노트북LM 책쓰기_스킬/font/Pretendard-ExtraBold.otf',
    '/Users/jaydenkang/Desktop/New Projects/20260321_노트북LM 책쓰기_스킬/font/Pretendard-Medium.otf',
    '/Users/jaydenkang/Desktop/New Projects/20260321_노트북LM 책쓰기_스킬/font/Pretendard-Regular.otf',
]

fonts = {}
for path in font_candidates:
    if os.path.exists(path):
        name = os.path.basename(path).replace('.otf', '').replace('.ttf', '')
        fp = font_manager.FontProperties(fname=path)
        fonts[name] = fp

# 폴백
if not fonts:
    for path in font_manager.findSystemFonts():
        if 'Malgun' in path or 'malgun' in path:
            fp = font_manager.FontProperties(fname=path)
            fonts['fallback'] = fp
            break

def get_font(style='Pretendard-Bold'):
    if style in fonts:
        return fonts[style]
    return list(fonts.values())[0] if fonts else font_manager.FontProperties()


def create_cover_a(output_path):
    """메인안 A: 딥 네이비 배경, 골드 강조"""
    # B5 비율 (176x250mm) → 1600x2286px 근사
    fig, ax = plt.subplots(1, 1, figsize=(7.04, 10), dpi=227)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    fig.patch.set_facecolor('#1B2A4A')
    ax.set_facecolor('#1B2A4A')

    # 상단 얇은 골드 라인
    ax.add_patch(patches.Rectangle((0.08, 0.88), 0.84, 0.003, color='#FFD43B'))

    # 부제
    ax.text(0.5, 0.84, '팀장이 바로 쓰는 실전 활용법 20',
            fontproperties=get_font('Pretendard-Medium'),
            fontsize=14, color='#FFFFFF', alpha=0.8,
            ha='center', va='center')

    # 메인 타이틀 1줄: "노트북LM으로"
    ax.text(0.5, 0.68, '노트북LM으로',
            fontproperties=get_font('Pretendard-Bold'),
            fontsize=38, color='#FFFFFF',
            ha='center', va='center')

    # 메인 타이틀 2줄: "다 됨"
    ax.text(0.5, 0.52, '다 됨',
            fontproperties=get_font('Pretendard-ExtraBold'),
            fontsize=72, color='#FFD43B',
            ha='center', va='center',
            fontweight='bold')

    # 하단 구분선
    ax.add_patch(patches.Rectangle((0.08, 0.28), 0.84, 0.003, color='#FFD43B'))

    # 체크마크 심볼
    ax.text(0.5, 0.20, '✓',
            fontsize=36, color='#4DABF7',
            ha='center', va='center')

    # 저자명
    ax.text(0.5, 0.10, 'AI ROASTING',
            fontproperties=get_font('Pretendard-Regular'),
            fontsize=14, color='#FFFFFF', alpha=0.9,
            ha='center', va='center',
            style='italic')

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.savefig(output_path, bbox_inches='tight', pad_inches=0, facecolor='#1B2A4A')
    plt.close()
    print(f"메인안(A) 저장: {output_path}")


def create_cover_b(output_path):
    """대안 B: 화이트 배경, 구글 컬러"""
    fig, ax = plt.subplots(1, 1, figsize=(7.04, 10), dpi=227)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')

    # 상단 구글 4색 스트라이프
    google_colors = ['#4285F4', '#EA4335', '#FBBC05', '#34A853']
    stripe_width = 0.84 / 4
    for i, color in enumerate(google_colors):
        ax.add_patch(patches.Rectangle(
            (0.08 + i * stripe_width, 0.90), stripe_width, 0.015, color=color))

    # 부제
    ax.text(0.5, 0.84, '팀장이 바로 쓰는 실전 활용법 20',
            fontproperties=get_font('Pretendard-Medium'),
            fontsize=14, color='#666666',
            ha='center', va='center')

    # 메인 타이틀 1줄
    ax.text(0.5, 0.66, '노트북LM으로',
            fontproperties=get_font('Pretendard-Bold'),
            fontsize=38, color='#1A1A1A',
            ha='center', va='center')

    # 메인 타이틀 2줄
    ax.text(0.5, 0.50, '다 됨',
            fontproperties=get_font('Pretendard-ExtraBold'),
            fontsize=72, color='#4285F4',
            ha='center', va='center',
            fontweight='bold')

    # 하단 구글 4색 점
    dot_y = 0.30
    dot_positions = [0.38, 0.46, 0.54, 0.62]
    for pos, color in zip(dot_positions, google_colors):
        ax.plot(pos, dot_y, 'o', color=color, markersize=10)

    # 저자명
    ax.text(0.5, 0.12, 'AI ROASTING',
            fontproperties=get_font('Pretendard-Regular'),
            fontsize=14, color='#1A1A1A', alpha=0.7,
            ha='center', va='center')

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.savefig(output_path, bbox_inches='tight', pad_inches=0, facecolor='#FFFFFF')
    plt.close()
    print(f"대안(B) 저장: {output_path}")


if __name__ == '__main__':
    output_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(output_dir, 'images'), exist_ok=True)

    create_cover_a(os.path.join(output_dir, 'images', 'cover_a.png'))
    create_cover_b(os.path.join(output_dir, 'images', 'cover_b.png'))
    print("표지 생성 완료!")
