# Author:
#     Loic Gouarin <loic.gouarin@gmail.com>
#
# License: BSD 3 clause
"""Material to update the image with given points and save or plot this image."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from .color import DEFAULT_COLOR


def draw_pixel(
    img: np.ndarray,
    xs: np.ndarray,
    ys: np.ndarray,
    scale_color: float = 0.0005,
    color: tuple = DEFAULT_COLOR,
) -> None:
    """
    Add pixels on the image.

    Parameters
    ----------
    img : np.ndarray
        The image where we add pixels.

    xs : np.ndarray
        The x coordinate of the pixels to add.

    ys : np.ndarray
        The y coordinate of the pixels to add.

    scale_color : float
        Scale the given color (default is 0.0005).

    color : list(4)
        Define the RGBA color of the pixels.

    """
    size = img.shape[0]
    newxs = np.floor(xs * size)
    xs_mask = np.logical_and(newxs >= 0, newxs < size)
    newys = np.floor(ys * size)
    ys_mask = np.logical_and(newys >= 0, newys < size)
    mask = np.logical_and(xs_mask, ys_mask)
    coords = np.asarray([newxs[mask], newys[mask]], dtype="i8")
    img_color = np.asarray(color) * scale_color
    pixels = img[coords[0, :], coords[1, :], :]
    alpha = 1.0 - img_color[3]
    img[coords[0, :], coords[1, :], :] = img_color + pixels * alpha


def save_img(img: np.ndarray, path: str, filename: str) -> None:
    """
    Save the image in a png file.

    Parameters
    ----------
    img : np.ndarray
        The image to save.

    path : str
        The save directory.

    filename : str
        The file name with the png extension.

    """
    plt.imshow(img)
    plt.axis("off")

    path_obj = Path(path)
    if not Path.exists(path_obj):
        Path(path_obj).mkdir(parents=True)

    plt.savefig(path + "/" + filename, dpi=72, bbox_inches="tight", pad_inches=0.1)


def show_img(img: np.ndarray) -> None:
    """
    Plot the image using matplotlib.

    Parameters
    ----------
    img : np.ndarray
        The image to save.

    """
    plt.imshow(img)
    plt.axis("off")
    plt.show()
