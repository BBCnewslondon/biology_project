import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9.0,
    'axes.titlesize': 11.5,
    'figure.dpi': 300,
})

fig, ax = plt.subplots(figsize=(10.5, 6.8))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')


def draw_box(
    x,
    y,
    w,
    h,
    text,
    bg='#f8f9fa',
    edge='#495057',
    lw=1.3,
    fontsize=8.0,
    text_color='#111111',
    title=None,
):
  box = FancyBboxPatch(
      (x - w / 2, y - h / 2),
      w,
      h,
      boxstyle='round,pad=0.3,rounding_size=1.6',
      facecolor=bg,
      edgecolor=edge,
      linewidth=lw,
      zorder=2,
  )
  ax.add_patch(box)
  if title:
    ax.text(
        x,
        y + h / 2 - 1.3,
        title,
        ha='center',
        va='top',
        fontsize=fontsize + 0.6,
        fontweight='bold',
        color=text_color,
        linespacing=1.2,
        zorder=3,
    )
    ax.text(
        x,
        y - h / 2 + 1.3,
        text,
        ha='center',
        va='bottom',
        fontsize=fontsize,
        color=text_color,
        linespacing=1.28,
        zorder=3,
    )
  else:
    ax.text(
        x,
        y,
        text,
        ha='center',
        va='center',
        fontsize=fontsize,
        color=text_color,
        linespacing=1.28,
        zorder=3,
    )


def draw_arrow(
    p1,
    p2,
    label='',
    rad=0.0,
    color='#333333',
    lw=1.4,
    lx=None,
    ly=None,
    lcolor='#222222',
    style='->',
):
  arrow = FancyArrowPatch(
      p1,
      p2,
      connectionstyle=f'arc3,rad={rad}',
      arrowstyle=f'{style},head_length=5.5,head_width=3.8',
      color=color,
      linewidth=lw,
      zorder=4,
  )
  ax.add_patch(arrow)
  if label:
    mx = lx if lx is not None else (p1[0] + p2[0]) / 2
    my = ly if ly is not None else (p1[1] + p2[1]) / 2
    ax.text(
        mx,
        my,
        label,
        ha='center',
        va='center',
        fontsize=7.6,
        color=lcolor,
        bbox=dict(
            boxstyle='round,pad=0.22',
            facecolor='white',
            edgecolor='none',
            alpha=0.92,
        ),
        zorder=5,
    )


# GC Container
gc_container = FancyBboxPatch(
    (3.5, 22.5),
    62,
    41.5,
    boxstyle='round,pad=0.4,rounding_size=2.2',
    facecolor='#f3eef8',
    edgecolor='#7542a8',
    linestyle='--',
    linewidth=1.4,
    zorder=1,
)
ax.add_patch(gc_container)
ax.text(
    63.5,
    61.8,
    'GERMINAL CENTER (GC) REACTION',
    fontsize=8.8,
    fontweight='bold',
    color='#54278f',
    ha='right',
    va='center',
    zorder=2,
)

# Nodes
draw_box(
    32,
    92,
    56,
    11,
    title='1. Subcapsular Sinus: Antigen Entry',
    text=(
        r'Soluble proteins (<70 kDa) diffuse via follicular conduits' + '\n' +
        r'VLPs & mRNA-LNPs captured by $\mathrm{CD169}^+$ Macrophages'
        r' $\rightarrow$ FDCs'
    ),
    bg='#eef4fa',
    edge='#1f77b4',
    fontsize=7.8,
)

draw_box(
    32,
    73.5,
    56,
    11.5,
    title=r'2. Naive B Cell Activation & T–B Border Migration',
    text=(
        r'BCR crosslinking $\rightarrow$ $\mathrm{Ig}\alpha/\mathrm{Ig}\beta$'
        r' ITAM phosphorylation (Lyn/Syk/BTK)' + '\n' +
        r'MHC-II peptide loading + $CCR7$/$EBI2$ upregulation ($CD40L$,'
        r' IL-4/IL-21)'
    ),
    bg='#ffffff',
    edge='#495057',
    fontsize=7.8,
)

draw_box(
    84,
    73.5,
    29,
    11.5,
    title='Extrafollicular Plasmablasts',
    text=(
        r'TI-2 or High-Avidity BCR stimulation' + '\n' +
        r'Rapid, low-affinity IgM/IgG wave' + '\n' +
        r'Short-lived (Lifespan $\approx$ 2–5 d; No memory)'
    ),
    bg='#fff5f5',
    edge='#d62728',
    text_color='#8c1515',
    fontsize=7.6,
)

draw_box(
    19,
    44,
    26,
    22,
    title=r'Dark Zone (DZ)' + '\n' + r'[CXCR4$^{hi}$ CD83$^{lo}$]',
    text=(
        r'• Rapid Clonal Proliferation' + '\n' +
        r'• AID-Driven Somatic' + '\n' +
        r'  Hypermutation (SHM)' + '\n' +
        r'  of $V(D)J$ Variable Genes'
    ),
    bg='#e5d8f0',
    edge='#54278f',
    text_color='#2a114b',
    fontsize=7.7,
)

