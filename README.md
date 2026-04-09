# goit-pythonweb-hw-04
## setup project
### install packages
```bash
pip install -r requirements.txt

```
### create folders and files
```bash
python create_files.py
```
#### source dir example
```
tree src_dir/ | head -n15
src_dir/
├── choose
│   ├── across.csv
│   ├── area.wav
│   ├── away.css
│   ├── pass.xls
│   ├── popular
│   │   ├── add
│   │   │   ├── age.js
│   │   │   ├── before.odp
│   │   │   ├── remember.flac
│   │   │   ├── southern.gif
│   │   │   └── test.avi
│   │   ├── avoid.json
│   │   ├── country

```
## run script
```
usage: main.py [-h] [-d DSTDIR] [-v] [-f] srcdir

Recursive concurrent file copier.

positional arguments:
  srcdir               source directory

options:
  -h, --help           show this help message and exit
  -d, --dstdir DSTDIR  destination directory
  -v, --verbose        show progress logs
  -f, --fullpath       create original subdirectory structure in destination

```

```bash
python main.py src_dir/ -d dst_dir
```
```
tree dst_dir/ | head -n20
dst_dir/
├── avi
│   ├── arm.avi
│   ├── artist.avi
│   ├── country.avi
│   ├── design.avi
│   ├── gun.avi
│   ├── language.avi
│   ├── listen.avi
│   ├── message.avi
│   ├── most.avi
│   ├── policy.avi
│   ├── represent.avi
│   ├── response.avi
│   ├── test.avi
│   └── western.avi
├── bmp
│   ├── behind.bmp
│   ├── foreign.bmp
│   ├── nearly.bmp

```

### run with --fullpath option
```bash
python main.py -f src_dir/ -d dst_dir
```

```
tree dst_dir/ | head -n30
dst_dir/
├── avi
│   ├── choose
│   │   ├── popular
│   │   │   ├── add
│   │   │   │   └── test.avi
│   │   │   └── country
│   │   │       └── represent.avi
│   │   └── writer
│   │       ├── response.avi
│   │       └── training
│   │           └── western.avi
│   ├── employee
│   │   ├── produce
│   │   │   ├── dog
│   │   │   │   └── country.avi
│   │   │   ├── easy
│   │   │   │   └── listen.avi
│   │   │   └── gun.avi
│   │   ├── Republican
│   │   │   ├── try
│   │   │   │   └── language.avi
│   │   │   └── worry
│   │   │       └── message.avi
│   │   └── test
│   │       └── star
│   │           └── design.avi

```