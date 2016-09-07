
(asdf:operate 'asdf:load-op :como-lexicon)

(in-package :como-lexicon)

(defclass my-color-category (color-category blackboard)
  ())

(defun exercise-3-invent-speaker (topic category score context categories)
  "invention of the speaker while trying to express the topic
   topic - color
   category - color-category found in first attempt
   score - discrimination score of the category
   context - list of entities in the context
   categories -  list of categories known to the agent"
  categories)

;; implement learner function (after interaction)
(defun exercise-3-learn-hearer (success? word-received topic category-hearer context categories)
  "success - t or nil
   word-received - symbol for the word used by the tutor OR nil
   topic - color
   category-hearer - color-category or nil
   context - list of all colors in the context
   categories - list of all categories known to the learner
   Return - the new list of categories for the learner"
  (if (and word-received (not category-hearer))
    (cons (make-instance 'color-category
                         :id word-received
                         :color-y (color-y topic)
                         :color-u (color-u topic)
                         :color-v (color-v topic))
          categories)
    categories))

(defun exercise-3-learn-speaker (success? word-used topic category-speaker context categories)
  "success - t or nil
   word-used - symbol for the word used by the learner OR nil
   topic - color
   category-speaker - color-category or nil
   context - list of all colors in the context
   categories - list of all categories known to the learener
   Return - the new list of categories for the learner"
  nil)

;; 2) single interaction: execute with (ctrl + x + e)
(run-single-interaction-exercise-3)

;; run more interactions on the same experiment
;; (continue-interaction-exercise-3)

;; 3) run a series of interactions (ctrl + x + e)
;; result is about 0% with the current strategy! improve it!
(run-series-exercise-3)

;; 4a) But what if there are more colors? (avg success 0%)
;; Execute with (ctrl + x + e)'
(run-single-interaction-exercise-3 :number-of-colors-per-context 4)
(run-series-exercise-3 :number-of-colors-per-context 4)

;; 4b) Or if the agents have very different perceptions? (avg success 0%)
;; (this introduces the problem for session 2)
;; Execute with (ctrl + x + e)
(run-single-interaction-exercise-3 :color-stddev 100.0)
;; Execute with (ctrl + x + e)
(run-series-exercise-3 :color-stddev 100.0)

;; 4c) Or both... (avg success 0%)
;; Execute with (ctrl + x + e)
(run-single-interaction-exercise-3 :number-of-colors-per-context 4
                                   :color-stddev 100.0)
;; Execute with (ctrl + x + e)
(run-series-exercise-3 :number-of-colors-per-context 4
                       :color-stddev 100.0)
