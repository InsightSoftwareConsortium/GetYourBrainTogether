import zlib
zlib_compressed = zlib.compress(chunk_data)

zlib_decompressed = zlib.decompress(zlib_compressed)
assert np.array_equal(np.frombuffer(zlib_decompressed, dtype=np.uint16), chunk_data.ravel())

print(f'Zlib compression: {len(zlib_compressed) / chunk_data.nbytes}')