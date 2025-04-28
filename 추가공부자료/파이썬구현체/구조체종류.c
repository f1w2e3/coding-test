typedef struct {
    PyObject_HEAD             // (ob_refcnt, ob_type) 기본 헤더
    int co_argcount;          // 함수 인자 개수
    int co_posonlyargcount;   // 위치 전용 인자 개수
    int co_kwonlyargcount;    // 키워드 전용 인자 개수
    int co_nlocals;           // 지역 변수 개수
    int co_stacksize;         // 필요한 스택 크기
    int co_flags;             // 플래그 (e.g. generator)

    PyObject *co_code;        // ★ 실제 바이트코드 (PyBytesObject)
    PyObject *co_consts;      // ★ 상수 테이블 (PyTupleObject)
    PyObject *co_names;       // ★ "사용된 이름" 테이블 (PyTupleObject)
    PyObject *co_varnames;    // ★ "지역 변수 이름" 테이블 (PyTupleObject)
    PyObject *co_freevars;    // 자유변수
    PyObject *co_cellvars;    // 셀 변수

    // (디버그용 정보 생략)
} PyCodeObject;



typedef struct _frame {
    PyObject_HEAD
    struct _frame *f_back;       // 호출자 프레임 (이전 프레임)
    PyCodeObject *f_code;        // 어떤 함수 코드인지
    PyObject *f_locals;          // locals() 딕셔너리 (옵션)
    PyObject *f_globals;         // 글로벌 네임스페이스
    PyObject *f_builtins;        // __builtins__
    PyObject **f_localsplus;     // 진짜 지역변수 + 스택이 여기에 있음
    // ...기타 스택 포인터, 상태 플래그 등
} PyFrameObject;



typedef struct {
    PyObject_VAR_HEAD
    PyTypeObject *ob_type;  // 객체의 타입 정보
    long ob_refcnt;         // 참조 카운트
    // 그 외 객체의 데이터를 저장할 수 있는 공간
} PyObject;
