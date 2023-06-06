<h1 align="center">CVERMEER</h1>

_<h4 align="center">A GUI library for opencv's frames.</h4>_

CVermeer, who's name is inspired by renowned artist [Johannes Vermeer](https://fr.wikipedia.org/wiki/Johannes_Vermeer), is a library based on [OpenCV](https://opencv.org/) to ease the process of adding shapes onto opencv's frames.

The library manipulates `Widgets`, which contains other widgets, and can be drawn onto the frame through the `draw()` method, that each widget impements.

___

**Technos :** Python, OpenCV

**Version :** 0.0.0

**Author :** Anatole de Chauveron

___

## Summary

- [Summary](#summary)
- [Getting started](#getting-started)
  - [Requirements](#requirements)
  - [Install](#install)

## Getting started

### Requirements

**Python**

```bash
python --version
# Python 3.8.10
```

### Install

To add the library to your project, you can run the following commands, according to the dependency manager you are using.

**Pip**

```bash
pip install git+https://github.com/ocular-systems/cvermeer.git
```

**Poetry (recommanded)**

```bash
poetry add git+https://github.com/ocular-systems/cvermeer.git
```

> Poetry is recommanded, because if you are using this library, there is a good chance that you are already using opencv, so it will probably already be installed and managed by your dependencies.
