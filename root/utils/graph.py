import matplotlib.pyplot as plt
import numpy as np

def graph(algorithms, path_lengths, execution_times_sec, subtitle):
    execution_times_ms = [t * 1000 for t in execution_times_sec]
    x = np.arange(len(algorithms))
    
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    bars1 = ax1.bar(x, path_lengths, color='skyblue')
    ax1.set_xlabel('Algorithms')
    ax1.set_ylabel('Path Length')
    ax1.set_title(f'Path Lengths - {subtitle}')
    ax1.set_xticks(x)
    ax1.set_xticklabels(algorithms)
    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2.0, yval + 0.5, f'{yval}', ha='center', va='bottom', fontsize=8)
    
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    bars2 = ax2.bar(x, execution_times_ms, color='salmon')
    ax2.set_xlabel('Algorithms')
    ax2.set_ylabel('Execution Time (ms)')
    ax2.set_title(f'Execution Times - {subtitle}')
    ax2.set_xticks(x)
    ax2.set_xticklabels(algorithms)
    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2.0, yval + 0.5, f'{yval:.1f}', ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    plt.show()