; Q2
(define (over-or-under num1 num2)
  ; YOUR-CODE-HERE

  ; Solution 1
  ; (begin
  ;   (define x (- num1 num2))
  ;   (cond
  ;       ((> x 0) 1)
  ;       ((= x 0) 0)
  ;       ((< x 0) -1)  
  ;   )
  ; )

  ; Solution 2
  (if (< num1 num2)
    -1
    (if (= num1 num2)
      0
      1
    )
  )
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0


; Q3
(define (make-adder num)
  ; 'YOUR-CODE-HERE
  (lambda (y) (+ num y))
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13


; Q4
(define (composed f g)
  ; 'YOUR-CODE-HERE
  (lambda (x) (f (g x)))
)


; Q5
(define lst
  ; 'YOUR-CODE-HERE
  '((1) 2 (3 4) 5)
)


; Q6
(define (remove item lst)
  ; 'YOUR-CODE-HERE
  (if (null? lst)
    lst
    (if (= (car lst) item)
      (remove item (cdr lst))
      (cons (car lst) (remove item (cdr lst)))
    )
  )
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

