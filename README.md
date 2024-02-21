# Pattern Design: Object-oriented Design

### Section 1: The Purpose of the Repository

This repo talks about all the 23 design patterns and analyzes the advantages and disadvantages of them.

### Section 2: Creational Design Patterns

#### Pattern #001: Abstract Factory Pattern

**Definition --->**

> a design pattern that produces families of related objects without specifying concrete classes.

**Scenario --->**<br>

> Imagine that diverse products are manufactured. Each product has the same different product styles, and each manufacturing style for a product represents a variant of this product.

**Problem --->**<br>

> If a developer created each class for a product with a certain manufacturing style, many individual classes have to be created although some functionalities are the same, so it creates over-coding.

**Solution --->**<br>

> Individual interfaces (classes) shall be initialized for the distinct product family, and then each variant for each interface shall be created following these interfaces.

#### Pattern #002: Builder Pattern

**Definition --->**

> a design pattern that designs manufacturing complex objects step by step via the same construction code.

**Scenario --->**<br>

> Imagine that a developer has to design the code for each complex manufacturing step, and each product could require extra similar code structures to manufacture. Such code design elevates the work amount for developers.

**Problem --->**<br>

> Individual interfaces (classes) are initialized to declare the required methods and fields for the manufacturing of a product family.

**Solution --->**<br>

> A Builder interface (class) is initialized to declare the required methods and fields for the manufacturing of a product family. Each inherited child class (product) is responsible for the manufacturing of a certain product, so builders can be customized by overriding the code in each inherited method.
