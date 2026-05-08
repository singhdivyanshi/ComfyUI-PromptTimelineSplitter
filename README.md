# ComfyUI Prompt Timeline Splitter

Simple timeline-based prompt parser for cinematic image-to-video workflows in ComfyUI.

## Features

* Timeline prompt input
* Multi-line cinematic scene parsing
* Timestamp-based prompt formatting
* Beginner-friendly lightweight node

## Example Input

```text id="pc7kn0"
0-3s: cat walks into room

3-6s: cat eats food

6-9s: cat sleeps near window
```

## Current Version

### v1.0.0

* Initial working custom node
* Timeline text parsing
* Basic formatted output
* ComfyUI integration

## Installation

Clone into:

```text id="jz5ej0"
ComfyUI/custom_nodes/
```

Then restart ComfyUI.

## Development Goal

This node is aimed at making timeline-based prompting easier for AI image-to-video workflows in ComfyUI.

Users can describe scene progression over time using simple timestamp-based prompts.

---

I made this node while knowing almost nothing about Python.

Feel free to suggest improvements or report bugs if you run into any issues.