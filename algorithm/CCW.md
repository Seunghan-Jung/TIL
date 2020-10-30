<script type="text/javascript"   src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script><script type="text/javascript"    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script><script type="text/x-mathjax-config">  MathJax.Hub.Config({    extensions: ["tex2jax.js"],    jax: ["input/TeX", "output/HTML-CSS"],    tex2jax: {      inlineMath: [ ['′,′′,′'], ["\\(","\\)"] ,  ['','′,′']],      displayMath: [ ['′,′′,′'], ["\\[","\\]"] ],      processEscapes: true    },    "HTML-CSS": { availableFonts: ["TeX"] }  });</script>

# 선분교차알고리즘 CCW

두 선분의 양 끝점의 좌표가 주어졌을 때, 이 두 선분이 교차하는지 확인하는 알고리즘

## CCW

Counter Clock Wise로 세점의 순서가 시계방향인지 반시계방향인지 일직선 상에 있는지 알 수 있는 방법

세 점 $P1(x_1, y_1)$, $P2(x_2, y_2)$, $P3(x_3, y_3)$ 가 있을 때,
$$
(x_2 - x_1)(y_3 - y_1) - (y_2 - y_1)(x_3 - x_1)\\
= (x_1y_2 + x_2y_3 + x_3y_1) - (x_1y_3 + x_2y_1 + x_3y_2)
$$
의 값이 양수이면 $P1$ - $P2$ - $P3$ 순으로 시계방향 음수이면 반시계방향, $0$이면 일직선상에 있게 된다.

```python
from collections import namedtuple

Point = namedtuple('Point', ('x', 'y'))

def ccw(P1: Point, P2: Point, P3: Point):
    x1, y1 = P1
    x2, y2 = P2
    x3, y3 = P3

    return (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)
```

## CCW로 선분 교차 확인하기

두 선분 $\overline{PQ}$, $\overline{RS}$ 가 있을 때, `ccw(P, Q, R) * ccw(P, Q, S)` 와 `ccw(R, S, P) * ccw(R, S, Q)`가 모두 $0$ 이하라면 두 선분은 교차한다.

단, 두 값 모두 $0$일 때는 네 점 모두 일직선에 있기 때문에 $R \le Q$ 이고 $P \le S$이어야 한다. (점의 대소비교는 일반적인 정렬기준이고, 해당 식은 $P \le Q$, $R \le S$ 임을 전제로 한다.)

```python
Line = namedtuple('Line', ('P', 'Q'))

def is_cross(L: Line, M: Line):
    P, Q, R, S = L.P, L.Q, M,P, M.Q
    
    A = ccw(P, Q, R) * ccw(P, Q, S)
    B = ccw(R, S, P) * ccw(R, S, Q)

    if A == 0 and B == 0:
        return M.P <= L.Q and L.P <= M.Q

    return A <= 0 and B <= 0
```

