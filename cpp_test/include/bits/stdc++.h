// GCC 전용 헤더인 <bits/stdc++.h>를 Apple clang(libc++)에서도 쓰기 위한 대체본.
// 백준/코드트리에 제출하던 코드를 수정 없이 로컬에서 컴파일하기 위한 용도.
#pragma once

// C 표준 라이브러리
#include <cassert>
#include <cctype>
#include <cerrno>
#include <cfloat>
#include <climits>
#include <cmath>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cwchar>
#include <cwctype>

// C++11 이상 C 호환 헤더
#include <cfenv>
#include <cinttypes>
#include <cstdint>
#include <cuchar>

// 컨테이너
#include <array>
#include <bitset>
#include <deque>
#include <forward_list>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

// 알고리즘 / 반복자 / 수치
#include <algorithm>
#include <iterator>
#include <numeric>
#include <random>
#include <ratio>

// 문자열 / 정규식
#include <regex>
#include <string>
#if __cplusplus >= 201703L
#include <string_view>
#endif

// 입출력
#include <fstream>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <ostream>
#include <sstream>
#include <streambuf>

// 유틸리티
#include <chrono>
#include <complex>
#include <exception>
#include <functional>
#include <initializer_list>
#include <limits>
#include <locale>
#include <memory>
#include <new>
#include <stdexcept>
#include <tuple>
#include <type_traits>
#include <typeindex>
#include <typeinfo>
#include <utility>
#include <valarray>

// 동시성 (코테에선 거의 안 쓰지만 원본과 맞추기 위해 포함)
#include <atomic>
#include <condition_variable>
#include <future>
#include <mutex>
#include <thread>

#if __cplusplus >= 201703L
#include <any>
#include <charconv>
#include <execution>
#include <filesystem>
#include <optional>
#include <variant>
#endif
