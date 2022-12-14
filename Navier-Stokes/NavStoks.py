import numpy as np

def navier_stokes(u, v, p, dx, dy, dt, viscosity):

    un = np.zeros_like(u)

    vn = np.zeros_like(v)

    

    # calcul des termes de diffusion

    u_diff = (viscosity * dt / dx**2) * (np.roll(u, -1, axis=1) - 2 * u + np.roll(u, 1, axis=1))

    v_diff = (viscosity * dt / dy**2) * (np.roll(v, -1, axis=0) - 2 * v + np.roll(v, 1, axis=0))

    

    # calcul des termes de convection

    u_convect = u * (np.roll(u, -1, axis=1) - np.roll(u, 1, axis=1)) + v * (np.roll(u, -1, axis=0) - np.roll(u, 1, axis=0))

    v_convect = u * (np.roll(v, -1, axis=1) - np.roll(v, 1, axis=1)) + v * (np.roll(v, -1, axis=0) - np.roll(v, 1, axis=0))

    

    # calcul de la pression

    p_term = -(dx**2 / dt) * (np.roll(u, -1, axis=1) - np.roll(u, 1, axis=1))

    q_term = -(dy**2 / dt) * (np.roll(v, -1, axis=0) - np.roll(v, 1, axis=0))

    p = (p_term + q_term) / (2 * (dx**2 + dy**2))

    

    # calcul des vitesses pour le prochain pas de temps

    un = u + dt * (-u_convect + u_diff)

    vn = v + dt * (-v_convect + v_diff)

    

    return un, vn, p

