# Monte Carlo simulation of 20,000 electrons in a double-slit geometry.

import numpy as np
import matplotlib.pyplot as plt

# Parameter settings
N_ELECTRONS = 20000       # Number of electrons
SLIT_DISTANCE = 0.5       # Distance between slits
SLIT_WIDTH = 0.1          # Slit width
SCREEN_DISTANCE = 5.0     # Distance to screen
WAVELENGTH = 0.1          # Electron wavelength (de Broglie wavelength)

def sample_single_electron_visibility():
    """
    Calculate visibility V_i from internal phase θ of each electron.
    
    V(θ) = 2cos²θ sin²θ / (cos⁴θ + sin⁴θ)
    
    Returns:
    --------
    V_i : float
        Visibility of the electron (0-1)
    """
    # Sample θ uniformly from [0, 2π)
    theta = np.random.uniform(0, 2*np.pi)
    c2 = np.cos(theta)**2
    s2 = np.sin(theta)**2
    numerator = 2 * c2 * s2
    denominator = c2**2 + s2**2  # cos⁴ + sin⁴
    
    # Safety check: denominator should never be zero theoretically
    if denominator == 0:
        return 0.0
    return numerator / denominator

def calculate_interference_pattern(x, y, visibility):
    """
    Calculate probability density of interference pattern.
    
    Parameters:
    -----------
    x, y : float or ndarray
        Coordinates on the screen
    visibility : float
        Visibility of the electron (0-1)
    
    Returns:
    --------
    intensity : float or ndarray
        Probability density at (x, y)
    """
    # Positions of two slits
    slit1_y = SLIT_DISTANCE / 2
    slit2_y = -SLIT_DISTANCE / 2
    
    # Distance from each slit
    r1 = np.sqrt((y - slit1_y)**2 + SCREEN_DISTANCE**2)
    r2 = np.sqrt((y - slit2_y)**2 + SCREEN_DISTANCE**2)
    
    # Phase difference
    phase_diff = 2 * np.pi * (r1 - r2) / WAVELENGTH
    
    # Probability density with interference term
    intensity = 1 + visibility * np.cos(phase_diff)
    
    # Envelope function (decay with distance from slits)
    envelope = np.exp(-0.5 * (x**2) / 2.0)
    
    return intensity * envelope

def simulate_double_slit_per_electron(N_ELECTRONS=20000, seed=42):
    """
    Simulate double-slit experiment using different visibility V_i for each electron.
    
    Parameters:
    -----------
    N_ELECTRONS : int
        Number of electrons (default: 20000)
    seed : int
        Random seed for reproducibility (default: 42)
    
    Returns:
    --------
    x_detected : ndarray
        x-coordinates of detected electrons
    y_detected : ndarray
        y-coordinates of detected electrons
    visibilities : ndarray
        List of visibility values for each electron
    """
    np.random.seed(seed)
    x_grid = np.linspace(-2, 2, 200)
    y_grid = np.linspace(-2, 2, 400)
    X, Y = np.meshgrid(x_grid, y_grid)

    x_detected = []
    y_detected = []
    visibilities = []

    for i in range(N_ELECTRONS):
        # Calculate visibility from internal phase of each electron
        V_i = sample_single_electron_visibility()
        visibilities.append(V_i)
        
        # Probability density for this electron (on grid)
        prob_density = calculate_interference_pattern(X, Y, V_i)
        prob_density = prob_density / prob_density.sum()
        flat_prob = prob_density.flatten()
        
        # Sample according to probability distribution
        idx = np.random.choice(len(flat_prob), p=flat_prob)
        y_idx = idx // len(x_grid)
        x_idx = idx % len(x_grid)
        
        x_detected.append(x_grid[x_idx])
        y_detected.append(y_grid[y_idx])

    return np.array(x_detected), np.array(y_detected), np.array(visibilities)

# Execute simulation
print("Starting simulation...")
x_pos, y_pos, V_list = simulate_double_slit_per_electron(N_ELECTRONS)

# Calculate average visibility
mean_V = np.mean(V_list)
theoretical_V = np.sqrt(2) - 1  # Theoretical value = 0.4142

print(f"\n=== Results ===")
print(f"Number of electrons: {N_ELECTRONS}")
print(f"Observed average visibility <V>: {mean_V:.4f}")
print(f"Theoretical average visibility: {theoretical_V:.4f}")
print(f"Error: {abs(mean_V - theoretical_V):.4f}")

# Create plots (font sizes doubled for publication)
fig = plt.figure(figsize=(18, 8), facecolor='black')

# Main simulation results
ax1 = plt.subplot(1, 2, 1)
ax1.set_facecolor('black')
ax1.scatter(y_pos, x_pos, c='white', s=5, alpha=0.5, edgecolors='none')
ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 2)
ax1.set_aspect('equal')
ax1.set_title(f'Double-Slit Simulation\n<V> = {mean_V:.4f}', 
              color='white', fontsize=28, pad=20)
ax1.set_xticks([])
ax1.set_yticks([])
for spine in ax1.spines.values():
    spine.set_edgecolor('white')
    spine.set_linewidth(1.5)

# Histogram of visibility distribution
ax2 = plt.subplot(1, 2, 2)
ax2.set_facecolor('black')
ax2.hist(V_list, bins=50, color='cyan', alpha=0.7, edgecolor='white')
ax2.axvline(mean_V, color='red', linestyle='--', linewidth=2, 
            label=f'Observed <V> = {mean_V:.4f}')
ax2.axvline(theoretical_V, color='yellow', linestyle='--', linewidth=2, 
            label=f'Theory <V> = {theoretical_V:.4f}')
ax2.set_xlabel('Visibility V', color='white', fontsize=24)
ax2.set_ylabel('Count', color='white', fontsize=24)
ax2.set_title('Distribution of Single-Electron Visibility', 
              color='white', fontsize=28, pad=20)
ax2.tick_params(colors='white', labelsize=20)
ax2.legend(facecolor='black', edgecolor='white', labelcolor='white', 
           fontsize=20)
for spine in ax2.spines.values():
    spine.set_edgecolor('white')
    spine.set_linewidth(1.5)

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/double_slit_physics.png', 
            dpi=150, facecolor='black', edgecolor='none', bbox_inches='tight')
print("\nImage saved: double_slit_physics.png")

# Test visibility sampling
print("\n=== Visibility Sampling Test ===")
test_samples = [sample_single_electron_visibility() for _ in range(100000)]
print(f"Average of 100000 samples: {np.mean(test_samples):.4f}")
print(f"Error from theoretical value: {abs(np.mean(test_samples) - theoretical_V):.4f}")