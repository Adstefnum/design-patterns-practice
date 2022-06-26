# Problem
- Imagine you had to build several houses with different materials but using the same steps.
- Imagine also that you have to build several other houses but you omit some steps like building a swimming pool in one and not building it in another
- The builder pattern enables you to create different builders to take care of building with different materials
- It also allows you to use these same builders that inherit from a single common interface with corresponding products for each builder
- It also allows you to use a director which enables removing steps from a builder to for instance create a product without a step
