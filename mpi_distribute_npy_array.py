from mpi4py import MPI
import numpy as np
import hashlib

def load_data_portion(file_path, start, end):
    # Load the entire data.npy as a memory-mapped array, but only the metadata is read into memory
    data_mmapped = np.load(file_path, mmap_mode='r')

    # Extract the portion of data
    portion = data_mmapped[start:end, :, :]
    return portion

def sha256_hash(data):
    data_bytes = data.tobytes()
    sha256 = hashlib.sha256()
    sha256.update(data_bytes)
    return sha256.hexdigest()

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Define the portion of data you want to read
start = rank * 2
end = start + 2

# Read the portion of 3D data from the binary NumPy data file
portion = load_data_portion('data.npy', start, end)

# Distribute the portion of data to another processor using MPI
if rank == 0:
    sent_data_hash = sha256_hash(portion)
    comm.send(portion, dest=1)
    print(f'Processor {rank} sent data to processor 1')
    print(f'Sent data hash: {sent_data_hash}')
elif rank == 1:
    received_data = comm.recv(source=0)
    received_data_hash = sha256_hash(received_data)
    print(f'Processor {rank} received data from processor 0')
    print(f'Received data hash: {received_data_hash}')

