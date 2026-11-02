#!/usr/bin/env bash
set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
report_name=Lattice_Memory_Certification_Report
source_path="$repo_root/learning/source/$report_name.tex"
output_path=${1:-/tmp/lattice-report-build}
mkdir -p -- "$output_path"
output_path=$(CDPATH= cd -- "$output_path" && pwd)

pdflatex --version | head -n 1
for pass in 1 2; do
    pdflatex -interaction=nonstopmode -halt-on-error \
        -output-directory="$output_path" "$source_path" \
        > "$output_path/build-pass-$pass.txt"
done
test -s "$output_path/$report_name.pdf"
test -s "$output_path/$report_name.log"
printf 'Fresh PDF: %s\nFinal log: %s\n' \
    "$output_path/$report_name.pdf" "$output_path/$report_name.log"
