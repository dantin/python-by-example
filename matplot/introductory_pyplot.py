# version 1.0 2018-08-01
# URL: https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import NullFormatter  # useful for `logit` scale


def default_plot():
    # x-axis ranges from [0, len(args)]
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.show()


def plot_xy():
    # plt x versus y
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.ylabel('y axis')
    plt.show()


def style_plot():
    # like MATLAB, color is RED('r'), using DOT('o')
    # default is 'b-', solid blue line
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    # x-axis from [0, 6], y-axis from [0, 20]
    # [xmin, xmax, ymin, ymax]
    plt.axis([0, 6, 0, 20])
    plt.show()


def multi_plot():
    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

    # red dashes, blue squares and green triangles
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.show()


def data_plot():
    # provides an object with 'data' keyword argument, and generate plot with strings corresponding to these variable
    data = {
        'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50),
    }
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100

    plt.scatter('a', 'b', c='c', s='d', data=data)
    plt.xlabel('entry a')
    plt.ylabel('entry b')
    plt.show()


def cat_plot():
    names = ['group_a', 'group_b', 'group_c']
    values = [1, 10, 100]

    plt.figure(1, figsize=(9, 3))

    # 'subplot()' command specifies `numrows`, `numcols`, `plot_number`
    plt.subplot(131)
    plt.bar(names, values)
    plt.subplot(132)
    plt.scatter(names, values)
    plt.subplot(133)
    plt.plot(names, values)
    plt.suptitle('Categorical Plotting')
    plt.show()


def line_properties():
    # # Use keyword args
    # plt.plot(x, y, linewidth=2.0)

    # # Use setter methods of 'Line2D' instance
    # # line1, line2 = plot(x1, y1, x2, y2)
    # line, = plot.plot(x, y, '-')
    # line.set_antialiased(False) # turn off antialising

    # # Use 'setp()' command
    # lines = plt.plot(x1, y1, x2, y2)
    # # use keyword args
    # plt.setp(lines, color='r', linewidth=2.0)
    # # or MATLAB style string value pairs
    # plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
    pass


def multi_fig_and_axes():
    def f(t):
        return np.exp(-t) * np.cos(2*np.pi*t)

    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
    plt.subplot(212)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
    plt.show()


def multi_fig():
    plt.figure(1)       # the first figure
    plt.subplot(211)    # the first subplot in the first figure
    plt.plot([1, 2, 3])
    plt.subplot(212)    # the second subplot in the first figure
    plt.plot([4, 5, 6])

    plt.figure(2)       # a second figure
    plt.plot([4, 5, 6]) # create a subplot(111) by default

    plt.figure(1)       # figure 1 current; subplot(212) still current
    plt.subplot(211)    # make subplot(211) in figure one current
    plt.title('Easy as 1, 2, 3') # subplot 211 title
    plt.show()


def text_demo():
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    # the histogram of the data
    n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)

    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    # support TeX expression
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()


def annotating_text():
    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line, = plt.plot(t, s, lw=2)

    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 )
    plt.ylim(-2, 2)
    plt.show()


def axes_scale_demo():
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # make up some data in the interval ]0, 1[
    y = np.random.normal(loc=0.5, scale=0.4, size=1000)
    y = y[(y >0) & (y < 1)]
    y.sort()
    x = np.arange(len(y))

    # plot with various axes scales
    plt.figure(1)

    # linear
    plt.subplot(221)
    plt.plot(x, y)
    plt.yscale('linear')
    plt.title('linear')
    plt.grid(True)

    # log
    plt.subplot(222)
    plt.plot(x, y)
    plt.yscale('log')
    plt.title('log')
    plt.grid(True)

    # symmetric log
    plt.subplot(223)
    plt.plot(x, y - y.mean())
    plt.yscale('symlog', linthreshy=0.01)
    plt.title('symlog')
    plt.grid(True)

    # logit
    plt.subplot(224)
    plt.plot(x, y)
    plt.yscale('logit')
    plt.title('logit')
    plt.grid(True)

    # Format the minor tick labels of the y-axis into empty strings with
    # `NullFormatter`, to avoid cumbering the axis with too many labels.
    plt.gca().yaxis.set_minor_formatter(NullFormatter())
    # Adjust the subplot layout, because the logit one may take more space
    # than usual, due to y-tick labels like "1 - 10^{-3}"
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                        wspace=0.35)
    plt.show()


if __name__ == '__main__':
    # default_plot()
    # plot_xy()
    # style_plot()
    # multi_plot()
    # keyword_str_plot()
    # cat_plot()
    # multi_fig_and_axes()
    # multi_fig()
    # text_demo()
    # annotating_text()
    axes_scale_demo()
