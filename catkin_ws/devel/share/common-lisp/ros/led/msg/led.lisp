; Auto-generated. Do not edit!


(cl:in-package led-msg)


;//! \htmlinclude led.msg.html

(cl:defclass <led> (roslisp-msg-protocol:ros-message)
  ((status
    :reader status
    :initarg :status
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass led (<led>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <led>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'led)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name led-msg:<led> is deprecated: use led-msg:led instead.")))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <led>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader led-msg:status-val is deprecated.  Use led-msg:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <led>) ostream)
  "Serializes a message object of type '<led>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'status) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <led>) istream)
  "Deserializes a message object of type '<led>"
    (cl:setf (cl:slot-value msg 'status) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<led>)))
  "Returns string type for a message object of type '<led>"
  "led/led")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'led)))
  "Returns string type for a message object of type 'led"
  "led/led")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<led>)))
  "Returns md5sum for a message object of type '<led>"
  "3a1255d4d998bd4d6585c64639b5ee9a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'led)))
  "Returns md5sum for a message object of type 'led"
  "3a1255d4d998bd4d6585c64639b5ee9a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<led>)))
  "Returns full string definition for message of type '<led>"
  (cl:format cl:nil "bool status~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'led)))
  "Returns full string definition for message of type 'led"
  (cl:format cl:nil "bool status~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <led>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <led>))
  "Converts a ROS message object to a list"
  (cl:list 'led
    (cl:cons ':status (status msg))
))
