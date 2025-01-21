# LCWA MODS

This repo contains sample data for use and testing of processing scripts for text/XML.
The sample data comes from the Library of Congress Web Archives (LCWA), a program
that has been selecting, harvesting, and preserving Web sites since 2000. The sample
data is an unsystematically collected sample of metadata for 28 sites preserved
in the [Web archives](http://www.loc.gov/webarchiving/)
at the Library of Congress. The metadata is gathered as sample data for practicing basic 
operations and manipulations of XML information; this metadata is formatted according to the 
structure and schema defined in the [Metadata Object Description Schema (MODS)](http://www.loc.gov/standards/mods/), 
a format initially developed in 2002 for the communication of resource description 
information by libraries and archives. The data is described in more detail below. 
In addition to this readme, this git repository contains:

* Samples of library metadata in MODS XML format:
  1. a file containing a group of 25 MODS records in XML format [here](/2018_lcwa_MODS_25.xml)
  2. a file containing a group of 5 MODS records in XML format [here](/2018_lcwa_MODS_5.xml)
  3. a file with a single MODS record in XML format [here](/2018_lcwa_MODS_single.xml)
  4. a folder (`MODS-in-directories`) with 28 subdirectories that contain individual MODS records for 28 items [here](/MODS-in-directories)
* Jupyter notebooks 
  1. A [notebook with the scripts used to pull and format this data](/Get-Some-LC-Web-Archive-MODs.ipynb)
  2. A [notebook with sample problems and solutions that illustrates various operations that can be undertaken with the XML metadata](/Pulling-from-LCWA-MODS.ipynb) 
* Python scripts
  1. A [script that illustrates how to loop through the `MODS-in-directories` files, extract information, and write it to a csv file](/MODS-to-CSV-test.py)

The Jupyter notebook contains information about downloading
[MODS](http://www.loc.gov/standards/mods/) records for use as sample data to
practice parsing XML in python. These sample files were generated in August of
2018 from MODS metadata records for archived Web sites collected by the Library
of Congress.

Those familiar with the Library may know about the [LCCN](https://www.loc.gov/marc/lccn_structure.html), a general control number that provides unique identifiers for most items that are held by the Library of Congress. The Web archives described in these MODS records do not have LCCNs. Instead, an LCWA (Web Archives) offers a unique identifier for the metadata records.

These are newer MODS records that don't have LCSH:
```
lcwaN0010234,lcwaN0001999,lcwaN0003238,lcwaN0010144,lcwaN0010145,
lcwaN0012178,lcwaN0012179,lcwaN0012180,lcwaN0012184,lcwaN0012195,
lcwaN0010932,lcwaN0010933,lcwaN0010936,lcwaN0010937,lcwaN0010940,
```

These have LCSH in `<subject>`:

`lcwaN0010888,lcwaN0010226,lcwaN0009692,lcwaN0009700,lcwaN0010401`

These are election sites that include `<subject>` both [lcsh](https://en.wikipedia.org/wiki/LCSH)
and "local" headings noted as "lcwat", which represent a taxonomy that was
developed for the quick categorization of sites during the nomination and
harvesting process:

`lcwaE0008846,lcwaE0008263,lcwaE0008338,lcwaE0008918,lcwaE0008001`

These are some previous generation records, which illustrate slight differences in
format and naming convention.

* `lcwa00097019` _Brazilian Presidential Election 2010 Web Archive_
* `dfd3979a7fb56bb3acc06b7b0129633c,00853935a711639f58b0f35bae8d7781` _Example from 2002 Winter Olympics and NYPL (September 11, 2001 Web Archive)_

## Citation

Jesse Johnston. (2025). morskyjezek/LCWA-MODS: Working with MODS and XML in Python (v1.0). Zenodo. https://doi.org/10.5281/zenodo.14709641

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

[![DOI](https://zenodo.org/badge/{github_id}.svg)](https://zenodo.org/badge/latestdoi/{github_id})
