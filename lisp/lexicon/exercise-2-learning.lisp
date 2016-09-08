
;; 1) load system
(asdf:operate 'asdf:load-op :como-lexicon)

(in-package :como-lexicon)

(defclass learned-color-category (color-category blackboard)
  ())

(defclass iteration-counter ( )
  ())

;; implement learner function
(defun exercise-2-learn-hearer (success? word-received topic category-hearer context categories)
  "success - t or nil
   word-received - symbol for the word used by the tutor OR nil
   topic - color
   category-hearer - color-category or nil
   context - list of all colors in the context
   categories - list of all categories known to the learner
   Return - the new list of categories for the learner"
  (cond 
    ((not topic)
     categories) ;; maybe not needed
  ((not category-hearer)
      (setf categories (cons (make-instance 'color-category
                  :id word-received
                  :color-y (color-y topic)
                  :color-u (color-u topic)
                  :color-v (color-v topic))
                             categories))
    )
      (t ; if category is already here
       (setf (color-y category-hearer) 
             (+ (* (color-y category-hearer) 0.98)
               (* (color-y topic) 0.02))) 
       (setf (color-u category-hearer) 
             (+ (* (color-u category-hearer) 0.98)
                (* (color-u topic) 0.02)))
       (setf (color-v category-hearer) 
             (+ (* (color-v category-hearer) 0.98)
                (* (color-v topic) 0.02)))
              
       ))
  
        categories)
 

(defun exercise-2-learn-speaker (success? word-used topic category-speaker context categories)
  "success - t or nil
   word-used - symbol for the word used by the learner OR nil
   topic - color
   category-speaker - color-category or nil
   context - list of all colors in the context
   categories - list of all categories known to the learener
   Return - the new list of categories for the learner"
  categories)

;; 2a) single interaction: execute with (ctrl + x + e)
(run-single-interaction-exercise-2)

;; run more interactions on the same experiment
(continue-interaction-exercise-2)

;; 2b) run a series of interactions (ctrl + x + e)
;; result is about 0% try and improve this
(run-series-exercise-2)

;; 3a) number of random tutor categories
(run-single-interaction-exercise-2 :random-nr-of-tutor-categories 10)

;; 3b) run a series of interactions (ctrl + x + e)
;; result is about 0% with the current strategy! improve it!
(run-series-exercise-2 :random-nr-of-tutor-categories 10)

;; 4a) But what if there are more colors? (avg success 0%)
;; Execute with (ctrl + x + e)'
(run-single-interaction-exercise-2 :number-of-colors-per-context 4
                                   :random-nr-of-tutor-categories 10)
(run-series-exercise-2 :number-of-colors-per-context 4
                       :random-nr-of-tutor-categories 10)

;; 4b) Or if the agents have very different perceptions? (avg success 50%)
;; (this introduces the problem for session 2)
;; Execute with (ctrl + x + e)
(run-single-interaction-exercise-2 :color-stddev 100.0)
;; Execute with (ctrl + x + e)
(run-series-exercise-2 :color-stddev 100.0)


;; 4c) Or both... (avg success 0%)
;; Execute with (ctrl + x + e)
(run-single-interaction-exercise-2 :number-of-colors-per-context 4
                                   :color-stddev 100.0)
;; Execute with (ctrl + x + e)
(run-series-exercise-2 :number-of-colors-per-context 4
                       :color-stddev 100.0)


