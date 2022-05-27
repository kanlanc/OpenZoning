# MAPC Zoning Atlas Technical Appendix notes

### Data Sources

- spatial and tabular data
- both are united by the Zone Code (``ZO_CODE``), which is the concatenation of the Municipal ID (``MUNI_ID``) and the Zone Abbreviation (``ZO_ABBR``) fields

### Spatial Data

- *base zoning districts*
- sourced by:
  - main source: reporting by representatives of municipalities after MAPC outreach
  - downloading from open data portal on munic.'s website
  - data from internal files from past planning projects
  - last resort: GIS spatial data or available data form statewide programs

### Tabular Data

- data from bylaw and ordinance review. Their process for acquiring this data was:
  1. contacted municipal staff for their advice
    - sending a table pre-populated with known districts, all desired fields, and attribute values from the 1999 MassGIS data (where available)
  2. verified this information with their own internal code review
- base zoning districts (`BZD`) & overlay zoning districts (`OZD`)

  - `BZD` tabular data is far more extensive
  - `OZD` tabular data extent is the classification into one of three types:
    - flexible districts — increase development options
    - restrictive districts — decrease development options
    - special districts — targeted application to specific (often legally mandated) uses (telecommunications or adult-use districts)
    - MAPC has not attempted to interpret & standardize `OZDs` yet

### Interpretation of Zoning Districts

- "core fields" covering use allowance and dimensional requirements:
  - minimum lot size
  - dwelling units per acre
  - maximum height
  - maximum floor-area-ratio (`FAR`)
  - multifamily housing permitted? and if a special permit is required
- Zoning Atlas values reflect the as-of-right regulations for all zoning types except for Multifamily
  - MF gets four designations: (`MULFAM2`, `MULFAM3_4`, `MULFAM5_19`, `MULFAM20_`)
    - these capture uses allowed by special permit in addition to what is allowed by as-of-right
  - MAPC clearly shows a bias to increasing MF housing with their Atlas
- **Challenge #1 for MAPC: Not Referenced or Unspecified Core Fields**
  - **very few municipalities use all core fields, so additional fields were provided to account for dimensional regulations that could be used to estimate core fields where these values weren't specified**
    - Maximum Percent Lot Coverage (`PCTLOTCOV`)
      - Minimum Land Area per Dwelling Unit (`LApDU`)
    - Maximum Building Floors (`MAXFLRS`)
    - Maximum Dwelling Units (`MAXDU`)
  - used a hierarchical set of algorithms to calculate core fields from these additional fields
  - whenever information for these additional fields were available, MAPC always filled them regardless of whether it was need to calc. core fields
- **Challenge #2 for MAPC: Multiple By-Right Dimensional Regulations**
  - zones with multiple as-of-right zonings
  - solved this by recording values that correspond to the maximum density allowed for all parcels
    - Residential: Maximum Dwelling Units per Acre
    - Non-residential/mixed-use: `FAR`
  - means that core field values aren't necessarily the highest allowed within the zone, but are the values associated with highest allowable density
  - **this distinction generally only applies to the Minimum Lot Size field, as a larger minimum lot size does not always correspond to the allowance of greater density**

### Field Structure - Base Zoning Districts

- each core field is structured with six attributes:
  1. Zone Value
    - populated when a dimensional regulation (i.e. the value) comes directly from the bylaw or ordinance
  2. Calculated Value(s)
    - populated when the Zone Value values can also be calculated as a function of other explicit values within the bylaws and ordinances. There can be up to three calculated values: multiple calculated values means that all of the unspecified Zone Values (for a given plot?) could not all be calculated with a consistent method because "the referenced regulations were not uniformly available." Calculated fields end in "`_CALC`".
  3. Override Value
    - populated when Calculated Value(s) are unable to be calculated because the required variable values are unavailable, or the Calculated Value(s) seem to be inaccurate. Override fields end in "`_OVE`".
  4. Effective Value
    - populated with the Override Value if specified, otherwise is the average of the Zone Value and all Calculated Values. Effective fields end in "`_EFF`".
  5. Specification Description
    - captures if and how a value is included in the bylaw or ordinance: The three options are:
      1. a dimensional regulation referenced in the zoning code but where the maximum (or minimum) value is specified with a formula
      2. a dimensional regulation referenced in the zoning code but where a value is not defined for that district
      3. a dimensional regulation that is not referenced in the zoning code
    - Null values just means the field is not populated. These fields end in "`_SPEC`".
  6. Estimation Indicator
    - indicates whether the effective value is equal to the Zone Value. Ends in "`_ESVAL`".

### Field Groups

1. Zone Use Type (`ZO_USETY`) - what zonings are allowed in the zone by-right, regardless of zone name

    1. Residential
    2. Non-residential
    3. Residential and Non-residential
    4. Open Space
    5. Classifications 1, 2, and 3 override classification 4. The only plots classified in 4 are those that allow neither residential or non-residential.

