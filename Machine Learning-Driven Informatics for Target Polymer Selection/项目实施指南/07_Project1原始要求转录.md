# Project 1 原始要求转录

来源：根目录 `Project 1(1).docx`。本转录从 Word 正文和公式文本提取，保留内容并以 Markdown 重排；Tg 和 R² 分别对应原文公式中的下标与上标。以原始 Word 文件为最终依据。

## Project 1: Machine Learning-Driven Informatics for Target Polymer Selection

### Objective

Develop an end-to-end Python pipeline using supervised machine learning and molecular fingerprinting to predict key thermal and mechanical properties (such as glass transition temperature Tg or elastic modulus) directly from monomer SMILES strings, enabling rapid virtual screening of candidate polymers.

### Workflow & Student Tasks

**Data Curation:** Extract polymer structural data (SMILES) and experimental target properties from open-access databases (e.g., Polymer Genome, PoPE, or PubChem).

**Feature Extraction:** Generate 2D molecular descriptors and topological Morgan fingerprints using RDKit.

**Model Development:** Train and evaluate regression models (Random Forest, XGBoost, and LightGBM) using scikit-learn.

**Virtual Screening:** Deploy the trained surrogate model across a virtual monomer library to screen for candidate polymers matching specific property constraints.

### Prerequisites & Stack

**Tools:** Python (RDKit, scikit-learn, Pandas, Matplotlib)

**Background:** Introductory polymer chemistry and basic supervised machine learning principles

### Expected Deliverables

A documented Jupyter Notebook demonstrating data preprocessing, feature encoding, model evaluation (R², RMSE), and feature importance analysis.

A shortlisted matrix of screened polymer candidates evaluated against literature benchmarks.

## 本指南额外提出的执行建议

只先做 Tg、12–16 周、24 张任务卡、组划分、Dummy、建议样本数/候选数、目录结构、具体字段和调参预算，均为针对初学者提出的实施建议，不是原文逐字要求。PoPE 的入口尚未确认；Polymer Genome 的实际平台定位见 `05`。这些差异已在主指南标明。
