# 📊 Status: Work in Progress
## Android Device Tree for realme C25, C25s & Narzo 50A (even)

The realme C25, realme C25s, and Narzo 50A are budget smartphones from realme, released in 2021. This repository contains the device-specific configuration needed to build LineageOS and based custom ROMs.

![Realme EVEN](https://raw.githubusercontent.com/Badmaneers/device_realme_even_rui4/refs/heads/main/images/6091177406246272107.jpg)

*Image Credit: [@Rem01Gaming](https://github.com/Rem01Gaming)*

---

## 📱 Device Specifications

| Feature | Specification |
| :--- | :--- |
| **SoC (C25)** | MediaTek Helio G70 (12 nm) |
| **SoC (C25s & N50A)**| MediaTek Helio G85 (12 nm) |
| **CPU** | Octa-core (2x2.0 GHz Cortex-A75 & 6x1.8/1.7 GHz Cortex-A55) |
| **GPU** | Mali-G52 MC2 |
| **Memory** | 4 GB RAM |
| **Storage** | 64 GB / 128 GB (eMMC 5.1) |
| **MicroSD** | Dedicated slot (up to 512 GB) |
| **Battery** | Li-Po 6000 mAh, non-removable |
| **Dimensions** | 164.4 x 75 x 9 mm (6.47 x 2.95 x 0.35 in) |
| **Display** | 6.5" IPS LCD, 720 x 1600 pixels, 20:9 ratio (~270 ppi) |
| **Rear Camera** | 48MP (Global) / 13MP (India) / 50MP (N50A) + 2MP Depth + 2MP Macro |
| **Front Camera** | 8 MP |
| **Release OS** | Android 11, realme UI 2.0 (Upgradable to Android 12 & 13) |

---

## 🛠️ Build Instructions

### 1. Initialize the build environment
Initialize the ROM manifest (e.g., LineageOS 21):
```bash
repo init -u https://github.com/LineageOS/android.git -b lineage-21.0
```

### 2. Setup Local Manifests
Clone the local display/device manifests to sync all necessary dependencies (device tree, vendor, kernel):
```bash
git clone https://github.com/Badmaneers/even-manifests.git -b lineage-21 .repo/local_manifests
```

### 3. Sync the repositories
```bash
repo sync -c -j$(nproc --all) --force-sync --no-clone-bundle --no-tags
```

### 4. Setup the build environment
```bash
source build/envsetup.sh
```

### 5. Build the ROM
```bash
lunch lineage_even-userdebug
mka bacon
```

---

