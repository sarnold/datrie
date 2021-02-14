# find first using DATRIE_PATH if set
#
find_path(DATRIE_INCLUDE_DIR triedefs.h
          PATHS ${DATRIE_PATH} ENV DATRIE_PATH
          PATH_SUFFIXES include include/datrie NO_DEFAULT_PATH)

find_path(DATRIE_INCLUDE_DIR triedefs.h
          PATH_SUFFIXES include include/datrie)

find_library(DATRIE_LIBRARY  NAMES datrie libdatrie
             PATHS ${DATRIE_PATH} ENV DATRIE_PATH
             PATH_SUFFIXES lib lib64 lib/datrie lib64/datrie NO_DEFAULT_PATH)

find_library(DATRIE_LIBRARY NAMES datrie libdatrie
             PATH_SUFFIXES lib lib64 lib/datrie lib64/datrie)

set(DATRIE_LIBRARIES ${DATRIE_LIBRARY})
set(DATRIE_INCLUDE_DIRS ${DATRIE_INCLUDE_DIR})

include(FindPackageHandleStandardArgs)

find_package_handle_standard_args(Datrie
                                  DEFAULT_MSG
                                  DATRIE_LIBRARY
                                  DATRIE_INCLUDE_DIR)

mark_as_advanced(DATRIE_INCLUDE_DIR DATRIE_LIBRARY)
