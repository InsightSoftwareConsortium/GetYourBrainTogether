# 1st GYBS ANTs BoF notes

## GPU multi-resolution pyramid performance acceleration

- WIP: https://github.com/ANTsX/ANTs/pull/1331
- [ITKVkFFTBackend](https://github.com/InsightSoftwareConsortium/ITKVkFFTBackend)

## WebAssembly support

- [itk-wasm](https://wasm.itk.org)
- [Example itk-wasm pipeline](https://github.com/Kitware/itk-vtk-viewer/blob/d613a98e2eb2fede59ddcb874938929eae8171fd/src/IO/Downsample/Downsample.cxx#L47-L180)
- ANTs pipeline
    - Fixed Image
    - Moving Image
    - Initial Transform
    - Method
        - Rigid
        - Affine
        - Syn
        - SynQuick
        - SynCC
        - SynRepro
        - SynQuickRepro
        - Additional options for the preset in ANTsPy and ANTsR docs
    - Output Transform

## HDF5 Transform Support

- .mat ITKTransform for affine
- nifti displacement field as image
- ITK HDF5 support added recently