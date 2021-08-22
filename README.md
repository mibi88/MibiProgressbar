# MibiProgressbar
Display a progress bar in your terminal !

# Install

`pip install mibiprogressbar`

# Getting Started

## Import them

```python
from MibiProgressbar import *
```

## New progressbar
```python
pbar = progressbar(title = "Progress", value = 0, width = 10, char = "█", uchar = "-", after = "")
```
## Build them

```python
pbar = pbar.buildbar()
```
## Display them

```python
pbar.displaybar()
```
## Get them

```python
text = pbar.getbar()
```
## Update them

```python
pbar.updatebar(title = None, value = None, width = None, char = None, uchar = None, after = None)
```

## Example

```python
###EXAMPLE###
import time
from MibiProgressbar import *

pbar = progressbar(title = "Demo", value = "0")
pbar.buildbar()
pbar.displaybar()
time.sleep(1)
pbar.updatebar(value = "25")
pbar.buildbar()
pbar.displaybar()
time.sleep(1)
pbar.updatebar(value = "50")
pbar.buildbar()
pbar.displaybar()
time.sleep(1)
pbar.updatebar(value = "75")
pbar.buildbar()
pbar.displaybar()
time.sleep(1)
pbar.updatebar(value = "100")
pbar.buildbar()
pbar.displaybar()
```
