import matplotlib.pyplot as plt
import numpy as np
import pytest

import splinart as spl


@pytest.mark.mpl_image_compare
def test_circle_case():  # noqa: ANN201
    """Test de a creation d'un cercle."""
    np.random.random(42)  # noqa: NPY002

    img_size, channels = 1000, 4
    img = np.ones((img_size, img_size, channels), dtype=np.float32)

    theta, path = spl.circle([0.5, 0.5], 0.3)

    def xs_func():  # noqa: ANN202
        nsamples = 500
        return (np.random.random() + 2 * np.pi * np.linspace(0, 1, nsamples)) % (  # noqa: NPY002
            2 * np.pi
        )

    spl.update_img(img, path, xs_func, nrep=4000, x=theta)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(img)
    return fig
