# 🚀 gem5 + PARSEC 3.0 ARM Integration

This repository contains simulation setup and benchmarking of **gem5 ARM** architecture with **PARSEC 3.0 benchmarks** including power model integration.

---

## 📁 Repository Structure
gem5_srm/
├── gem5/ # gem5 source code (ARM build)
├── parsec-3.0/ # PARSEC 3.0 benchmark suite
├── power_model/ # Power model with regression scripts and server
├── power_socket/ # Socket communication implementation
├── shared_directory/ # Shared host-to-guest directory
├── clone.sh # Setup helper script
└── images/ # Diagrams and terminal screenshots used in README


---

## 🧪 Step 1: Build gem5 (ARM)

```bash
git clone https://gem5.googlesource.com/public/gem5
cd gem5
scons build/ARM/gem5.opt -j$(nproc)

---








