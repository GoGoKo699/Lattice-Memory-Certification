# Rebuild the explanatory report

The [report PDF](../learning/report/Lattice_Memory_Certification_Report.pdf) has one editable, self-contained source: [Lattice_Memory_Certification_Report.tex](../learning/source/Lattice_Memory_Certification_Report.tex). Its diagrams and analytic plot are inline TikZ/PGFPlots; no external figures or bibliography are needed.

From the repository root, build into a separate output directory:

```bash
bash verification/build_report.sh /tmp/lattice-report-build
```

The command runs pdfLaTeX twice, prints the actual engine, and requires a fresh PDF and its matching final log. Inspect all pages after changing the source; a warning-free log alone does not establish readable equations, page breaks, figures or tables.

The requested reference environment is pdfLaTeX with TeX Live 2025. The recorded build used pdfTeX 1.40.25 from TeX Live 2023/Debian, with all 14 pages rendered and inspected. TeX Live 2025 compatibility has not yet been verified. The source uses standard TeX Live packages, including Latin Modern, AMS mathematics, TikZ, PGFPlots and tcolorbox.

The report is anonymous and reference-free. Scholarly attribution, imported proof ingredients, and the boundaries of the literature comparison remain in the [scientific references](../references/RELATED_WORK.md). The scientific account is authoritative for exact claims and assumptions.
