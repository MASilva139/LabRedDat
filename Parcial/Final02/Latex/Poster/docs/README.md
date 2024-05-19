
# HYposter - LaTeX posters for University of Helsinki
HYposter is a style file for `beamerposter` whose purpose is to simplify the process
of making scientific posters that have a University of Helsinki look with LaTeX.
HYposter tries to look like the "tighter" version of the official poster style.

`beamerposter` is a LaTeX package that uses `beamer` for typesetting posters.


## Requirements
LaTeX with [beamer] and [beamerposter]. Most modern LaTeX installations come with
`beamer` included, but you must install `beamerposter` yourself.

## Usage
Once you have beamerposter and the template set up in your LaTeX installation or
working directory, using HYposter is fairly straightforward. Open one of the supplied
templates (either two- or three-column or landscape), and follow the three steps given
in the template:

1. Check that the file encoding is correct.
2. Fill in the title of your poster and your name
3. Add the contents of your poster

### Title lines
The title consists of two lines. The first one will be coloured in the faculty colour,
the second one is grey. Due to technical limitations, you must give these two 
parts separately with the `\titlestart` and `\titleend` commands.

### Authors
Give the authors with the `\author` command. These are put to the right side of the title
in smaller black letters. If you want you can add or skip email ids, name of the department etc.  

### Bottom left corner - Logo(s)
If you want to add logo(s) of various institutes which have supported or cooperated in the work, please upload a single .png file after combining the logos of all involved institutes. It will appear in the lower left corner of the poster. Just make sure that the size of the '.png' is small enough to fit in the lower left corner. 

### Title size
Longer titles don't fit with the default size. If your title is long, you can use
the `\titlesize` command to change the size. The default is `\titlesize{\VeryHuge}` or `\titlesize{\VERYHuge}`.
The best choice for a longer title is `\Huge`. If you need to go smaller than that,
your title is probably too long for a poster, but you can try `\LARGE`.

### Orientation
Right now the orientation is set to be 'Portrait'.
You can set `orientation=landscape` in the `beamerposter` settings to make a landscape
poster. The head part is typeset a bit differently to save space and look better. You might have to make adjustments in the '.sty' files after selecting 'landscape' orientation.

### Column length
The columns are essentially just vertical boxes. There is no wrapping over them,
which means that if you put too much stuff into a column, it will simply flow over the bottom edge of the page. You must make sure that your contents fit the columns.

### Number of columns
The column width is fixed at the beginning by setting either `twocolumn`, `threecolumn`
or `fourcolumn` (or nothing, which defaults to `threecolumn`) in the \usetheme options. 
This means that you must use that number of `\newcolumn` commands to make the columns. 
Any less and you'll have an empty space; any more, and the additionsl columns will go 
outside the page. Four columns are really only meant for landscape orientation, they're
too narrow on a portrait poster.





