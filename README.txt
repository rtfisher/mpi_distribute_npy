RTF: 4/11/23

There are two short Python scripts (npy_array_create.py and mpi_distribute_npy_array.py) which generate a sample array and then reads in a subset of the data and distributes it across processes using MPI and memory-mapped arrays.

(Chat-GPT4):
In this corrected script, the load_data_portion function uses np.load with mmap_mode='r' to create a memory-mapped array for the binary NumPy file. This loads the data.npy file from disk as a memory-mapped array, but only the metadata is read into memory. Then it extracts the desired portion of the data directly from the file without loading the entire data cube into memory.

Save the script as mpi_distribute_memmap.py and run it using the mpirun command:

mpirun -np 2 python mpi_distribute_memmap.py

This script adds a sha256_hash() function to generate a SHA-256 hash from a NumPy array. It then calculates the hash values for the sent and received data portions and prints them out. If the sent and received data are identical, their hash values should also be identical.

RTF: This test only works with 2 cores.

(Chat-GPT4 Again With Explanation):
numpy.memmap is a memory-mapped array object that provides a way to read and write large arrays stored in binary files on disk while using a small amount of memory. It works by creating a mapping between the file on disk and a NumPy array in memory. This mapping enables you to access and manipulate the file's content as if it were a regular NumPy array, but only the accessed parts are loaded into memory.

Memory-mapped arrays are particularly useful when working with large datasets that do not fit into your computer's memory. By using numpy.memmap, you can perform operations on large datasets without having to load the entire data into memory.

Here's a brief explanation of how numpy.memmap works:

When you create a memory-mapped array using numpy.memmap, the function opens the specified file on disk, but it doesn't read the entire content into memory. Instead, it creates a mapping between the file and an array in memory.

When you access a portion of the memory-mapped array (e.g., by indexing or slicing), only that portion is read from the file on disk and loaded into memory. This allows you to work with the data as if it were a regular NumPy array, while using only a small amount of memory.

If you modify the memory-mapped array, the changes are not immediately written to the file on disk. Instead, they are stored in memory and written to the file when you either explicitly flush the changes (using the flush method) or when the memory-mapped array is deleted or garbage collected.
