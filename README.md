# LCWA MODS

This repo contains sample data for use and testing of processing scripts for text/XML. 
The data, which reflects metadata for items collected by the Library of Congress, is
described in more detail below. In addition to this readme, the repository
contains:
* a Jupyter notebook with the scripts used to pull and format this data
* a file containing a group of 25 MODS records in XML format
* a file containing a group of 5 MODS records in XML format
* a file with a single MODS record in XML format
* a folder (`MODS-in-directories`) with 28 subdirectories that contain individual MODS records for 28 items

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

These are election sites that include `<subject>` with both [lcsh](https://en.wikipedia.org/wiki/LCSH)
and "local" headings noted as "lcwat", which represent a taxonomy that was
developed for the quick categorization of sites during the nomination and
harvesting process:

`lcwaE0008846,lcwaE0008263,lcwaE0008338,lcwaE0008918,lcwaE0008001`

These are some previous generation records, which have slight variety in
format and naming convention.

* `lcwa00097019` _Brazilian Presidential Election 2010 Web Archive_
* `dfd3979a7fb56bb3acc06b7b0129633c,00853935a711639f58b0f35bae8d7781` _Example from 2002 Winter Olympics and NYPL (September 11, 2001 Web Archive)_