draw_box(
    49.5,
    41,
    28,
    24,
    title=r'Light Zone (LZ)' + '\n' + r'[CXCR4$^{lo}$ CD83$^{hi}$ CD86$^{hi}$]',
    text=(
        r'• Competitive Antigen Extraction' + '\n' +
        r'  from FDC networks (CR1/CR2)' + '\n' +
        r'• Cognate $T_{FH}$ Selection' + '\n' +
        r'  ($CD40L$, ICOS, IL-21)' + '\n' +
        r'• Selection of Class-Switched' + '\n' +
        r'  Variants (IgG1/IgG3)'
    ),
    bg='#ffffff',
    edge='#7542a8',
    text_color='#2a114b',
    fontsize=7.6,
)

draw_box(
    22.5,
    8.5,
    38,
    13,
    title=r'4A. Quiescent Memory B Cells (MBCs)',
    text=(
        r'Lower-affinity / Early LZ exit ($BCL6^{lo}$)' + '\n' +
        r'• $\mathrm{CD80}^+\mathrm{PD}\text{-}\mathrm{L2}^+$ $\rightarrow$ Recall'
        r' Plasmablasts' + '\n' +
        r'• $\mathrm{CD80}^-\mathrm{PD}\text{-}\mathrm{L2}^-$ $\mathrm{IgM}^+$'
        r' $\rightarrow$ Secondary GC Entry'
    ),
    bg='#eef8f3',
    edge='#2b8a3e',
    text_color='#184f24',
    fontsize=7.6,
)

draw_box(
    68.5,
    8.5,
    43,
    13,
    title=r'4B. Bone Marrow LLPCs ($\mathrm{CD19}^-\mathrm{CD38}^{hi}\mathrm{CD138}^+$)',
    text=(
        r'High-affinity LZ exit: $BLIMP\text{-}1^+$ $IRF4^+$ $XBP1^+$' + '\n' +
        r'$CXCR4$-guided homing to $CXCL12^+$ BM stromal niche' + '\n' +
        r'Sustained by APRIL/BAFF (BCMA) & IL-6 ($t_{1/2} > 10\text{--}50\text{'
        r' yr}$)'
    ),
    bg='#eef4fa',
    edge='#1f77b4',
    text_color='#0d3c61',
    fontsize=7.6,
)

# Arrows
draw_arrow((32, 86.5), (32, 79.3))
draw_arrow(
    (60, 73.5),
    (69.5, 73.5),
    label=r'BLIMP-1' + '\n' + r'upregulation',
    color='#d62728',
    lcolor='#a81c1d',
    lx=64.7,
    ly=78.0,
)
draw_arrow(
    (22, 67.7),
    (19, 55),
    label=r'BCL6 upregulation' + '\n' + r'(GC Entry)',
    color='#54278f',
    lcolor='#54278f',
    lx=14.5,
    ly=61.5,
)
draw_arrow(
    (32, 49),
    (46, 53),
    label=r'CXCL13 gradient' + '\n' + r'(CXCR4 downregulation)',
    rad=-0.25,
    color='#54278f',
    lcolor='#54278f',
    lx=39,
    ly=56.5,
)
draw_arrow(
    (35.5, 34),
    (21, 33),
    label=r'c-Myc & mTORC1' + '\n' + r'Cyclic Re-entry',
    rad=-0.25,
    color='#54278f',
    lcolor='#54278f',
    lx=28.5,
    ly=27.5,
)
draw_arrow(
    (41, 29),
    (26, 15),
    label=r'Weaker $T_{FH}$ signal' + '\n' + r'(Broad repertoire)',
    color='#2b8a3e',
    lcolor='#184f24',
    lx=27,
    ly=19.5,
)
draw_arrow(
    (55, 29),
    (65, 15),
    label=r'Intense BCR + CD40L' + '\n' + r'(BLIMP-1 / IRF4 switch)',
    color='#1f77b4',
    lcolor='#0d3c61',
    lx=66,
    ly=19.5,
)
draw_arrow(
    (41.5, 11),
    (86, 67.7),
    label=r'Variant / Booster Recall' + '\n' + r'(Secondary Plasmablasts)',
    rad=0.42,
    color='#2b8a3e',
    lcolor='#184f24',
    lx=82.5,
    ly=38,
)

plt.title(
    'A: Spatio-Temporal Regulation of Vaccine-Induced B Cell Differentiation',
    loc='left',
    fontweight='bold',
    y=0.98,
)
plt.tight_layout()
plt.savefig('figure1a_schematic.pdf', format='pdf', bbox_inches='tight')
plt.savefig('figure1a_schematic.png', format='png', dpi=300, bbox_inches='tight')