# λambeq documentation

![Build status](https://github.com/quantinuum/lambeq-docs/actions/workflows/docs.yml/badge.svg)
[![License](https://img.shields.io/github/license/quantinuum/lambeq-docs)](LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/lambeq)](//pypi.org/project/lambeq)
[![PyPI downloads](https://img.shields.io/pypi/dm/lambeq)](//pypi.org/project/lambeq)
[![arXiv](https://img.shields.io/badge/arXiv-2110.04236-green)](//arxiv.org/abs/2110.04236)

## About this repository

This repository holds the documentation of the [lambeq Python library](https://github.com/quantinuum/lambeq).

## About lambeq

lambeq is a toolkit for quantum natural language processing (QNLP).

- Documentation: https://docs.quantinuum.com/lambeq/
- User support: <lambeq-support@quantinuum.com>
- Contributions: Please read [our guide](https://docs.quantinuum.com/lambeq/CONTRIBUTING.html).
- If you want to subscribe to lambeq's mailing list, let us know by sending an email to <lambeq-support@quantinuum.com>.

## Getting started with lambeq

### Prerequisites

- Python 3.10+

### Installation

lambeq can be installed with the command:

```bash
pip install lambeq
```

The default installation of lambeq includes Bobcat parser, a statistical parser (see [related paper](https://arxiv.org/abs/2109.10044)) fully integrated with the toolkit.

To install lambeq with optional dependencies for extra features, run:

```bash
pip install lambeq[extras]
```

To enable DepCCG support, you will need to install the external parser separately.

---
**Note:** The DepCCG-related functionality is no longer actively supported in `lambeq`, and may not work as expected. We strongly recommend using the default Bobcat parser which comes as part of `lambeq`.

---

If you still want to use DepCCG, for example because you plan to apply ``lambeq`` on Japanese, you can install DepCCG separately following the instructions on the [DepCCG homepage](//github.com/masashi-y/depccg). After installing DepCCG, you can download its model by using the script provided in the `contrib` folder of this repository:

```bash
python contrib/download_depccg_model.py
```

## Usage

The [docs/examples](//github.com/quantinuum/lambeq-docs/tree/main/docs/examples)
directory contains notebooks demonstrating usage of the various tools in
lambeq.

Example - parsing a sentence into a diagram (see
[docs/examples/parser.ipynb](//github.com/quantinuum/lambeq-docs/blob/main/docs/examples/parser.ipynb)):

```python
from lambeq import BobcatParser

parser = BobcatParser()
diagram = parser.sentence2diagram('This is a test sentence')
diagram.draw()
```

## Testing lambeq

Run all tests with the command:

```bash
pytest
```

Note: if you have installed lambeq in a virtual environment, remember to
install pytest in the same environment using pip.

## Building documentation

The prose pages are MDX under `docs/`; the notebooks under `docs/` and the API
reference (from `quartodoc/`) are rendered into MDX at build time. The tooling
comes from the [documentation-ui](https://github.com/quantinuum-dev/documentation-ui)
repository: check it out (and build it) beside this one, then from this
repository's root run:

```bash
# Generate the notebook + API pages and build a static site into build/site
node <path-to>/documentation-ui/docs-preview/bin/docs-preview.mjs build --full

# Or serve a live preview at http://localhost:3000/lambeq/
node <path-to>/documentation-ui/docs-preview/bin/docs-preview.mjs dev --full
```

Generating needs [Quarto](https://quarto.org/), [pandoc](https://pandoc.org/)
and [uv](https://docs.astral.sh/uv/). After the first `--full` run, drop
`--full` to reuse the generated pages. Serve a static build from its root with
any file server, e.g. `npx serve build/site`.

`docs/public/lambeq-assets/` holds only the images the MDX prose pages use;
notebook output images and downloads are extracted from the notebooks at build
time.

CI checks spelling and links with:

```bash
node <path-to>/documentation-ui/docs-checks/bin/check-spelling.mjs docs build/mdx/content/lambeq \
  --api-reference build/mdx/content/lambeq/api
node <path-to>/documentation-ui/docs-checks/bin/check-links.mjs build/site --base-path /lambeq
```

Words specific to lambeq that the spell checker should accept go in
`project-words.txt`.

## License

Distributed under the Apache 2.0 license. See [`LICENSE`](LICENSE) for
more details.

## Citation

If you wish to attribute our work, please cite
[the accompanying paper](//arxiv.org/abs/2110.04236):

```
@article{kartsaklis2021lambeq,
   title={lambeq: {A}n {E}fficient {H}igh-{L}evel {P}ython {L}ibrary for {Q}uantum {NLP}},
   author={Dimitri Kartsaklis and Ian Fan and Richie Yeung and Anna Pearson and Robin Lorenz and Alexis Toumi and Giovanni de Felice and Konstantinos Meichanetzidis and Stephen Clark and Bob Coecke},
   year={2021},
   journal={arXiv preprint arXiv:2110.04236},
}
```
