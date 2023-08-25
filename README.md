# ML introspection

- [x] load pretrained model (cifar10 or smth)
- [x] generate seeded random input
- [x] run model on input
- [x] check that results are deterministic
- [ ] examine generated C code
- [ ] examine generated assembly
- [ ] automate the introspection (parse AST?)

# setup

- clone submodules (tinygrad) with `git submodule update --init --recursive`
- install tinygrad with `pip install -e tinygrad`