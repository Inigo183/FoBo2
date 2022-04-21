# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "led: 1 messages, 0 services")

set(MSG_I_FLAGS "-Iled:/rasp_ws/src/led/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(led_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/rasp_ws/src/led/msg/led.msg" NAME_WE)
add_custom_target(_led_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "led" "/rasp_ws/src/led/msg/led.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(led
  "/rasp_ws/src/led/msg/led.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/led
)

### Generating Services

### Generating Module File
_generate_module_cpp(led
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/led
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(led_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(led_generate_messages led_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/rasp_ws/src/led/msg/led.msg" NAME_WE)
add_dependencies(led_generate_messages_cpp _led_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(led_gencpp)
add_dependencies(led_gencpp led_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS led_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(led
  "/rasp_ws/src/led/msg/led.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/led
)

### Generating Services

### Generating Module File
_generate_module_eus(led
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/led
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(led_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(led_generate_messages led_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/rasp_ws/src/led/msg/led.msg" NAME_WE)
add_dependencies(led_generate_messages_eus _led_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(led_geneus)
add_dependencies(led_geneus led_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS led_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(led
  "/rasp_ws/src/led/msg/led.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/led
)

### Generating Services

### Generating Module File
_generate_module_lisp(led
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/led
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(led_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(led_generate_messages led_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/rasp_ws/src/led/msg/led.msg" NAME_WE)
add_dependencies(led_generate_messages_lisp _led_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(led_genlisp)
add_dependencies(led_genlisp led_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS led_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(led
  "/rasp_ws/src/led/msg/led.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/led
)

### Generating Services

### Generating Module File
_generate_module_nodejs(led
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/led
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(led_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(led_generate_messages led_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/rasp_ws/src/led/msg/led.msg" NAME_WE)
add_dependencies(led_generate_messages_nodejs _led_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(led_gennodejs)
add_dependencies(led_gennodejs led_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS led_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(led
  "/rasp_ws/src/led/msg/led.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/led
)

### Generating Services

### Generating Module File
_generate_module_py(led
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/led
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(led_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(led_generate_messages led_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/rasp_ws/src/led/msg/led.msg" NAME_WE)
add_dependencies(led_generate_messages_py _led_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(led_genpy)
add_dependencies(led_genpy led_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS led_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/led)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/led
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(led_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/led)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/led
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(led_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/led)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/led
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(led_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/led)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/led
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(led_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/led)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/led\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/led
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(led_generate_messages_py std_msgs_generate_messages_py)
endif()
