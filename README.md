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
usage: main.py [-h] [-d DSTDIR] [-v] srcdir
```

```bash
python main.py src_dir/ -d dst_dir
```

### destination dir example
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