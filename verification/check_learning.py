#!/usr/bin/env python3
"""Check the shared milestone map, local navigation, and bridge example.

Run from any working directory. --write PATH records the JSON report.
This does not test hosted rendering or establish scientific priority.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

import numpy as np
import verify

ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, description: str) -> None:
    if not condition:
        raise AssertionError(description)


def without_code(text: str) -> str:
    """Remove fenced blocks before inspecting headings and inline mathematics."""
    return re.sub(r'^```[^\n]*\n.*?^```[ \t]*$', '', text, flags=re.M | re.S)


def heading_ids(text: str) -> set[str]:
    """Compute slugs for the simple ATX headings used in this repository."""
    seen: dict[str, int] = {}
    result: set[str] = set()
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', without_code(text), re.M):
        title = re.sub(r'[\*_`]', '', title.strip()).lower()
        slug = ''.join(c for c in title
                       if c in '-_ ' or unicodedata.category(c)[0] in 'LN')
        slug = slug.replace(' ', '-')
        occurrence = seen.get(slug, 0)
        seen[slug] = occurrence + 1
        result.add(slug if occurrence == 0 else f'{slug}-{occurrence}')
    return result


def check_map() -> dict:
    text = (ROOT / 'learning/MILESTONES.md').read_text(encoding='utf-8')
    records = list(re.finditer(r'^### M(\d{2}): (.+)$', text, re.M))
    require([int(m[1]) for m in records] == list(range(1, 31)), 'Need M01–M30 exactly once, in order')
    fields = ('Phase', 'Central question', 'Understanding target', 'Dependencies',
              'Story role', 'Conceptual connection', 'Source pointers')
    edges = 0
    for index, match in enumerate(records):
        number = int(match[1])
        end = records[index + 1].start() if index + 1 < len(records) else len(text)
        body = text[match.end():end]
        for field in fields:
            require(body.count(f'**{field}:**') == 1, f'M{number:02}: missing/duplicate {field}')
        phase = 'Background/preliminaries' if number <= 14 else 'Narrative/innovation'
        require(f'**Phase:** {phase}.' in body, f'M{number:02}: phase mismatch')
        dep_line = re.search(r'^\*\*Dependencies:\*\* (.+)$', body, re.M)
        require(dep_line is not None, f'M{number:02}: no dependency line')
        deps = [int(x) for x in re.findall(r'M(\d{2})', dep_line[1])]
        require(all(1 <= d < number for d in deps), f'M{number:02}: forward or invalid dependency')
        require(len(deps) == len(set(deps)), f'M{number:02}: repeated dependency')
        require(bool(deps) or number == 1, f'M{number:02}: disconnected milestone')
        edges += len(deps)
    for name in ('README.md', 'MILESTONES.md', 'WATROUS_BRIDGE.md'):
        content = (ROOT / 'learning' / name).read_text(encoding='utf-8')
        require('Watrous' in content and '2018' in content, f'{name}: missing selected anchor')
        for personal in ('Revise → Learn', 'COACHING.md', 'retry challenge', 'learner answers'):
            require(personal not in content, f'{name}: personal assessment material')
    require('Watrous2018' in (ROOT / 'references/references.bib').read_text(), 'Missing anchor bibliography')
    require('learning/MILESTONES.md' in (ROOT / 'README.md').read_text(), 'Root learning route missing')
    require('learning/WATROUS_BRIDGE.md' in (ROOT / 'llms.txt').read_text(), 'LLM bridge route missing')
    return {'milestones': 30, 'background': 14, 'narrative': 16, 'dependency_edges': edges,
            'fields_per_milestone': len(fields)}


def check_links_and_math() -> dict:
    files = sorted(p for p in ROOT.rglob('*.md')
                   if not any(part.startswith('.') for part in p.relative_to(ROOT).parts))
    local_count, fragment_count, math_blocks, inline_count = 0, 0, 0, 0
    for path in files:
        text = path.read_text(encoding='utf-8')
        require(len(re.findall(r'^```', text, re.M)) % 2 == 0, f'{path}: unbalanced fences')
        math_blocks += len(re.findall(r'^```math\s*$', text, re.M))
        prose = re.sub(r'`[^`\n]*`', '', without_code(text))
        for line in prose.splitlines():
            delimiters = re.findall(r'(?<!\\)\$', line)
            require(len(delimiters) % 2 == 0, f'{path}: unbalanced inline math')
            inline_count += len(delimiters) // 2
        for target in re.findall(r'\]\(([^\s)]+)\)', text):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            candidate = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            require(candidate.is_relative_to(ROOT), f'{path}: link leaves repository: {target}')
            require(candidate.exists(), f'{path}: missing destination: {target}')
            local_count += 1
            if parsed.fragment:
                require(candidate.suffix == '.md', f'{path}: unsupported local fragment: {target}')
                slug = unquote(parsed.fragment)
                require(slug in heading_ids(candidate.read_text(encoding='utf-8')),
                        f'{path}: missing heading: {target}')
                fragment_count += 1
    return {'markdown_files': len(files), 'local_links': local_count,
            'heading_fragments': fragment_count, 'display_math_blocks': math_blocks,
            'inline_math_expressions': inline_count}


def example_checks() -> dict:
    audit = verify.Audit()
    beta = (1 + 1 / math.sqrt(2)) / 2
    c, s = math.cos(math.pi / 8), math.sin(math.pi / 8)
    bs = (np.array([c, s], dtype=complex), np.array([-s, c], dtype=complex))
    us = verify.bases(2)
    total_success = 0.0
    pgm_values = []
    for bit, b in enumerate(bs):
        k = np.kron(np.eye(2), b.conj()[None, :])
        weight = float(np.trace(k.conj().T @ k).real / 4)
        audit.equal('example_branch_probability', weight, 0.5)
        psi = k.T / math.sqrt(4 * weight)
        rho = psi @ psi.conj().T
        audit.equal('example_reduced_state', rho, np.kron(np.eye(2) / 2, np.outer(b, b.conj())))
        audit.equal('example_rank', np.count_nonzero(np.linalg.eigvalsh(rho) > 1e-10), 2)
        root = verify.psd_power(rho, 0.5)
        audit.equal('example_trace_power', np.trace(verify.psd_power(rho, 0.75)).real, 2**0.25)
        for theta, u in enumerate(us):
            rows = u.conj().T @ psi
            states = [np.outer(row, row.conj()) for row in rows]
            ensemble_average = sum(states)
            inverse = verify.psd_power(ensemble_average, -0.5)
            pgm = float(sum(np.trace(v @ inverse @ v @ inverse).real for v in states))
            diag = np.diag(u.conj().T @ root @ u).real
            audit.equal('example_pgm_identity', pgm, float(diag @ diag))
            audit.equal('example_pgm_value', pgm, 0.75)
            pgm_values.append(pgm)
            u1 = verify.H if theta // 2 else verify.I
            branch_success = 0.0
            for x in range(4):
                if x % 2 == bit:
                    vector = u1[:, x // 2]
                    effect = np.outer(vector, vector.conj())
                    branch_success += float(np.trace(effect @ states[x]).real)
            audit.equal('example_branch_success', branch_success, beta)
            total_success += weight * branch_success / 4
    audit.equal('example_total_success', total_success, beta)
    audit.leq('example_barnum_knill', beta, math.sqrt(0.75))
    audit.leq('example_converse', math.sqrt(0.75), 2**(-1/6))
    # The published bridge distinguishes ordinary and normalized Schatten norms.
    a = np.diag([0.0, 1.0, 2.0, 3.0])
    singular_values = np.linalg.svd(a, compute_uv=False)
    for p in (1, 1.5, 2):
        ordinary = float(np.sum(singular_values**p)**(1/p))
        normalized = float((np.trace(verify.psd_power(a, p)).real/4)**(1/p))
        audit.equal('norm_translation', normalized, 4**(-1/p)*ordinary)
    return {'assertions': sum(audit.counts.values()), 'branch_basis_cases': len(pgm_values),
            'success': total_success, 'pgm_success': float(np.mean(pgm_values)),
            'converse': 2**(-1/6), 'check_counts': audit.counts,
            'maximum_identity_errors': audit.max_errors,
            'maximum_positive_inequality_violations': audit.max_violation}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', type=Path)
    args = parser.parse_args()
    result = {'status': 'passed', 'anchor': 'Watrous, The Theory of Quantum Information (2018)',
              'milestone_map': check_map(), 'navigation_and_math_source': check_links_and_math(),
              'worked_example': example_checks(), 'hosted_rendering': 'not_verified',
              'limits': ['Structural checks do not assess a reader or validate every explanation.',
                         'Balanced delimiters are not a mathematical-rendering test.',
                         'The worked example is not optimization over all collective strategies.',
                         'Live GitHub rendering and remote integration require separate verification.']}
    report = json.dumps(result, sort_keys=True, indent=2) + '\n'
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(report, encoding='utf-8')
    print(report, end='')


if __name__ == '__main__':
    main()
