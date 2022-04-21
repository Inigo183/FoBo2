
(cl:in-package :asdf)

(defsystem "fobo-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Direction" :depends-on ("_package_Direction"))
    (:file "_package_Direction" :depends-on ("_package"))
  ))