2. Multifamily (`MULFAM2`, `MULFAM3_4`, `MULFAM5_19`, `MULFAM20_`)
- A value of:
  - 0 = never allowed
  - 1 = special permit required
  - 2 = by-right
- In instances where MF housing was only allowed in unique circumstances (a conversion of an existing single-family home to a two-family home or when the occupants of the building were elderly and low-income), the field value is a 2.

3. Minimum Lot Size (`MINLOTSIZE`)
- Associated Fields: `MNLS_SPEC`, `MNLS_OVE`, `MNLS_CALC`, `MNLS_EFF`, `MNLS_ESVAL`
- Value Referenced In: `DUpAC_CALC1` , `DUpAC_CALC3` (see " **Field Structure - Base Zoning District**" section)
- Value corresponds to what is prescribed for the greatest density use allowed by-right
- In zones with tiered minimum lot sizes, the value corresponds to the minimum cumulative lot size for the largest structure allowed by-right
  - Example: A zone with a maximum of six dwelling units per lot, which specifies a minimum lot size of 5,000SF for the first dwelling unit and then 2,500SF for each additional dwelling unit would have a ``MINLOTSIZE`` of 17,000SF, equal to ``(5,000SF + (2,500SF * (5 additional dwelling units)``.
  - The base value was recorded when the largest allowable structure could not be determined

4. Maximum Percent Lot Coverage (`PCTLOTCOV`)
- Associated Fields: `PLC_SPEC`, `PLC_OVE`, `PLC_CALC`, `PLC_EFF`, `PLC_ESVAL`
- Value Referenced In: `FAR_CALC`
- Value corresponds to what is prescribed for the greatest density use allowed by-right
- Any lots w/o this value specified in the code has a value of 100%

5. Minimum Land Area Per Dwelling Unit (`LApDU`)
- Associated Fields: `LApDU_SPEC`
- Value Referenced In: `MNLS_CALC`, `MXDU_CALC1`
- In zones with tiered minimum land area per dwelling unit requirements, the value corresponds to the cumulative value for the greatest number of units allowed by-right.

6. Maximum Building Height (`MAXHEIGHT`)
- Associated Fields: `MXHT_SPEC`, `MXHT_CALC`, `MXHT_EFF`, `MXHT_ESVAL`
- Value Referenced In: `MXFL_CALC`
- Where value is not specified in the bylaws or ordinances:
`MXHT_CALC` = `MXFLRS` x 10 (values rounded down)

7. Maximum Building Floors (`MXFLRS`)
  - Associated Fields: `MXFL_SPEC`, `MXFL_CALC`, `MXFL_EFF`, `MXFL_ESVAL`
  - Value Referenced In: `MXHT_CALC`, `MXDU_CALC3`, `FAR_CALC`
  - Where value is not specified in the bylaws or ordinances:
`MXFL_CALC` = `MAXHEIGHT`/ 10 (values rounded down)

8. Maximum Dwelling Units (`MAXDU`)
  - Associated Fields: `MXDU_SPEC`, `MXDU_OVE`, `MXDU_CALC1`, `MXDU_CALC2`, `MXDU_CALC3`, `MXDU_EFF`, `MXDU_ESVAL`
  - Value Referenced In: `MNLS_CALC`, `DUpAC_CALC1`
  - This value is not often included in the section of the bylaw or ordinance that specifies dimensional regulations. When this is the case the "allowable uses in zone" was checked. If the zoning allowed housing by-right but was vague in wording (e.g. a zone that allowed "Multi-family Residential"), the definition of the term was reviewed to see if it specified this value. If it did not, the field was left blank meaning "no maximum specified."
  - For how `MAXDU` is calculated:
[Maximum Dwelling Units Calculation](https://www.notion.so/Maximum-Dwelling-Units-Calculation-95ee4e9388914720837961e0e7074a61)

9. Dwelling Units per Acre (`DUpAC`)
  - Associated Fields: `DUpAC_SPEC`, `DUpAC_OVE`, `DUpAC_CALC1`, `DUpAC_CALC2`,
`DUpAC_CALC3`, `DUpAC_EFF`, `DUpAC_ESVAL`
- Value Referenced In: N/A
- For how `MAXDU` is calculated:
[Dwelling Units per Acre Calculation](https://www.notion.so/Dwelling-Units-per-Acre-Calculation-ce50016f8d8240e3a89a241086d2bb55)

10. Floor-area Ratio (`FAR`)
  - Associated Fields: `FAR_SPEC`, `FAR_OVE`, `FAR_CALC`, `FAR_EFF`
  - Value Referenced In: `MXDU_CALC2`, `DUpAC_CALC2`
  - Where value is not specified in the bylaws or ordinances:

````FAR` = `MXFLR` / `_PCTLOTCOV````
