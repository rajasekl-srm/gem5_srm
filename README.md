# 🚀 gem5 + PARSEC 3.0 ARM Integration

This repository contains simulation setup and benchmarking of **gem5 ARM** architecture with **PARSEC 3.0 benchmarks** including power model integration.

---

## ⚙️  Step 1: Build gem5 (ARM)

```bash
git clone https://gem5.googlesource.com/public/gem5
cd gem5
scons build/ARM/gem5.opt -j$(nproc)

---


**## ⚙️ Step 2: Build PARSEC Benchmarks for ARM**

```bash
cd ~/gem5_srm/parsec-3.0
source env.sh
parsecmgmt -a build -p blackscholes -c gcc-hooks

![TerminalOutput](images/blackhole_build.png)








