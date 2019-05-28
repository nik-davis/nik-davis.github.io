# nik-davis.github.io-src
Source for my blog http://nik-davis.github.io/

To test:

```
pelican content -d -r
pelican -l
```

To publish:

```
pelican content -s publishconf.py && ghp-import output -b master && git push origin master
```
