import numpy as np
import matplotlib.pyplot as plt

# Parameters
omega = 1.0  # Angular frequency
t = np.linspace(0, 4*np.pi/omega, 1000)  # Time array covering 2 full cycles

# Calculate the three quantities
velocity = np.cos(omega * t)  # v = cos(ωt)
acceleration = -np.sin(omega * t)  # a = -sin(ωt)
angular_velocity = -(1/4) * np.sin(2 * omega * t)  # Ω = -(1/4)sin(2ωt)

# Create the plot
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))

# Plot velocity
ax1.plot(t, velocity, 'b-', linewidth=2, label=r'$v = \cos(\omega t)$')
ax1.set_ylabel('Velocity', fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=11)
ax1.set_title('Internal Motion Components in 0-Sphere Model', fontsize=14, fontweight='bold')

# Plot acceleration
ax2.plot(t, acceleration, 'r-', linewidth=2, label=r'$a = -\sin(\omega t)$')
ax2.set_ylabel('Acceleration', fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.legend(fontsize=11)

# Plot angular velocity
ax3.plot(t, angular_velocity, 'g-', linewidth=2, label=r'$\Omega = -\frac{1}{4}\sin(2\omega t)$')
ax3.set_ylabel('Angular Velocity', fontsize=12)
ax3.set_xlabel(r'Time ($\omega t$)', fontsize=12)
ax3.grid(True, alpha=0.3)
ax3.legend(fontsize=11)

# Add vertical lines to show period relationships
for i in range(5):
    # Period markers for v and a (period = 2π/ω)
    if i < 3:
        ax1.axvline(x=i*2*np.pi/omega, color='blue', linestyle='--', alpha=0.5)
        ax2.axvline(x=i*2*np.pi/omega, color='red', linestyle='--', alpha=0.5)
    
    # Period markers for Ω (period = π/ω, twice as frequent)
    ax3.axvline(x=i*np.pi/omega, color='green', linestyle='--', alpha=0.5)

# Set x-axis ticks in terms of π
pi_ticks = np.array([0, np.pi/omega, 2*np.pi/omega, 3*np.pi/omega, 4*np.pi/omega])
pi_labels = [r'$0$', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$']

for ax in [ax1, ax2, ax3]:
    ax.set_xlim(0, 4*np.pi/omega)
    ax.set_xticks(pi_ticks)
    ax.set_xticklabels(pi_labels)

# Add annotations
ax1.annotate('Period: $2\pi$', xy=(2*np.pi/omega, 0.8), fontsize=10, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7))
ax2.annotate('Period: $2\pi$', xy=(2*np.pi/omega, -0.8), fontsize=10,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightcoral", alpha=0.7))
ax3.annotate('Period: $\pi$ (Double frequency)', xy=(np.pi/omega, -0.2), fontsize=10,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.7))

plt.tight_layout()
plt.savefig('spin_oscillation_components.pdf', dpi=300, bbox_inches='tight')
plt.savefig('spin_oscillation_components.png', dpi=300, bbox_inches='tight')
plt.show()

print("Figure saved as 'spin_oscillation_components.pdf' and 'spin_oscillation_components.png'")
print("\nKey observations:")
print("1. Velocity and acceleration have period 2π")
print("2. Angular velocity has period π (double frequency)")
print("3. This demonstrates the 2ωt dependence in the cross product a×v")
print("4. The double frequency corresponds to the 720° periodicity of spin-1/2 particles")