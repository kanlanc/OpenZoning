### The purpose of this script is to read the shapefiles provided by MAPC, 
### and save them as parquet files (smaller file size).

library(tidyverse)
library(sf)
library(geoarrow)
library(here)

base_districts <- here("MAPC files",
                       "Base Districts") %>%
  st_read()

overlay_districts <- here("MAPC files",
                       "Overlay Districts") %>%
  st_read()

metadata <- here("MAPC files",
                 "Zoning Atlas Metadata.csv") %>%
  read_csv()

write_geoparquet(base_districts, 
         here("MAPC files",
              "base-districts.parquet"))

write_geoparquet(overlay_districts, 
                 here("MAPC files",
                      "overlay-districts.parquet"))