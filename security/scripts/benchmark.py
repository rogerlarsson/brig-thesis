#!/usr/bin/env python
# encoding: utf-8

import sys
import json
import time
import timeit
import subprocess

BINARY="./data/main"
INPUTFILE="./data/movie_256"

BLOCKSIZES = [(2**x) for x in range(6,29)]

#[
#    128, 512, 1024, 4096, 32768, 65536, 131072, 262144, 524288,
#    1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864,
#    134217728, 268435456
#]
COMPRESSION_ALGOS = ["none", "lz4", "snappy"]
ENCRYPTION_ALGOS = ["none", "aes", "chacha"]
RUNS=10

def setup(size=256):
    for cmd in [
        "mkdir -p data",
        "sudo mount -t ramfs -o size=2G ramfs data",
        "sudo chmod 0777 data",
        "sudo dd if=/dev/urandom of=./data/movie_{0} bs=1M count={0} conv=sync".format(size),
        "sudo chown -R qitta:users data",
        "cp ./main ./data/main"
    ]:
        if subprocess.call(cmd.split(), shell=False) != 0:
            return "Error occured during setup."
    return None

def teardown():
    for cmd in ["sudo umount -l data", "sudo rm data -rv"]:
        if subprocess.call(cmd.split(), shell=False) != 0:
            return "Error occured during teardown."
    return None

def build_cmd(data, block):
    cmd = "{binary} -b {block} -D -e -n {enc} -c -a {zip} -f {inputfile}".format(
            binary=BINARY,
            block=block,
            enc=data["encryption"],
            zip=data["compression"],
            inputfile=INPUTFILE
        )
    return cmd.split()

def write_bench_data(data):
    filename = "{sys}_{type}_{enc}_{zip}.json".format(
        sys=data["system"],
        type=data["type"],
        enc=data["encryption"],
        zip=data["compression"]
    )
    with open(filename, "w") as fd:
        print("Writing {0}".format(filename))
        fd.write(json.dumps(data))

def get_input_parameters(system, encryption, compression, title, runs):
    if encryption not in ENCRYPTION_ALGOS or compression not in COMPRESSION_ALGOS:
        print("Invalid compression/encryption algorithm.")
        return None

    return {
        "encryption": encryption,
        "compression": compression,
        "title": title,
        "runs": runs,
        "results": [],
        "system": system,
        "type": "unknown"
    }

def read_benchmark(system, encryption, compression, title, runs=10):
    data = get_input_parameters(system, encryption, compression, title, runs)
    if data is None:
        print("Something went wrong - no correct data template available.")
        sys.exit(-1)

    print("** Running bench using {0} runs. **".format(data["runs"]))

    print("Parameters for this run: {0}.".format(data))
    for blocksize in BLOCKSIZES:
        cmd = "subprocess.call({cmd})".format(
            cmd=build_cmd(data, blocksize)
        )
        print("{0} bytes blocksize run...".format(blocksize))
        run = timeit.timeit(cmd, number=data["runs"], setup="import subprocess")
        data["results"].append(round(run/data["runs"]*1000))

    data["type"] = "read"
    return data

if __name__ == '__main__':

    try:
        ret_code = setup()
        if ret_code is not None:
            print("Cannot setup ramfs.", ret_code)
            sys.exit(-1)

        system = "unknown"
        if len(sys.argv) == 2:
            system = sys.argv[1]
        data = read_benchmark(system=system, encryption="aes", compression="none", title="AES-GCM", runs=RUNS)
        write_bench_data(data)
        data = read_benchmark(system=system, encryption="none", compression="none", title="Go-Baseline", runs=RUNS)
        write_bench_data(data)
        data = read_benchmark(system=system, encryption="chacha", compression="none", title="ChaCha20/Poly1305", runs=RUNS)
        write_bench_data(data)
    except KeyboardInterrupt:
        print("Interrupted by user.")
    finally:
        teardown()