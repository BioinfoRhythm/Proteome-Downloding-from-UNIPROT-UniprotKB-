# UniProt FASTA batch downloader
# This script downloads protein FASTA sequences from UniProt
# for a list of unique human UniProt accession IDs.
# Assign the path to the txt
# Assign path where fasta files will be downloaded
cmd = """
sort -u /home/neo/human_uniport_fasta/only_human_unique.txt | grep -v '^$' | while read id; do
  wget -q https://rest.uniprot.org/uniprotkb/${id}.fasta \
       -O /home/neo/human_uniport_fasta/${id}.fasta || echo "$id" >> uniprot_not_found.txt
done
"""

subprocess.run(cmd, shell=True, executable="/bin/bash")

