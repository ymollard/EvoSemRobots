;; 1) Load ASDF system
(asdf:operate 'asdf:load-op :como-lexicon)

(in-package :como-lexicon)

;; 2) Define your own categories (this function is be called by the experiment to load the categories)
;; Execute with (ctrl + x + e) 
(defun my-get-category-list ()
  (list
   (make-instance 'color-category
                  :id 'black
                  :color-y 0.0
                  :color-u 125.0
                  :color-v 125.0)
   (make-instance 'color-category
                  :id 'white
                  :color-y 255.0
                  :color-u 125.0
                  :color-v 125.0)))

;; 3) Look at the categories you have created. Point your web browser at
;; http://localhost:8000/ and execute the following (ctrl + x + e)
(show-categories)

;; 4) Run a single interaction (output at http://localhost:8000/)
;; Execute with (ctrl + x + e)
(run-single-interaction-exercise-1)

;; 5) Run series (test your categories)
;; 5a) agents are quite successful with few categories. (avg success ~85%)
;; Execute with (ctrl + x + e)
(run-series-exercise-1)

;; 5b) But what if there are more colors? (avg success 50%)
;; Execute with (ctrl + x + e)
(run-single-interaction-exercise-1 :number-of-colors-per-context 4)
;; Execute with (ctrl + x + e)
(run-series-exercise-1 :number-of-colors-per-context 4)

;; 5c) Or if the agents have very different perceptions? (avg success 50%)
;; (this introduces the problem for session 2)
;; Execute with (ctrl + x + e)
(run-single-interaction-exercise-1 :color-stddev 100.0)
;; Execute with (ctrl + x + e)
(run-series-exercise-1 :color-stddev 100.0)

;; 5d) Or both... (avg success 20%)
;; Execute with (ctrl + x + e)
(run-single-interaction-exercise-1 :number-of-colors-per-context 4
                                   :color-stddev 100.0)
;; Execute with (ctrl + x + e)
(run-series-exercise-1 :number-of-colors-per-context 4
                       :color-stddev 100.0)
