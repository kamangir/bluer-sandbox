title:::

> ℹ️ BLE Localization Cost Function with σ

This document defines the mathematical model used to estimate the position of a UGV based on BLE advertisements.  
Each beacon advertises its position $(x_i, y_i, z_i)$ and uncertainty $\sigma_i$ along with its transmitted power.

---

## 1. RSSI–Distance Model

The received signal strength indicator (RSSI) is related to distance by the log-distance path-loss model:

$$
\mathrm{RSSI}_i = P_{\mathrm{tx},i} - 10\, n_i \log_{10}(d_i) + \varepsilon_i
$$

where:

- $P_{\mathrm{tx},i}$ is the transmit power (dBm) of beacon *i*
- $n_i$ is the path-loss exponent (≈ 2 for open space, higher indoors)
- $\varepsilon_i$ is zero-mean Gaussian noise with standard deviation $\sigma_{\mathrm{rssi},i}$

Rearranging gives an estimate of the distance to beacon *i*:

$$
d_i = 10^{(P_{\mathrm{tx},i} - \mathrm{RSSI}_i) / (10\, n_i)}
$$

---

## 2. Measurement Model

Let the UGV’s unknown position be

$$
\mathbf{p} = (x, y, z)
$$

Each beacon *i* has a known position

$$
\mathbf{p}_i = (x_i, y_i, z_i)
$$

The measured distance $d_i$ relates to the true distance by

$$
r_i(\mathbf{p}) = \|\mathbf{p} - \mathbf{p}_i\| - d_i
$$

where $r_i$ is the residual of beacon *i*.

---

## 3. Variance and σ Incorporation

Each measurement has an associated variance $s_i^2$ that combines:

1. Range noise from RSSI  
2. Beacon’s advertised position uncertainty

### 3.1 Range variance (from RSSI noise)

Using first-order error propagation:

$$
\mathrm{Var}(d_i)
  \approx
  \left( \frac{\partial d_i}{\partial \mathrm{RSSI}_i} \right)^2
  \mathrm{Var}(\mathrm{RSSI}_i)
  \;=\;
  \left( \frac{\ln(10)}{10\, n_i} \, d_i \right)^2
  \sigma_{\mathrm{rssi},i}^2
$$

*(All variables are scalar; this is KaTeX-safe.)*

### 3.2 Beacon position variance

If a beacon advertises an isotropic uncertainty $\sigma_i$:

$$
\mathrm{Var}_{\mathrm{beacon},i} \approx \sigma_i^2
$$

### 3.3 Total variance per measurement

$$
s_i^2 = \mathrm{Var}(d_i) + \mathrm{Var}_{\mathrm{beacon},i}
$$

---

## 4. Weighted Least Squares Cost Function

The UGV’s estimated position $\hat{\mathbf{p}}$ minimizes

$$
J(\mathbf{p})
  = \sum_i \frac{r_i(\mathbf{p})^2}{s_i^2}
  = \sum_i
    \frac{
      \left(
        \|\mathbf{p} - \mathbf{p}_i\| - d_i
      \right)^2
    }{s_i^2}
$$

This is equivalent to maximum likelihood estimation under Gaussian noise with heterogeneous variances.

---

## 5. Estimating Global σ

After solving for $\hat{\mathbf{p}}$, compute the overall uncertainty:

$$
\hat{\sigma}
  = \sqrt{
      \frac{1}{N - 3}
      \sum_i r_i(\hat{\mathbf{p}})^2
    }
$$

where $N$ is the number of beacons and 3 is the number of position parameters $(x, y, z)$.

---

## 6. Robust Form (Optional)

To reduce the effect of outliers (for example, multipath), replace the quadratic cost with a robust loss such as Huber or Cauchy:

$$
J(\mathbf{p})
  = \sum_i
    \rho\!\left(
      \frac{r_i(\mathbf{p})}{s_i}
    \right)
$$

where $\rho(\cdot)$ is a smooth function that limits the influence of large residuals.

---

## 7. Summary

| Symbol | Meaning |
|---------|----------|
| $\mathbf{p}$ | Current UGV position $(x, y, z)$ |
| $\mathbf{p}_i$ | Beacon *i* position $(x_i, y_i, z_i)$ |
| $d_i$ | Distance inferred from RSSI |
| $r_i$ | Residual = geometric distance − estimated distance |
| $s_i$ | Combined standard deviation per beacon |
| $\sigma_i$ | Advertised beacon position uncertainty |
| $\hat{\sigma}$ | Estimated global uncertainty |

The weighted least-squares estimator is:

$$
\hat{\mathbf{p}} =
\arg\min_{\mathbf{p}}
\sum_i
\frac{
\left(\|\mathbf{p} - \mathbf{p}_i\| - d_i\right)^2
}{s_i^2}
$$