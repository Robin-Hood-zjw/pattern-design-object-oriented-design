# Pattern Design: Object-oriented Design

### Section 1: Creational Design Patterns

<details>
    <summary>Creational Pattern 01</summary><br>

    #### Pattern #001: [Abstract Factory Pattern](https://github.com/Robin-Hood-zjw/pattern-design-object-oriented-design/tree/main/creational%20patterns/abstract%20factory)

**Definition --->**

> a creational design pattern that lets you produce families of related objects without specifying their concrete classes

**Scenario --->**<br>

> Imagine that diverse products are manufactured. Each product has the same different product styles, and each manufacturing style for a product represents a variant of this product.

**Problem --->**<br>

> If a developer created each class for a product with a certain manufacturing style, many individual classes have to be created although some functionalities are the same, so it creates over-coding.

**Solution --->**<br>

> Individual interfaces (classes) shall be initialized for the distinct product family, and then each variant for each interface shall be created following these interfaces.

</details>

<!-- #### Pattern #001: [Abstract Factory Pattern](https://github.com/Robin-Hood-zjw/pattern-design-object-oriented-design/tree/main/creational%20patterns/abstract%20factory)

**Definition --->**

<!-- > a creational design pattern that lets you produce families of related objects without specifying their concrete classes

**Scenario --->**<br>

<!-- > Imagine that diverse products are manufactured. Each product has the same different product styles, and each manufacturing style for a product represents a variant of this product. -->

<!-- **Problem --->**<br> -->

<!-- > If a developer created each class for a product with a certain manufacturing style, many individual classes have to be created although some functionalities are the same, so it creates over-coding. -->

<!-- **Solution --->**<br> -->

<!-- > Individual interfaces (classes) shall be initialized for the distinct product family, and then each variant for each interface shall be created following these interfaces. --> --> -->

#### Pattern #002: [Builder Pattern](https://github.com/Robin-Hood-zjw/pattern-design-object-oriented-design/tree/main/creational%20patterns/builder)

**Definition --->**

> a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code

**Scenario --->**<br>

> The product's manufacturing process can be similar or even the same. Repetitive coding in the same method representation is workload-requiring, so the code structure to alleviate the mass production of objects is helpful.

**Problem --->**<br>

> Imagine that a developer has to design the code for each complex manufacturing step, and each product could require extra similar code structures to manufacture. Such code design elevates the work amount for developers.

**Solution --->**<br>

> A Builder interface (class) is initialized to declare the required methods and fields for the manufacturing of a product family. Each inherited child class (product) is responsible for the manufacturing of a certain product, so builders can be customized by overriding the code in each inherited method.

#### Pattern #003: [Factory Method Pattern](https://github.com/Robin-Hood-zjw/pattern-design-object-oriented-design/tree/main/creational%20patterns/factory%20method)

**Definition --->**

> a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created

**Scenario --->**<br>

>

**Problem --->**<br>

>

**Solution --->**<br>

>

#### Pattern #004: [Prototype Pattern](https://github.com/Robin-Hood-zjw/pattern-design-object-oriented-design/tree/main/creational%20patterns/prototype)

**Definition --->**

> a creational design pattern that lets you copy existing objects without making your code dependent on their classes

**Scenario --->**<br>

>

**Problem --->**<br>

>

**Solution --->**<br>

>

#### Pattern #005: [Singleton Pattern](https://github.com/Robin-Hood-zjw/pattern-design-object-oriented-design/tree/main/creational%20patterns/singleton)

**Definition --->**

> a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance principle

**Scenario --->**<br>

>

**Problem --->**<br>

> The singleton pattern breaks the single responsibility, since it permits the two main responsibilities of this pattern:

**Solution --->**<br>

>
