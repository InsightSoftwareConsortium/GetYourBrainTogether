# GYBS -BoF Dataset standards

Daniel Tward
Lydia Ng
Can Ceritoglu
Adam Tyson
Dženan Zukić
Matt McCormick
Iana Vasylieva
Tom Birdsong
John Bogovic


## Orientation on MRI

Can described the situation

## nibabel and related topics

* Dženan showed notebook
* matrices live with corresponding images
  * convert from array ijk to physical xyz
* reorienting images doesn't change the physical coordinates of the thing -Lydia
  * so should "orientation" should not matter for registration (right?)
* Viewers (good ones) correctly show anatomical coordinates when metadata are correct

* "one of the best decisions was to work in RAS all the time" - Bruce Fischl (according to Daniel)
  * generally either axial or sagittal okay -Can 

## Standards for transformations and orientations

* want there to be ANY standard  - Adam
  * trying to be agnostic to alas + species
  * transforms won't be specific
  * but orientation might be specific to animal
  * what does RAS mean across species -Lydia
    * does that make it into the standard?
    * observed similar issue in spinal cord -Adam
  * need a separate related effort for standards re anatomical orientation
    * Bing (?) working with Partha Mitra at CSHL - Daniel
    * good tools are key -Adam
  * Standard not a particular orientation, but a way to describe what your coordinate system is -Daniel
    * limited three letter convention of Analyze was probably not good 
    * we have an implementation of every acronym (specify the origin and any orientation) -Adam
    * BUT 50% people just don't get this concept :( and need hand-holding
  * Say we throw away three letter codes
    * make it pictoral
    * atlases - put it in the coordinate system of some atlas

* Axes names 
  * separate ijk <> xyz
  * what does x mean etc
  * maybe atlases can give meaning to axes and give a pictoral description of what the axes mean

* NGFF will have spaces Dženan
  * e.g. "DICOM patient LPS", "talairach", "allan CCR v2", "my marmoset atlas"
  * viewers should respect these things
  * the tools HAVE to support it, if they don't we're lost 
  * Need libraries and reference implementations
  * And tools had better actually use it

* Situation in Fiji with microscopists depends on what is imaged -John
  * Microscopists do actually care about orientation -Lyida
  * they need to name the orientations

* branglobe
  * users supply orientation and software deals with it appropriately
  * people have own idea of orientation or names of axes or what axes names mean
  * so to simplify it there are no semantic labels (but it should come back)

* three letter acronyms vs matrices
  * matrices are more general (origins and oblique axes)
  * so cant convert back and forth between them
  * may need some sort of convention
  * how to deal with things like oblique axes, orientations
  * have some atlas rotated relative to each other -Adam
    *  just getting the metadata from users/scope to downstream tools
  * Start with matrix as base with acronyms as instance of matrices -Lydia + Dzenan

* Make demos that preserve metadata
  * library

# Pain points

* even converting affines between different tools is hard -Matt
  * often implicit and not well defined
  * NGFF needs to make very careful, specific definitions of everything
* spec needs to come with a validator -Lydia
  * "you said your image was in this orientation, does this look right?" if it doesn't do something about it


* XYZ vs 012
  * there are a variety of approaches
  * MUST be tracked -Matt
  * supporting F-order in zarr is big/impossible ask for many libraries
  * trade-off between options and reasonable support
  * document it
  * use same convention as nrrd
    * "fastest to slowest" need to say what ijk means
    * Write this down, document document document!

* Lydia to help John define orientations
