# OZFS Data Standard
_Will go here_
TODO: Link to definitions in the [Glossary](glossary.md) where possible. E.g. [Lot Area](glossary.md#lot-area)

Testing/working files to go in [Examples folder](/examples)


## Constraint Structure
Stored in hierarchy of:

- [lot](glossary.md#lot)
  - [structure](glossary.md#structure)
    - [story](glossary.md#story) (i.e. floor)

Repeatable structures within above:
- [mass](glossary.md#building-mass) (option) (i.e. bulk)
- [base](glossary.md#base)
  - [height](glossary.md#building-height)
  - [setback](glossary.md#setback)
  - plane

  
## constraints & modifiers
#### Edges:
- front
- rear
- side

#### Dimensions:
in ft / sq ft
- [width](glossary.md#width)
- [depth](glossary.md#depth)
- area
- [frontage](glossary.md#frontage)

#### Counts:
- min
- max
- numberOf
- per
  - [Acre](glossary.md#acre)
  - [DU (dwelling unit)](glossary.md#dwelling-unit)
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
