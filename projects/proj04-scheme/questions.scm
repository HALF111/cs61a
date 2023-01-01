(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement


; scm> (zip '((1 2) (3 4) (5 6)))
; ((1 3 5) (2 4 6))
; scm> (zip '((1 2)))
; ((1) (2))
; scm> (zip '())
; (() ())
(define (zip pairs)
  (list (map car pairs) (map cadr pairs))
)
; (define (zip pairs)
;   (if null? pairs
;     (list nil nil)
;     (list (cons (caar s) (car (zip (list (cdr s))))) (cons (car (cdar s)) (cdr (zip (list (cdr s))))))
;   )
; )


(define (enum_helper index lst)
  (if (null? lst)
    lst
    (cons (list index (car lst)) (enum_helper (+ index 1) (cdr lst)))
  )
)
;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (enum_helper 0 s)
)
  ; END PROBLEM 15


;; Problem 16

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
  (cond
    ((null? list1) list2)
    ((null? list2) list1)
    ((comp (car list1) (car list2)) (cons (car list1) (merge comp (cdr list1) list2)))
    (else (cons (car list2) (merge comp list1 (cdr list2))))
  )
)
  ; END PROBLEM 16


(merge < '(1 5 7 9) '(4 8 10))
; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))
; expect (10 9 8 7 5 4 3 1)


;; Problem 17

; Reference: https://github.com/311zzb/cs61a_fall2020/blob/default/projects/scheme/questions.scm
(define (nondecreaselist s)
  ; BEGIN PROBLEM 17
  (if (null? (cdr s))
    (list s)  ; Here is (list s) instead of (list (car s)), which makes it a double-nested list
    (if (> (car s) (cadr s))
      (cons (list (car s)) (nondecreaselist (cdr s)))
      (cons (cons (car s) (car (nondecreaselist (cdr s)))) (cdr (nondecreaselist (cdr s))))
    )
  )
)
  ; END PROBLEM 17

;; Problem EC
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))


; !!!!!!
; ATTETNTION:
; The test in ./tests/EC.py Line 49
; (let-to-lambda '(lambda (x) a (let ((a x)) a))) should be (let-to-lambda '(lambda (x) (let ((a x)) a)))
; and the answer in Line 50 should be (lambda (x) ((lambda (a) a) x)), instead of (lambda (x) a ((lambda (a) a) x))
;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM EC
         expr
         ; END PROBLEM EC
         )
        ((quoted? expr)
         ; BEGIN PROBLEM EC
         expr
         ; END PROBLEM EC
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           (define new_body (map let-to-lambda body))
           (list form params (car new_body))
           ; END PROBLEM EC
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           (define formals (car (zip values)))
           (define args (map let-to-lambda (cadr (zip values))))
           (define new_body (map let-to-lambda body))
           (cons (list 'lambda formals (car new_body)) args)
           ; END PROBLEM EC
           ))
        (else
         ; BEGIN PROBLEM EC
         (map let-to-lambda expr)
         ; END PROBLEM EC
         )))

