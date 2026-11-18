# Vue 3D : de combien le jardin a-t-il bouge entre deux captures ?
# Usage : python3 -I mesure_glisse.py <avant.png> <apres.png> [points_par_pixel]
# Repere : le coin gauche du terrain (pixel de terre le plus a gauche, entre
# la barre du haut et les boutons du bas). Captures a 1 pixel par point
# (393 x 852) par defaut ; passer 0.5 pour des captures a 2 pixels par point.
# Controle du correctif de la 3D (1.8.4, 18/11) : un glisse de 100 points
# doit deplacer le jardin de 100 points ; le build 115 donnait 150.
import sys
from PIL import Image
import numpy as np

def coin(chemin, k):
    a = np.asarray(Image.open(chemin).convert('RGB')).astype(int)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    terre = (r > 90) & (r < 150) & (g > 50) & (g < 100) & (b > 30) & (b < 80) & (r - b > 40)
    h = a.shape[0]
    terre[: int(h * 0.153)] = False     # barre du haut (Satellite, Plan, 3D)
    terre[int(h * 0.587):] = False      # boutons et carte du bas
    ys, xs = np.nonzero(terre)
    if not len(xs):
        sys.exit('terrain introuvable dans ' + chemin)
    i = xs.argmin()
    return xs[i] * k, ys[i] * k

k = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
(x0, y0), (x1, y1) = coin(sys.argv[1], k), coin(sys.argv[2], k)
print('coin du terrain : (%.0f, %.0f) -> (%.0f, %.0f) ; deplacement (%+.0f, %+.0f) points' % (x0, y0, x1, y1, x1 - x0, y1 - y0))
