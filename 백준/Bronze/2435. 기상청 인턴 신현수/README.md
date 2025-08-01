# [Bronze I] 기상청 인턴 신현수 - 2435 

[문제 링크](https://www.acmicpc.net/problem/2435) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현, 브루트포스 알고리즘, 누적 합

### 제출 일자

2025년 7월 10일 09:14:00

### 문제 설명

<p>2012년 여름은 너무나 더웠다. 현수는 이런 더위 속에서 컴퓨터 공학과 회장을 게속하는 것은 불가능하다고 생각했다. 결국 그는 2학기 개강을 앞두고 기상청 인턴으로 지원했다.</p>

<p>요즘 꿈의 직장은 기상청이다. 현수는 어떻게든 인턴으로 취직해서 한국 날씨에 큰 별이 되고자 날씨에 관한 모든 것을 공부하기 시작했다.</p>

<p>그는 9시 뉴스를 보며 기상 캐스터 처럼 연습을 하기도 했고, 그 어렵다는 수능 지구과학을 공부하면서 다시 한 번 기상에 대한 기초 지식을 쌓았고, 로욜라 도서관에서 날씨에 대한 책을 모두 읽었다.</p>

<p>드디어 그날이 왔다. 면접 날이다.</p>

<p>기상청 면접관의 질문은 딱 하나였다. </p>

<p>"자네 FA있나?"</p>

<p>현수는 당당하게 말했다. "저는 컴공과 11학번 중, 유일하게 FA가 없습니다!!"</p>

<p>면접관은 흐믓하게 그를 쳐다본 후에 바로 채용하기로 결정했다.</p>

<p>현수는 집에 돌아가는 길에 계속해서 이런 생각이 났다. "왜 FA가 있나 없나를 물어봤을까..? 성실함만 있으면 정말 다 되는 사회인가? 왜 내가 준비한 걸 펼칠 수 있는 기회를 주지 않았을까??"</p>

<p>결국 그는 침대에 누워서 천장을 바라보면서 이런 생각을 계속 했지만, 계속 머리에 맴도는 것은 "컴실2에 늦을까봐 홍태석 어깨를 잡고 뛰어가는 것과, 기상청 면접관의 어이없는 질문 뿐이었다."</p>

<p>드디어 오늘은 현수가 기상청에 출근하는 첫 날이다. 출근 시간은 8시였다. 지금 시간은 7시 58분이다.</p>

<p>기상청 1층이다. 뛰어야겠다. 긴 다리를 이용해 사무실까지 날아가보자.</p>

<p>7시 59분 50초. 아슬아슬하게 도착했다.</p>

<p>"잘했네. 이번 인턴 기간동안 자네가 할 일은 하나네. 매일 아침 9시까지 와서 온도를 측정하고 집에 가면 된다네."</p>

<p>10일동안 이 일을 한 뒤에, 현수는 큰 고민에 빠졌다. </p>

<p>내가 이 일을 왜 하는 것일까?? 안되겠다. 이 데이터를 이용해서 의미 있는 값을 찾아야겠어! 왜 그가 나한테 이 일만을 시켰는지를!!</p>

<p>현수가 10일동안 잰 온도는 다음과 같다.</p>

<p>3 -2 -4 -9 0 3 7 13 8 -3</p>

<p>대체 이게 무슨 의미가 있을까?? 그럼 한 번 연속된 이틀동안 온도의 합을 구해보자.</p>

<p>1 -6 -13 -9 3 10 20 21 5</p>

<p>이제 여기서 가장 큰 값을 찾아보았다. 21</p>

<p>온도의 합이 가장 큰 값은 21이었다. 그래 바로 이거였어!</p>

<p>자 그럼 이제 연속된 5일동안 온도의 합을 구해보자!</p>

<p>-12 -12 -3 14 31 28</p>

<p>그래 이거야 31!!!</p>

<p>현수는 바로 이게 자신이 매일 온도를 재던 이유라는 것을 알았다. (현수는 소수점을 싫어하기 때문에, 온도는 항상 정수이다.)</p>

<p><strong>측정한 온도가 어떤 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값! 이것을 구하면 된다.</strong></p>

<p>현수가 N일동안 측정한 온도가 순서대로 주어졌을 때, 연속적인 K일 동안의 온도의 합이 가장 큰 값을 구해보세요.</p>

### 입력 

 <p>첫째 줄에 두 개의 정수 N과 K가 한 개의 공백을 사이에 두고 주어진다. N은 온도를 측정한 전체 날짜의 수이다. N은 2이상, 100이하이다. K는 합을 구하기 위한 연속적인 날짜의 수이다. K는 1과 N 사이의 정수이다. </p>

<p>둘째 줄에는 매일 측정한 온도를 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 수는 모두 -100이상, 100이하이다.</p>

### 출력 

 <p>첫째 줄에, 온도의 수열에서 연속적인 K일의 온도의 합이 최대가 되는 값을 출력한다.</p>

