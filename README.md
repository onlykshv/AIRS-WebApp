# AIRS-WebApp

# Ransomware Incident Knowledge Graph & Analytics Platform

## Project Description

This project provides an automated framework for analyzing ransomware incidents using graph-based knowledge representation and actionable analytics. It ingests ransomware-related reports and datasets, extracts key entities and relationships, and visualizes insights in the form of knowledge graphs and summary analytics. The goal is to support cybersecurity analysis, incident investigation, and rapid attribution by organizing complex threat intelligence into an interactive, interpretable data structure.

***

## Features (Completed)

- **Data Ingestion & Processing**
  - Robust file architecture for organizing raw reports (PDF, CSV) and processed datasets
  - Automated extraction of plain text from ransomware-related PDFs using pdfplumber
  - Parsing and transformation of ransomware incident CSV datasets into standardized schemas

- **Entity and Relationship Extraction**
  - Entity recognition using spaCy NER for identifying:
    - Ransomware families
    - Sedd/Exp (cryptocurrency) addresses
    - Threat types/methods
    - IP addresses
    - Technical attributes (time, protocol, port, cluster, etc.)
  - Construction of entity-relation triples for the knowledge graph

- **Knowledge Graph Construction & Visualization**
  - Generation of ransomware family-centric and overall incident knowledge graphs using NetworkX
  - Graph visualization with Matplotlib, including relationship coloring and labeling

- **Analytics & Reporting**
  - Tabulation of top ransomware families, addresses, threats, and other high-frequency entities
  - Identification of overlapping infrastructure (pivot points) for intelligence and reporting

- **Modular Data Management**
  - Reusable and clearly named entity/relation CSV outputs (entities_master.csv, relations_master.csv, families_master.csv)
  - Organization under `/data/processed` for streamlined workflows and future integration

***

## Technologies Used

- **Python** (core scripting, orchestration)
- **pdfplumber** (PDF text extraction)
- **spaCy** (named entity recognition)
- **pandas** (data transformation)
- **NetworkX** (knowledge graph creation)
- **Matplotlib** (graph visualization)

***

**The platform features an end-to-end, script-driven pipeline for transforming threat intelligence into actionable knowledge graphs and analytics, ready for extension and integration into cybersecurity operations.**
