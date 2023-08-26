# ML introspection

- [x] load pretrained model (cifar10 or smth)
- [x] generate seeded random input
- [x] run model on input
- [x] check that results are deterministic
- [ ] examine generated C code
    - [ ] find actual call to clang
        - multiple calls to get_program, at different levels of call stack
        - clang_random.so in /tmp, find location where it's generated
    - [ ] set breakpoint
    - [ ] find a way to get the code in python directly
- [ ] examine generated assembly
- [ ] automate the introspection (parse AST?)

# setup

- clone submodules (tinygrad) with `git submodule update --init --recursive`
- install tinygrad with `pip install -e tinygrad`