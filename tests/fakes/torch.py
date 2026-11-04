import os, types, _fk
def set_num_threads(n): _fk.log("threads", n)
cuda = types.SimpleNamespace(is_available=lambda: os.environ.get("FAKE_CUDA") == "1", empty_cache=lambda: None,
                             get_device_name=lambda i=0: "NVIDIA GeForce RTX 3090")
