store = dict()
multiscales.to_zarr(store)
# For very large images, there are many files.
# When kept as directory stores, this can strain filesystems which are designed to support a limited number of files.
print(len(store.keys()))