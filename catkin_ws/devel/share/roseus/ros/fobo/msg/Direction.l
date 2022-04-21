;; Auto-generated. Do not edit!


(when (boundp 'fobo::Direction)
  (if (not (find-package "FOBO"))
    (make-package "FOBO"))
  (shadow 'Direction (find-package "FOBO")))
(unless (find-package "FOBO::DIRECTION")
  (make-package "FOBO::DIRECTION"))

(in-package "ROS")
;;//! \htmlinclude Direction.msg.html


(defclass fobo::Direction
  :super ros::object
  :slots (_x _z ))

(defmethod fobo::Direction
  (:init
   (&key
    ((:x __x) 0)
    ((:z __z) 0)
    )
   (send-super :init)
   (setq _x (round __x))
   (setq _z (round __z))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:serialization-length
   ()
   (+
    ;; int32 _x
    4
    ;; int32 _z
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _x
       (write-long _x s)
     ;; int32 _z
       (write-long _z s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _x
     (setq _x (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _z
     (setq _z (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get fobo::Direction :md5sum-) "eee2fa0953539393a39986ddd18480b3")
(setf (get fobo::Direction :datatype-) "fobo/Direction")
(setf (get fobo::Direction :definition-)
      "int32 x
int32 z
")



(provide :fobo/Direction "eee2fa0953539393a39986ddd18480b3")


