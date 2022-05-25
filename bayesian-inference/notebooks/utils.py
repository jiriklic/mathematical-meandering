import random
import scipy
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets


def print_sample(sample, view_size=9):
    print(sample[:view_size])
    print("Size:\t{}".format(len(sample)))
    print("Min:\t{}".format(min(sample)))
    print("Max:\t{}".format(max(sample)))
    print("Mean:\t{:.2f}".format(sum(sample) / len(sample)))
    print("Sum:\t{}".format(sum(sample)))


def plot_norm(mean=0, std=1, ymax=1):
    x_min = -20.0
    x_max = 20.0
    x = np.linspace(x_min, x_max, 1000)
    y = stats.norm.pdf(x,loc=mean, scale=std)
    
    fig = plt.figure(figsize=(12, 3), dpi=100);
    plt.xlabel("$x$")
    plt.ylabel("$pdf$")
    plt.title("$X \sim N(\mu, \sigma)$")
    plt.ylim(ymax = ymax, ymin = 0.0)
    plt.plot(x, y);


def interact_norm():
    mu = widgets.FloatSlider(
        value=0,
        min=-15,
        max=15.0,
        step=0.1,
        description="$\mu$",
        disabled=False,
        # continuous_update=False,
        orientation="horizontal",
        readout=True,
        readout_format=".1f",
    )

    sigma = widgets.FloatSlider(
        value=1.0,
        min=0.1,
        max=3.1,
        step=0.1,
        description="$\sigma$",
        disabled=False,
        # continuous_update=False,
        orientation="horizontal",
        readout=True,
        readout_format=".1f",
    )

    ymax = widgets.FloatSlider(
        value=1.0,
        min=1.0,
        max=5.0,
        step=0.1,
        description="$y_{max}$",
        disabled=False,
        # continuous_update=False,
        orientation="horizontal",
        readout=True,
        readout_format=".1f",
    )

    widgets.interact(plot_norm, mean=mu, std=sigma, ymax=ymax);


def plot_beta(a=100.0, b=100.0, ymax=15.0):
    x = np.linspace(0.0, 1.0, 1000)
    y = stats.beta.pdf(x,a=a, b=b)
    
    fig = plt.figure(figsize=(12, 3), dpi=100);
    plt.xlabel("$x$")
    plt.ylabel("$pdf$")
    plt.title("$X \sim Beta(a, b)$")
    plt.ylim(ymax = ymax, ymin = 0.0)
    plt.plot(x, y);


def interact_beta():
    a = widgets.FloatSlider(
        value=200.0,
        min=0.2,
        max=200.0,
        step=0.1,
        description="$a$",
        disabled=False,
        # continuous_update=False,
        orientation="horizontal",
        readout=True,
        readout_format=".1f",
    )

    b = widgets.FloatSlider(
        value=200.0,
        min=0.2,
        max=200.0,
        step=0.1,
        description="$b$",
        disabled=False,
        # continuous_update=False,
        orientation="horizontal",
        readout=True,
        readout_format=".1f",
    )

    ymax = widgets.FloatSlider(
        value=150.0,
        min=1.0,
        max=150.0,
        step=0.1,
        description="$y_{max}$",
        disabled=False,
        # continuous_update=False,
        orientation="horizontal",
        readout=True,
        readout_format=".1f",
    )

    widgets.interact(plot_beta, a=a, b=b, ymax=ymax);


def plot_gamma(a=2.0, b=2.0, ymax=1.0, loc=0.0):
    
    x = np.linspace(0.0, 100.0, 1000)
    y = stats.gamma.pdf(x, a, loc=loc, scale=1/b)
    
    fig = plt.figure(figsize=(12, 3), dpi=100);
    plt.xlabel("$x$")
    plt.ylabel("$pdf$")
    plt.title("$X \sim \Gamma (a, b)$")
    plt.ylim(ymax = ymax, ymin = 0.0)
    plt.plot(x, y);


def interact_gamma():
    a = widgets.FloatSlider(
        value=0.1,
        min=0.1,
        max=200.0,
        step=0.1,
        description="$a$",
        disabled=False,
        # continuous_update=False,
        orientation="horizontal",
        readout=True,
        readout_format=".1f",
    )

    loc = widgets.FloatSlider(
        value=0.0,
        min=0.0,
        max=80.0,
        step=0.1,
        description="loc",
        disabled=False,
        # continuous_update=False,
        orientation="horizontal",
        readout=True,
        readout_format=".1f",
    )

    b = widgets.FloatSlider(
        value=0.1,
        min=0.1,
        max=200.0,
        step=0.1,
        description="$b$",
        disabled=False,
        # continuous_update=False,
        orientation="horizontal",
        readout=True,
        readout_format=".1f",
    )
        
    ymax = widgets.FloatSlider(
        value=1.0,
        min=1.0,
        max=25.0,
        step=0.1,
        description="$y_{max}$",
        disabled=False,
        # continuous_update=False,
        orientation="horizontal",
        readout=True,
        readout_format=".1f",
    )

    widgets.interact(plot_gamma, a=a, b=b, ymax=ymax, loc=loc);
