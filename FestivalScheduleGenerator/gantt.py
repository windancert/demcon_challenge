import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Example planning: (show_name, start, end, stage_id)
planning = [
    ("show_3", 29, 36, 1),
    ("show_2", 30, 33, 2),
    ("show_4", 33, 35, 2),
    ("show_1", 36, 39, 1),
    ("show_6", 36, 40, 3),
    ("show_5", 40, 42, 2)
]

def plot_gantt_chart(planning):
    # Prepare plot
    fig, ax = plt.subplots(figsize=(10, 5))

    # Map stage IDs to vertical positions
    stage_ids = sorted(set(stage for _, _, _, stage in planning))
    stage_y = {stage: i for i, stage in enumerate(stage_ids)}

    # Plot each show
    for name, start, end, stage in planning:
        duration = end - start + 1  # Inclusive end time
        ax.barh(stage_y[stage], duration, left=start, height=0.6, edgecolor='black')
        ax.text(start + duration / 2, stage_y[stage], name, va='center', ha='center', color='white', fontsize=8)

    # Format axes
    ax.set_yticks(list(stage_y.values()))
    ax.set_yticklabels([f"Stage {s}" for s in stage_ids])
    ax.set_xlabel("Hour from festival start")
    ax.set_title("Festival Stage Planning - Gantt Chart (Inclusive End Times)")
    ax.grid(True, axis='x', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

