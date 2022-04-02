cmake_minimum_required(VERSION 3.16.3)

project(AccessSpatialMetadata)

find_package(ITK REQUIRED)
include(${ITK_USE_FILE})

add_executable(AccessSpatialMetadata Code.cxx)
target_link_libraries(AccessSpatialMetadata PUBLIC ${ITK_LIBRARIES})

install(TARGETS AccessSpatialMetadata
  DESTINATION bin
  COMPONENT Runtime
  )

install(FILES Code.cxx CMakeLists.txt Code.py
  DESTINATION share/AccessSpatialMetadata
  COMPONENT Code
  )

enable_testing()
add_test(NAME AccessSpatialMetadataTest
  COMMAND AccessSpatialMetadata
    ${CMAKE_CURRENT_LIST_DIR}/Gourds.png
  )

if(ITK_WRAP_PYTHON)
  add_test(NAME AccessSpatialMetadataTestPython
    COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_LIST_DIR}/Code.py
      ${CMAKE_CURRENT_LIST_DIR}/Gourds.png
    )
endif()
