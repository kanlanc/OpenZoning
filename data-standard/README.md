# OZFS Data Standard
_Will go here_
TODO: Link to definitions in the [Glossary](glossary.md) where possible. E.g. [Lot Area](glossary.md#lot-area)

Testing/working files to go in [Examples folder](/examples)


## Constraint Structure
Stored in hierarchy of:

- [lot](glossary.md#lot)
  - [structure](glossary.md#structure)
    - [floor](glossary.md#floor)

Repeatable structures within above:
- [bulk](glossary.md#bulk) (option)
- [base](glossary.md#base)
  - [height](glossary.md#height)
  - [setback](glossary.md#setback)
  - [plane](glossary.md#plane)

  
## constraints & modifiers
#### Edges:
- front
- rear
- side

#### Dimensions:
in ft / sq ft
- [width](glossary.md#width)
- [depth](glossary.md#depth)
- [area](glossary.md#area)
- [frontage](glossary.md#frontage)

#### Counts:
- min
- max
- numberOf
- per
  - Acre
  - DU (dwelling unit)
  - Lot


## special definitions

### roof
TBD

### max
when used as a _suffix_, defines or applies to the top-most floor, height, etc.

### corner

## other constraints
- [FAR](glossary.md#FAR) / [Floor Area](glossary.md#floor-area)
- Parking
- [Units](glossary.md#units)
- Use types
  - Use groups
    - Uses

## variants
### bonuses


## Open questions:
- how to store ratios/formulas
  - purely numeric (e.g. `6:1` sky exposure plane)
  - relating to fixed figures (e.g. height can be 2X lot width)
  - relating to development decisions (e.g. tower can contain at most 45% of lot FAR)
