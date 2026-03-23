import matplotlib.pyplot as plt


class Graph:
    """
    A wrapper for matplotlib to reduce verbosity
    """

    def __init__(
        self, title=None, xlabel=None, ylabel=None, y2label=None, width=15, height=5, extra_y=False, overried_ymin=0
    ):
        plt.rcParams.update({'lines.linewidth': 1})
        self.fig, self.ax1 = plt.subplots()
        self.overried_ymin = overried_ymin

        if title is not None:
            plt.title(title)

        if extra_y:
            self.ax2 = self.ax1.twinx()
        else:
            self.ax2 = None

        self.fig.set_figwidth(width)
        self.fig.set_figheight(height)

        if xlabel is not None:
            self.ax1.set_xlabel(xlabel)
        if ylabel is not None:
            self.ax1.set_ylabel(ylabel)
        if y2label is not None:
            self.ax2.set_ylabel(y2label)

    def __enter__(self):
        if self.ax2 is not None:
            return self.fig, self.ax1, self.ax2
        else:
            return self.fig, self.ax1

    def __exit__(self, exc_type, exc_val, traceback):
        if self.overried_ymin is not False:
            for ax in self.fig.axes:
                ax.set_ylim([0, None])
        for ax in self.fig.axes:
            if not ax.get_legend_handles_labels() == ([], []):
                ax.legend(loc='best')
        self.fig.tight_layout()
