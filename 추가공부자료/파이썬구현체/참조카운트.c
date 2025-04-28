#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/*
x=10
y=x
위 파이썬를 실행했을 때 내부동작:
1.PyLong_FromLong(10)를 실행
2.PyLong_FromLong 함수 안에서 Pyobject_New(PyLongObject)를 호출함.
이때 PyLongObject가 힙에 할당되어 객체의 타입을 정하고 참조카운트를 1으로 초기화한다.
3.PyLong_FromLong는 PyLongObject 객체를 생성한 뒤 정수 10을 해당 객체에 설정함.

*PyLongObject는 PyObject의 하위구조체

Py_INCREF는 참조카운트를 1증가시키고 Py_DECREF는 참조카운트를 1감소시킨다. 
객체의 참조카운트가 0이 되면 gc가 객체를 수거함.
*/

// PyObject 구조체
typedef struct PyObject {
    size_t ob_refcnt;      // 참조 카운트
    struct PyTypeObject *ob_type;  // 객체의 타입을 나타내는 포인터
} PyObject;

// PyTypeObject 구조체 (타입을 정의하는 구조체)
typedef struct PyTypeObject {
    const char *tp_name;  // 타입 이름
} PyTypeObject;

// PyLongObject 구조체 (PyObject를 포함)
typedef struct {
    PyObject ob_base;  // PyObject를 포함
    long ob_digit[1];  // PyLongObject만의 고유한 필드
} PyLongObject;

// PyLongObject 생성 함수
PyLongObject* PyLong_FromLong(long val) {
    PyLongObject *long_obj = (PyLongObject*)malloc(sizeof(PyLongObject));  // 메모리 할당
    long_obj->ob_base.ob_refcnt = 1;  // 참조 카운트 초기화
    long_obj->ob_base.ob_type = &PyLong_Type;  // 타입 설정
    long_obj->ob_digit[0] = val;  // 값 설정
    return long_obj;
}

// 참조 카운트 증가 함수
void Py_INCREF(PyObject *obj) {
    obj->ob_refcnt++;  // 참조 카운트 증가
}

int main() {
    // PyTypeObject 생성 (PyLongObject 타입 정의)
    PyTypeObject PyLong_Type = { "int" };

    PyLongObject *obj = PyLong_FromLong(10);  // 10 값으로 PyLongObject 생성 python: x=10
    printf("Value: %ld, RefCount: %ld\n", obj->ob_digit[0], obj->ob_base.ob_refcnt);  // 값과 참조 카운트 출력
    
    //x=10 이후에 y=x로 int 객체 10에 대한 참조 카운트 증가
    Py_INCREF((PyObject*)obj);  // 참조 카운트 증가 python: y=x
    printf("After INCREF, RefCount: %ld\n", obj->ob_base.ob_refcnt);  // 증가 후 참조 카운트 출력

    free(obj);  // 메모리 해제
    return 0;
}
