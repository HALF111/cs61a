; Q1
(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  ; 'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  ; 'YOUR-CODE-HERE
  (car (cdr (cdr s)))
)


; Q2
(define (sign num)
  ; 'YOUR-CODE-HERE
  (cond
    ((< num 0) -1)
    ((= num 0) 0)
    ((> num 0) 1)
  )
)


; Q3
(define (square x) (* x x))

(define (pow x y)
  ; 'YOUR-CODE-HERE
  (cond
    ( (= y 1) x )
    ( (even? y) (square (pow x (/ y 2))) )
    ( (odd? y) (* (square (pow x (/ (- y 1) 2))) x) )
  )
)

