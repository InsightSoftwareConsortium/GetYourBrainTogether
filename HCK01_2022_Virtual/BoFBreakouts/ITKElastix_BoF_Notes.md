# 1st GYBS hackathon ITKElastix BoF Notes

## Attendees

- Matt McCormick
- Tom Birdsong
- Paul Elliott
- Dženan Zukić
- John Bogovic
- Niels Dekker
- Viktor van der Valk
- Iana
- Marius Staring

## Transform Support

- Most typical: Affine + B-Spline
- Original elastix transform file format:
    - Initial transform + ... + final transform file
    - Plain text (txt), human readable parameter names
- ITK file format
    - Either single-transform for composite-transform file
    - Binary (HDF5) or plain text (tfm), just numeric parameters

New elastix input parameters: *ITKTransformOutputFileNameExtension*, *WriteITKCompositeTransform*.

Used in 3D Slicer, ...

- Translation, Euler, Similarity, and B-Splines transforms
- HDF5 / TFM support for Stack transforms just added!
    - Stack is a stack of groupwise registrations
    - Fiji Java code to parse elastix transformation support, some ITK transform support
        - HDF5 support available
    - napari plugin

## elastix updates

- Modern C++
    - C++17 in the future?
- Following ITK Style
- elastix command line tests, new GoogleTest's 
- file -> binary interface

### Near future plan: Make elastix library-first

- Build elastix command-line exe "2.0" upon ITKEalstix / C++ interface (itk::ElastixRegistrationMethod)
- Extend ITKElastix/C++ interface
    - Python-compatible

## WebAssembly Support

- [itk-wasm](https://wasm.itk.org/)
- [example pipeline](https://github.com/InsightSoftwareConsortium/GetYourBrainStraight/tree/main/HCK01_2022_Virtual/Tutorials/MetadataPreservation/AccessSpatialMetadata)
- Desirables: itk::Transform in memory inputs / outputs (in progress)
- elx::ParameterObject serialization / deserialization as JSON
    - 

## GPU accelerations

- Discrete Gaussian scale-space generation
- https://github.com/InsightSoftwareConsortium/ITKVkFFTBackend
- Pyramid's significant part of registration pipeline

## Open CL support

- https://clesperanto.github.io/
- https://github.com/InsightSoftwareConsortium/ITKClEsperanto
- We should focus on resampling

## WebAssembly

- "build elastix once, use it across windows/mac/linux and from several languages" -Matt
