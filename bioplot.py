import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'axes.labelsize': 10.5,
    'axes.titlesize': 11,
    'legend.fontsize': 8.5,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.dpi': 300,
})

t = np.linspace(0, 365, 1000)


def ab_kinetics(
    t, a_pb, a_llpc, t_half_pb=28.0, t_half_llpc=3650.0, t_peak=14.0
):
  rise = 1 - np.exp(-t / (t_peak / 2.5))
  decay_pb = a_pb * np.exp(-np.log(2) * np.maximum(0, t - t_peak) / t_half_pb)
  decay_llpc = a_llpc * np.exp(
      -np.log(2) * np.maximum(0, t - t_peak) / t_half_llpc
  )
  return rise * (decay_pb + decay_llpc)


# 1. Live-Attenuated / Tetanus-like
titer_durable = 1.0 + ab_kinetics(
    t, a_pb=2.3, a_llpc=1.8, t_half_pb=25, t_half_llpc=18000
)

# 2. Subunit / mRNA-LNP
titer_mrna = 1.0 + ab_kinetics(
    t, a_pb=2.9, a_llpc=0.25, t_half_pb=28, t_half_llpc=200
)
t_boost = 180.0
boost_mask = t >= t_boost
t_post = t[boost_mask] - t_boost

# Elevated secondary peak reflecting robust anamnestic surge
recall_spike = (1 - np.exp(-t_post / 2.0)) * (
    3.3 * np.exp(-np.log(2) * np.maximum(0, t_post - 7) / 32)
    + 0.55 * np.exp(-np.log(2) * np.maximum(0, t_post - 7) / 250)
)
titer_mrna[boost_mask] += recall_spike

# 3. Germinal Center SHM Breadth (%)
shm_breadth = 72 * (1 - np.exp(-np.maximum(0, t - 7) / 55))
shm_breadth[boost_mask] += 18 * (1 - np.exp(-t_post / 20))

# --- Plotting ---
fig, ax1 = plt.subplots(figsize=(8.8, 4.8))
ax2 = ax1.twinx()

ax2.fill_between(
    t,
    0,
    shm_breadth,
    color='#9467bd',
    alpha=0.12,
    label='GC Somatic Hypermutation (SHM) Breadth',
)
ax2.plot(
    t, shm_breadth, color='#7542a8', linestyle=':', linewidth=1.5, alpha=0.8
)

ax1.plot(
    t,
    titer_durable,
    color='#1f77b4',
    linewidth=2.2,
    label=(
        r'Live-Attenuated / Toxoid (Durable BM $\mathrm{CD19}^-\mathrm{CD138}^+$'
        r' LLPCs)'
    ),
)
ax1.plot(
    t,
    titer_mrna,
    color='#d62728',
    linewidth=2.2,
    linestyle='--',
    label=r'mRNA-LNP / Subunit (Deficient BM LLPCs + MBC Booster Recall)',
)

ax1.axhline(2.15, color='#444444', linestyle='-.', linewidth=1.0, alpha=0.75)
ax1.text(
    360,
    2.22,
    'Sterilizing Neutralization Threshold',
    color='#222222',
    fontsize=8,
    ha='right',
    style='italic',
    bbox=dict(
        boxstyle='round,pad=0.15',
        facecolor='white',
        edgecolor='none',
        alpha=0.8,
    ),
)
ax1.axvline(t_boost, color='#555555', linestyle='--', linewidth=1.0, alpha=0.5)
ax1.text(
    t_boost - 4,
    4.75,
    'Booster Dose\n(Month 6)',
    color='#333333',
    fontsize=8,
    ha='right',
    va='top',
    style='italic',
)

label_box = dict(
    boxstyle='round,pad=0.25', facecolor='white', edgecolor='none', alpha=0.85
)

# Callouts
ax1.annotate(
    'Extrafollicular\nPlasmablast Peak\n(Low Affinity)',
    xy=(15, 4.10),
    xytext=(32, 4.45),
    arrowprops=dict(
        arrowstyle='->',
        color='#222222',
        lw=1.0,
        connectionstyle='arc3,rad=-0.15',
    ),
    fontsize=8,
    fontweight='bold',
    bbox=label_box,
)

ax1.annotate(
    r'BM LLPC Plateau'
    + '\n'
    + r'(BLIMP-1$^+$ CXCR4$^+$; APRIL/BAFF niche)',
    xy=(95, 2.92),
    xytext=(55, 3.65),
    arrowprops=dict(
        arrowstyle='->',
        color='#1f77b4',
        lw=1.0,
        connectionstyle='arc3,rad=0.15',
    ),
    fontsize=8,
    color='#1f77b4',
    bbox=label_box,
)

ax1.annotate(
    r'Plasmablast Decay'
    + '\n'
    + r'(Lack of BM $\mathrm{CD19}^-\mathrm{CD138}^+$ LLPCs)',
    xy=(135, 1.38),
    xytext=(42, 1.05),
    arrowprops=dict(
        arrowstyle='->',
        color='#d62728',
        lw=1.0,
        connectionstyle='arc3,rad=0.15',
    ),
    fontsize=8,
    color='#a81c1d',
    bbox=label_box,
)

# Raw string prevents \t from turning into a tab character
ax1.annotate(
    r'Secondary MBC Recall'
    + '\n'
    + r'($\mathrm{CD80}^+\mathrm{PD}\text{-}\mathrm{L2}^+$ Plasmablasts'
    + '\n'
    + r'+ Secondary GC Entry)',
    xy=(188, 4.2),
    xytext=(212, 4.5),
    arrowprops=dict(
        arrowstyle='->',
        color='#d62728',
        lw=1.0,
        connectionstyle='arc3,rad=-0.15',
    ),
    fontsize=8,
    color='#a81c1d',
    bbox=label_box,
)

ax2.annotate(
    'Persistent Human GC (>6 mo)\nAID-Driven Affinity Maturation',
    xy=(285, 87),
    xytext=(235, 22),
    arrowprops=dict(
        arrowstyle='->',
        color='#54278f',
        lw=1.0,
        connectionstyle='arc3,rad=-0.15',
    ),
    fontsize=8,
    color='#54278f',
    bbox=label_box,
)

ax1.set_xlabel('Time Post-Primary Immunization')
ax1.set_ylabel(
    r'Serum Antibody Titer ($\log_{10}$ Arbitrary Units)', color='#111111'
)
ax2.set_ylabel('Relative Epitope Breadth / SHM Depth (%)', color='#54278f')
ax2.tick_params(axis='y', labelcolor='#54278f')
ax1.set_xlim(0, 365)
ax1.set_ylim(0.75, 5.2)
ax2.set_ylim(0, 115)
ax1.set_xticks([0, 28, 90, 180, 270, 365])
ax1.set_xticklabels([
    'Day 0\n(Prime)',
    'Day 28',
    'Month 3',
    'Month 6\n(Boost)',
    'Month 9',
    'Month 12',
])

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(
    lines1 + lines2,
    labels1 + labels2,
    loc='lower left',
    bbox_to_anchor=(0.0, 1.02),
    ncol=1,
    frameon=True,
    facecolor='#fafafa',
    edgecolor='#dddddd',
)
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
plt.title(
    'B: Vaccine Platform-Dependent Humoral Kinetics and Germinal Center'
    ' Breadth',
    loc='left',
    fontweight='bold',
    y=1.24,
)
plt.tight_layout()
plt.savefig('figure1b_kinetics.pdf', format='pdf', bbox_inches='tight')
plt.savefig('figure1b_kinetics.png', format='png', dpi=300, bbox_inches='tight')