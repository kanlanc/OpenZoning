# OZFS Geospatial Standard
Testing/working files to go in [Minneapolis folder](/source-gis/minneapolis)

### Rationale for approach
To 1) best utilize existing GIS files from jurisdictions, 2) reduce the complexity of maintaining geospatial layers, and 3) avoid the need for a "zoning rules engine" or other mechanism/intelligence for specifying order of operations.

More detail provided in [Issue 9](https://github.com/urban-stack/OpenZoning/issues/9), especially in contrast to _atomization_.

## Zoning District Geospatial Files
in the standard zoning basemap model, geospatially mapped areas/polygons are assigned specific types/categories of zones or districts (e.g. R6, C2, M3, etc.).

OZ Requirements:
- Each Geospatial file has one `district` column
- In each file, each mapped area has _exactly one_ applicable zoning district (e.g. `R2B`)
- Non-contiguous mapped areas may have the same applicable district
- Mapped areas _may not overlap_
- Some geospatial files/layers may only have one mapped area 

The applicable zoning district provides a _lookup code_ that is used to find the relevant zoning _constraints_

### Unmapped Rules/Regulations
There are oftentimes rules, regulations, constraints that are described or specified in text form, but not mapped in GIS, officially or unofficially. Some examples of this are:
- TOD-specific regulations applying within a 1/4-mile of a transit station
- Additional bulk allowed along Wide(r) streets or on corner lots
- Height restriction planes due to nearby airports or view restrictions

For OZ purposes, **these rules must be mapped!**

### The Superdistrict
Similar to the above requirement to map unmapped rules & regs, there's a two-fold need for a citywide district:
1. Constraints that apply citywide (e.g. re: ADUs)
2. City/jurisdiction-specific interpretations (e.g. does attic space count towards FAR)

Point 2 is not being addressed/scoped at this time.

## Layer Ordering/Prioritization
In Minneapolis, there are 4 (likely) geospatial layers being included: Superdistrict, Base Zoning, Built-Form Overlay, and Shoreland Overlay
These are below, with all of the City's overlays shown, though only the Shoreland overlay includes relevant constraints for OZ's purposes.

For OZ, each of these layers are given a prioritization or order of operations, with `0` being the lowest priority

<img src="https://github.com/urban-stack/OpenZoning/assets/18361305/d8395a71-a842-4159-b53b-fb8e8aa415bd" width="20%" height="20%">

### Workflow for intepreting a lot/parcel's zoning constraints
Based on a georeferenced lot (potential mechanisms for specifying a lot are listed in [Issue 60](https://github.com/urban-stack/OpenZoning/issues/60))

The Following steps are require for pulling the resolved constraint values for a lot:
1. the lot is spatially joined/intersected with the next priority layer (starting at `0`)
2. the `district` value is returned
3. the district's applicable constraints are pulled from JSONs (in a defined directory structure) 
4. any previously defined constrains are overwritten
5. the process above (`1.-4.`) is repeated for each layerany full sequence of layers (super district, base/primary zoning, built-form overlay, shoreland overlay)
6. the list of applicable constraints is complete and passed to app
7. the app then _resolves_ the constraints, applying them to the lot 😬

## Geospatial as default file format
For want of another format providing enhanced capabilities, the open source **GeoJSON** is the default geospatial layer format.
GeoJSON specification: https://datatracker.ietf.org/doc/html/rfc7946

GeoJSON stores things inneficiently. As discussed in [Issue 31](https://github.com/urban-stack/OpenZoning/issues/31#issuecomment-1192654438), GeoJSON (newline format) and Geopackage, are both potential future options that produce small file sizes.


## Other points
### Storing zoning geospatial files as Points vs. Polygons
For now, based on the principle of utilizing files as close to the source as possible (i.e. a jurisdiction's GIS files), polygons are assumed.
Decision based on Carole + Paul's discussion 

### Geospatial maintenance with Kart
As noted in [Issue 23](https://github.com/urban-stack/OpenZoning/issues/23), Github does not handle diffs/changes to geospatial files elegantly. If version control ends up being a necessary or valuable feature, then [Kart](https://kartproject.org/) is a potential option to explore.
