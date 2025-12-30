# Proteome-Downloding-from-UNIPROT-UniprotKB-
This repository contains a Python script that automates the batch download of UniProt FASTA protein sequences for a list of human UniProt accession IDs. The script ensures uniqueness, skips empty entries, and logs missing or invalid UniProt IDs.
# Overview
The script reads a text file containing UniProt accession IDs, removes duplicates, and downloads the corresponding protein FASTA files using the UniProt REST API. Any IDs that fail to download are recorded for later inspection.
This tool is especially useful for bioinformatics workflows that require large-scale protein sequence retrieval, such as proteomics, functional annotation, or machine learning dataset preparation.
# Features

Removes duplicate UniProt IDs automatically.

Ignores empty lines in input file.

Downloads FASTA sequences directly from UniProt.

Saves one FASTA file per UniProt ID.

Logs missing or deprecated IDs without stopping execution.

Easily integrable into Python-based pipelines.

# Input File
Plain text file

One UniProt accession ID per line
# Output

Individual FASTA files named by UniProt ID
