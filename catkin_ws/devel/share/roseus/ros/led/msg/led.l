;; Auto-generated. Do not edit!


(when (boundp 'led::led)
  (if (not (find-package "LED"))
    (make-package "LED"))
  (shadow 'led (find-package "LED")))
(unless (find-package "LED::LED")
  (make-package "LED::LED"))

(in-package "ROS")
;;//! \htmlinclude led.msg.html


(defclass led::led
  :super ros::object
  :slots (_status ))

(defmethod led::led
  (:init
   (&key
    ((:status __status) nil)
    )
   (send-super :init)
   (setq _status __status)
   self)
  (:status
   (&optional (__status :null))
   (if (not (eq __status :null)) (setq _status __status)) _status)
  (:serialization-length
   ()
   (+
    ;; bool _status
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _status
       (if _status (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _status
     (setq _status (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get led::led :md5sum-) "3a1255d4d998bd4d6585c64639b5ee9a")
(setf (get led::led :datatype-) "led/led")
(setf (get led::led :definition-)
      "bool status
")



(provide :led/led "3a1255d4d998bd4d6585c64639b5ee9a")


