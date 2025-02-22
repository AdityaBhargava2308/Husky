# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_animated_person_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED animated_person_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(animated_person_FOUND FALSE)
  elseif(NOT animated_person_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(animated_person_FOUND FALSE)
  endif()
  return()
endif()
set(_animated_person_CONFIG_INCLUDED TRUE)

# output package information
if(NOT animated_person_FIND_QUIETLY)
  message(STATUS "Found animated_person: 0.0.0 (${animated_person_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'animated_person' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${animated_person_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(animated_person_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${animated_person_DIR}/${_extra}")
endforeach()
