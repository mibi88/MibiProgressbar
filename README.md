# MibiProgressbar
Display a progress bar in your terminal !

# Install

`pip install mibiprogressbar`

# Getting Started

## Import them

```python
from MibiProgressbar import *
```
## Build them

```python
pbar = pbar.buildbar()
```

## Example

```python
###EXAMPLE###
import time

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
