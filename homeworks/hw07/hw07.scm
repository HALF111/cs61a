; Q1. Filter Lst
(define (filter-lst fn lst)
  ; 'YOUR-CODE-HERE
  (cond
    ((null? lst) lst)
    ((fn (car lst)) (cons (car lst) (filter-lst fn (cdr lst))))
    (else (filter-lst fn (cdr lst)))
  )
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)


; Q2. Interleave
(define (interleave first second)
  ; 'YOUR-CODE-HERE
  (cond
    ( (null? first) second )
    ( (null? second) first )
    ( else (cons (car first) (cons (car second) (interleave (cdr first) (cdr second)))) )
  )
)

(interleave (list 1 3 5) (list 2 4 6))
; expect (1 2 3 4 5 6)

(interleave (list 1 3 5) nil)
; expect (1 3 5)

(interleave (list 1 3 5) (list 2 4))
; expect (1 2 3 4 5)


; Q3. Accumulate
(define (accumulate combiner start n term)
  ; 'YOUR-CODE-HERE
  (combiner start (acc_helper combiner n term 1))
)

(define (acc_helper combiner n term i)
  ; 'YOUR-CODE-HERE
  (if (= i n)
    (term i)
    (combiner (term i) (acc_helper combiner n term (+ i 1)))
  )
)


; Q4. No Repeats
; Reference Answer：https://cs61a.org/hw/sol-hw08/#q4-no-repeats
(define (no-repeats lst)
  ; 'YOUR-CODE-HERE
  (if (null? lst)
    lst
    (cons (car lst) ( no-repeats (filter-lst (lambda (x) (not (= (car lst) x))) lst) ))
  )
)

